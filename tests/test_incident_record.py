from gov import yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def call(value):
    return {"value": value, "status": "Provisional", "reason": "Test"}


def incident(root, change):
    path = new_record(root, "inc", "misdirected-export", "Customer export sent to the wrong address", "2026-10-22", "Claude")
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def aware(d, time="2026-10-23T18:00", tz="Europe/London", regimes=("uk",), states=()):
    d["awareness"] = {"time": time, "tz": tz, "reasoning": "Recipient replied that they got the file", "confirmed": False}
    d["regimes"], d["states"] = list(regimes), list(states)


def test_render_computes_the_clock_from_the_record(root):
    path = incident(root, lambda d: aware(d))
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "**Earliest deadline:** 2026-10-26 17:00 GMT, UK GDPR" in text  # 72 hours across the autumn clock change
    assert "earliest_deadline: 2026-10-26 17:00 GMT" in text
    assert any("working deadline until the incident commander confirms" in m for m in found(root, "finding"))


def test_a_time_that_doesnt_exist_is_an_error(root):
    incident(root, lambda d: aware(d, time="2026-03-29T02:30", tz="Europe/Berlin", regimes=("gdpr",)))
    assert any("awareness: 2026-03-29T02:30 doesn't exist in Europe/Berlin" in m for m in found(root, "error"))


def test_a_processor_notifies_the_controller_first(root):
    def processor(d):
        aware(d)
        d["datasets"][0]["roles"] = ["processor"]
    incident(root, processor)
    assert any("notifying each controller or owner comes first" in m for m in found(root, "finding"))


def test_a_gdpr_controller_needs_authority_and_individual_rows(root):
    def controller(d):
        aware(d, regimes=("gdpr",))
        d["datasets"][0]["roles"] = ["controller"]
    incident(root, controller)
    findings = found(root, "finding")
    assert any("supervisory authority as its own row" in m for m in findings)
    assert any("individuals as their own row" in m for m in findings)


def test_only_a_person_decides(root):
    def decided(d):
        aware(d)
        d["decisions"] = [{"time": "2026-10-24 09:00 BST", "decision": "Notify the ICO", "by": "Claude", "evidence": "F1", "rationale": "Risk"}]
    incident(root, decided)
    assert any("decisions/0: only a person decides" in m for m in found(root, "error"))


def test_required_notices_need_drafts_and_render_as_drafts(root):
    row = {"recipient": "ICO", "regime": "UK GDPR Art. 33", "required": call(True), "basis": "Risk not unlikely", "deadline": "2026-10-26 17:00 GMT",
           "deadline_kind": "statutory", "owner": "Privacy lead", "status": "drafting"}
    def needs(d):
        aware(d)
        d["matrix"] = [row]
    path = incident(root, needs)
    assert any("ICO: notice is required but no draft exists yet" in m for m in found(root, "finding"))
    data = yamlio.load(path)
    data["notices"] = [{"recipient": "ICO", "text": "On 23 October 2026 a customer export was emailed to the wrong address."}]
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    assert not any("no draft exists" in m for m in found(root, "finding"))
    render_tree(root)
    notices = (path.parent / "notices" / f"{path.stem}-notices.md").read_text()
    assert "DRAFT: not sent." in notices and "## 1. To: ICO" in notices


def test_the_record_warns_while_the_breach_reference_is_only_partly_reviewed(root):
    path = incident(root, lambda d: aware(d))
    render_tree(root)
    assert "Reference status" not in path.with_suffix(".md").read_text()
    from conftest import mark_partial
    mark_partial(root)
    render_tree(root)
    assert "counsel has reviewed only part of us-breach-notification.md" in path.with_suffix(".md").read_text()


def test_a_contractual_due_date_can_be_the_earliest_deadline(root):
    row = {"recipient": "Each district", "regime": "District DPA", "required": call(True), "basis": "DPA clause 9: 48 hours",
           "deadline": "48 hours from discovery", "deadline_kind": "contractual", "due": "2026-10-24T18:00", "owner": "Privacy lead", "status": "drafting"}
    def contract(d):
        aware(d, regimes=("ny2d",), states=("NY",))
        d["datasets"][0]["roles"] = ["school-official", "maintainer"]
        d["matrix"] = [row]
    path = incident(root, contract)
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "**Earliest deadline:** 2026-10-24 18:00 BST, Contractual: Each district" in text
    assert "School official, Maintainer" in text and "NY Education Law 2-d" in text
