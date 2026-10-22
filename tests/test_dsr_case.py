from gov import yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def call(value, reason="Test"):
    return {"value": value, "status": "Provisional", "reason": reason}


def message(kind, sent=None, approved_by="Privacy lead", sent_by="Support lead"):
    return {"message": kind, "to": "Requester", "text": "Dear requester,\n\nWe received your request.", "approved_by": approved_by if sent else None,
            "sent": sent, "sent_by": sent_by if sent else None}


def case(root, change):
    path = new_record(root, "dsr", "access-deletion", "Access and deletion, customer", "2026-10-05", "Claude")
    data = yamlio.load(path)
    data.update(request_types=["access", "deletion"], roles=[{"data": "Customer account", "role": call("controller")}], regimes=["gdpr", "ccpa"])
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def test_deadlines_are_computed_from_the_received_date(root):
    path = case(root, lambda d: d.update(messages=[message("acknowledgment")]))
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "**Earliest deadline: 2026-11-05** (gdpr: Respond (one month, Art. 12(3)))" in text
    assert "| 2026-10-19 | ccpa | Acknowledge (10 business days, CCPA Regs. § 7021) |" in text
    assert "earliest_deadline: 2026-11-05" in text
    drafts = (path.parent / "drafts" / f"{path.stem}-drafts.md").read_text()
    assert drafts.startswith("---") and "DRAFT: not sent" in drafts


def test_claude_never_verifies_approves_or_sends(root):
    def claude(d):
        d["verification"].update(status="verified", by="Claude", date="2026-10-06")
        d["messages"] = [message("response", sent="2026-10-20", approved_by="Claude")]
    case(root, claude)
    errors = found(root, "error")
    assert any("verification: only a person verifies" in m for m in errors)
    assert any("messages/0: only a person" in m for m in errors)


def test_late_extensions_and_responses_are_findings(root):
    def late(d):
        d.update(extended_deadline="2027-01-05", responded="2027-01-10", status="Responded")
        d["verification"].update(status="verified", by="Support lead", date="2026-10-07")
        d["messages"] = [message("extension-notice", sent="2026-11-10"), message("response", sent="2027-01-10")]
    case(root, late)
    findings = found(root, "finding")
    assert any("the extension notice went out on 2026-11-10, after the first deadline (2026-11-05)" in m for m in findings)
    assert any("after the deadline of 2027-01-05" in m for m in findings)


def test_processor_cases_need_a_referral_and_deletions_reach_processors(root):
    case(root, lambda d: None)
    assert any("deletion and correction reach processors" in m for m in found(root, "finding"))
    case2 = new_record(root, "dsr", "forwarded", "Access, district student", "2026-10-05", "Claude")
    data = yamlio.load(case2)
    data.update(request_types=["access"], roles=[{"data": "Customer account", "role": call("school-official")}], regimes=["ferpa"])
    case2.write_text(yamlio.dumps(data), encoding="utf-8")
    assert any("draft the referral to the controller or institution" in m for m in found(root, "finding"))


def test_a_closed_case_shows_retention_and_leaves_the_schedule(root):
    def closed(d):
        d.update(status="Closed", responded="2026-10-25", closed="2026-10-30")
        d["verification"].update(status="verified", by="Support lead", date="2026-10-07")
        d["processors"] = [{"processor": "Zendesk", "instruction": "delete", "sent": "2026-10-26", "confirmed": "2026-10-28"}]
        d["messages"] = [message("response", sent="2026-10-25")]
    path = case(root, closed)
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "responded in 20 days · keep this record until 2028-10-30" in text
    assert "earliest_deadline" not in text
    assert "| 20 |" in (path.parent / "index.md").read_text()


def test_mixed_roles_get_both_checks_and_contract_deadlines_count(root):
    def mixed(d):
        d.update(regimes=["ferpa", "state"], roles=[{"data": "District-rostered student account", "role": call("school-official")},
                                                   {"data": "Family account the parent created", "role": call("controller")}],
                 contract_deadlines=[{"due": "2026-10-12", "step": "Refer the request to the district", "basis": "DPA section 7.2"}])
    path = case(root, mixed)
    findings = found(root, "finding")
    assert any("draft the referral" in m for m in findings)
    assert any("deletion and correction reach processors" in m for m in findings)
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "**Earliest deadline: 2026-10-12** (contract: Refer the request to the district (DPA section 7.2))" in text
    assert "Institution responds (45 days from its own receipt" in text
