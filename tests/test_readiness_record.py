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
