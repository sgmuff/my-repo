from gov import ids, yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def control(root, change, slug="admin-access-review"):
    path = new_record(root, "ctl", slug, "Quarterly admin access review", "2026-10-22", "Claude")
    data = yamlio.load(path)
    data["objectives"] = [{"cco": "CCO-15", "how": "Removes access no longer needed", "coverage": "full", "not_satisfied": "none"}]
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def evidence(ev, type_="record", shows="operation"):
    return {"id": ev, "type": type_, "shows": shows, "what": "Q3 review ticket", "location": "https://jira/IT-1",
            "date": "2026-10-01", "period": "Q3 2026", "owner": "IT lead", "stale_after": "2027-01-01"}


def test_coverage_renders_from_the_crosswalk(root):
    path = control(root, lambda d: None)
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "| CCO-15: Access control and least privilege" in text
    assert "AIUC-1 A003, A005, B006, B007, D003" in text
    assert "| CTL-0001 | [Quarterly admin access review]" in (path.parent / "index.md").read_text()


def test_unknown_objectives_are_errors(root):
    control(root, lambda d: d["objectives"][0].update(cco="CCO-99"))
    assert any("CCO-99 isn't an objective in crosswalk.md" in m for m in found(root, "error"))


def test_evidence_ids_are_issued_listed_once_and_resolve(root):
    ids.next_id(root, "EV")
    control(root, lambda d: d.update(evidence=[evidence("EV-0001"), evidence("EV-0002")]))
    control(root, lambda d: d.update(evidence=[evidence("EV-0001")], description="See EV-0007"), slug="mfa")
    errors = found(root, "error")
    assert any("EV-0002 is above the counter" in m for m in errors)
    assert any("evidence EV-0001 is also listed in" in m for m in errors)
    assert any("refers to EV-0007, which no control record lists" in m for m in errors)


def test_a_policy_is_not_operating_evidence(root):
    ids.next_id(root, "EV")
    control(root, lambda d: d.update(operating="evidenced", evidence=[evidence("EV-0001", "policy", "operation")]))
    findings = found(root, "finding")
    assert any("a policy shows design" in m for m in findings)


def test_testing_dates_follow_the_frequency_and_failures_need_actions(root):
    def tested(d):
        d.update(frequency="quarterly", operating="unverified", last_tested="2026-09-30", next_test="2027-03-31")
        d["testing"] = [{"date": "2026-09-30", "method": "sample", "scope": "All admin roles", "tested_by": "Internal audit",
                         "result": "exceptions", "exceptions": "Two stale admins"}]
    control(root, tested)
    findings = found(root, "finding")
    assert any("a quarterly control tested on 2026-09-30 is due again by 2026-12-30" in m for m in findings)
    assert any("found exceptions; add an open action" in m for m in findings)


def test_a_readiness_report_must_cite_controls_that_exist(root):
    path = new_record(root, "rdy", "agent", "Agent readiness", "2026-10-22", "Claude")
    data = yamlio.load(path)
    data["soa"] = [{"requirement": "A001", "applicability": "in-scope", "rationale": "Applies", "responsible": "company",
                    "controls": ["CTL-0004"], "evidence": [], "gap": "none"}]
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    assert any("refers to CTL-0004, which doesn't exist" in m for m in found(root, "error"))
