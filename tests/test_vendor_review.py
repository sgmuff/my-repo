from gov import yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree
from gov.vendor_items import SECTIONS


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def call(value):
    return {"value": value, "status": "Provisional", "reason": "Test"}


def review(root, change):
    path = new_record(root, "vr", "lumen-ai", "Lumen AI note-taker", "2026-10-22", "Claude")
    data = yamlio.load(path)
    for c in data["clauses"]:
        c.update(rating="present", evidence="DPA clause", fix="none")
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def rate(data, item, rating):
    next(c for c in data["clauses"] + data["ai"]["items"] if c["item"] == item)["rating"] = rating


def test_a_blank_review_validates_and_renders_with_requirement_text(root):
    path = review(root, lambda d: None)
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "| 2.7 | Deletes or returns all personal data at the end of the services" in text
    assert (root / "compliance/vendors/index.md").is_file()


def test_each_depth_covers_its_checklist_items(root):
    review(root, lambda d: d.update(clauses=[c for c in d["clauses"] if not c["item"].startswith("3.")]))
    assert any("a standard review covers dpa-checklist.md items 3.1" in m for m in found(root, "error"))


def test_a_light_review_needs_fewer_items_and_student_data_adds_section_5(root):
    def light(d):
        d["depth"] = {"value": "light", "reason": "Business contacts only"}
        d["clauses"] = [c for c in d["clauses"] if c["item"][0] in "12" or c["item"] == "7.1"]
    review(root, light)
    assert found(root, "error") == []
    path = next((root / "compliance/vendors").glob("VR-*.yaml"))
    data = yamlio.load(path)
    data["context"] = ["school-data"]
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    assert any("items 5.1, 5.2, 5.3, 5.4, 5.5" in m for m in found(root, "error"))


def test_an_ai_vendor_must_cover_section_6(root):
    def ai(d):
        d["ai"]["applicable"] = True
        d["ai"]["items"] = [{"item": "6.1", "rating": "TBC", "evidence": "TBC", "fix": "TBC"}]
    review(root, ai)
    assert any("ai/items: list each section 6 item once (missing 6.2" in m for m in found(root, "error"))


def test_approving_with_gaps_and_missing_art28_terms_are_findings(root):
    def gaps(d):
        rate(d, "2.7", "missing")
        rate(d, "3.3", "not-provided")
        d["decision"] = call("approve")
    review(root, gaps)
    findings = found(root, "finding")
    assert any("approve without conditions, but these items are gaps or weren't provided: 2.7, 3.3" in m for m in findings)
    assert any("Art. 28(3) terms are missing or overridden (2.7)" in m for m in findings)
    assert any("these gaps have no request and no fix: 2.7, 3.3" in m for m in findings)


def test_requests_answer_the_gap_finding_and_render_as_a_draft_letter(root):
    def asked(d):
        rate(d, "2.7", "missing")
        d["vendor"]["name"] = "Lumen"
        d["requests"] = [{"kind": "contract-change", "request": "Add deletion of all personal data, including backups, within 30 days of termination.", "item": "2.7"},
                         {"kind": "document", "request": "Your current subprocessor list.", "item": "none"}]
    path = review(root, asked)
    assert not any("have no request and no fix" in m for m in found(root, "finding"))
    render_tree(root)
    letter = (path.parent / "requests" / f"{path.stem}-requests.md").read_text()
    assert "DRAFT: not sent." in letter and "## Contract changes we request" in letter
    assert "1. Add deletion of all personal data, including backups, within 30 days of termination. (checklist 2.7)" in letter
    assert "1. Your current subprocessor list.\n" in letter


def test_transfers_need_their_linked_record(root):
    def flows(d):
        d["transfers"] = [{"flow": "Recordings to Lumen Inc.", "destination": "United States", "mechanism": "sccs", "link": "none"},
                          {"flow": "Support access", "destination": "United States", "mechanism": "eu-us-dpf", "link": "none"}]
    review(root, flows)
    findings = found(root, "finding")
    assert any("relies on sccs; link the TIA" in m for m in findings)
    assert any("relies on eu-us-dpf; link the transfer screen (TSR)" in m for m in findings)


def test_section_6_has_thirteen_items():
    assert len(SECTIONS["6"]) == 13 and "6.3a" in SECTIONS["6"]


def test_a_recorded_fix_or_a_multi_item_request_answers_a_gap(root):
    def handled(d):
        rate(d, "2.7", "missing")
        rate(d, "2.8", "partial")
        rate(d, "3.3", "not-provided")
        next(c for c in d["clauses"] if c["item"] == "3.3")["fix"] = "Retrieve the signed DPA from Legal (A3)"
        d["requests"] = [{"kind": "contract-change", "request": "Amend the DPA to add deletion and audit terms.", "item": "2.7, 2.8"}]
    review(root, handled)
    assert not any("have no request and no fix" in m for m in found(root, "finding"))


def test_a_notice_needs_only_section_3_and_an_objection_deadline(root):
    def notice(d):
        d["kind"] = "notice"
        d["clauses"] = [c for c in d["clauses"] if c["item"].startswith("3.")]
    path = review(root, notice)
    assert found(root, "error") == []
    assert any("record the last day to object" in m for m in found(root, "finding"))
    data = yamlio.load(path)
    data["objection_deadline"] = "2026-11-09"
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    assert not any("last day to object" in m for m in found(root, "finding"))
    render_tree(root)
    assert "**Objection deadline:** 2026-11-09" in path.with_suffix(".md").read_text()
