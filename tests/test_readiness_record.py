from gov import aiuc, yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def row(req, applicability="in-scope", gap="none", controls=("CTL-0001",)):
    return {"requirement": req, "applicability": applicability, "rationale": "Applies to the support agent", "responsible": "company",
            "controls": list(controls), "evidence": [], "gap": gap}


def report(root, change):
    path = new_record(root, "rdy", "support-agent", "Support agent readiness", "2026-10-22", "Claude")
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def complete_soa(root, capabilities):
    return [row(i) for i in aiuc.triggered(aiuc.requirements(root), capabilities)]


def test_the_parser_reads_every_requirement(root):
    reqs = aiuc.requirements(root)
    assert len(reqs) == 50 and reqs["A008"]["tags"] == ["Code-generation"]
    assert "A008" not in aiuc.triggered(reqs, []) and "A008" in aiuc.triggered(reqs, ["Code-generation"])


def test_missing_mandatory_requirements_are_listed(root):
    report(root, lambda d: d.update(capabilities=["Text-generation"], soa=[row("A001")]))
    assert any("these mandatory requirements apply to the agent's capabilities and need a row: A002" in m for m in found(root, "finding"))


def test_a_complete_soa_renders_with_titles(root):
    def complete(d):
        d.update(capabilities=["Text-generation"], release="October 15, 2026", system="TBC")
        d["soa"] = complete_soa(root, d["capabilities"])
        for t in d["testing"]:
            t.update(next_due="2027-01-15", control="CTL-0002")
    for slug in ("access-review", "third-party-tests"):
        new_record(root, "ctl", slug, slug.replace("-", " ").capitalize(), "2026-10-22", "Claude")
    path = report(root, complete)
    assert found(root, "error") == []
    assert not any("need a row" in m or "third-party testing" in m for m in found(root, "finding"))
    render_tree(root)
    assert "| A001 | Establish input data policy | In scope |" in path.with_suffix(".md").read_text()


def test_unknown_or_retired_ids_are_errors(root):
    report(root, lambda d: d.update(soa=[row("C011")]))
    assert any("C011 isn't a requirement in the release" in m for m in found(root, "error"))


def test_excluding_a_requirement_the_agent_triggers_is_a_finding(root):
    report(root, lambda d: d.update(capabilities=["Code-generation"], soa=[row("A008", applicability="excluded")]))
    assert any("A008 is mandatory and tagged Code-generation" in m for m in found(root, "finding"))


def test_ready_with_gaps_and_untested_duties_are_findings(root):
    def gaps(d):
        d["soa"] = [row("A009", gap="partial"), row("A001", controls=())]
        d["decision"] = {"value": "ready", "status": "Provisional", "reason": "Test"}
    report(root, gaps)
    findings = found(root, "finding")
    assert any("says ready, but these requirements have gaps" in m and "A009" in m for m in findings)
    assert any("no control carries these in-scope requirements: A001" in m for m in findings)
    assert any("A009 needs third-party testing at least every 3 months" in m for m in findings)


def test_a_missing_gap_with_an_open_action_clears_the_no_control_finding(root):
    def gap(d):
        d["soa"] = [row("A001", gap="missing", controls=()), row("A002", gap="missing", controls=())]
        d["actions"] = [{"id": "A1", "action": "Write the input data policy (A001)", "owner": "Privacy lead", "due": "2026-12-01",
                         "closure_evidence": "Policy approved", "launch_blocking": False, "status": "open"}]
    report(root, gap)
    msg = next(m for m in found(root, "finding") if "no control carries" in m)
    assert "A002" in msg and "A001" not in msg.split(":")[2]


def test_undecided_is_only_for_optional_requirements(root):
    report(root, lambda d: d.update(capabilities=["Text-generation"], soa=[row("A001", applicability="undecided")]))
    assert any("A001 is mandatory for this agent" in m for m in found(root, "error"))


def test_the_schedule_lists_record_actions_and_testing(root):
    from gov.cli import main
    def dated(d):
        d["actions"] = [{"id": "A1", "action": "Fix the refund cap", "owner": "Engineering", "due": "2026-11-20",
                         "closure_evidence": "Test passes", "launch_blocking": False, "status": "open"}]
        d["testing"][0].update(next_due="2027-01-15", last_done="never")
    report(root, dated)
    out = root / "compliance"
    assert main(["--root", str(root), "schedule", str(out), "--as-of", "2026-11-01"]) == 0
    text = (out / "schedule.md").read_text()
    assert "| 2026-11-20 | Due soon | RDY-2026-001 | rdy | action A1 | Fix the refund cap |" in text
    assert "| 2027-01-15 |  | RDY-2026-001 | rdy | next test |" in text
