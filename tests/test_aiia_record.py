from gov import yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def call(value):
    return {"value": value, "status": "Provisional", "reason": "Test"}


def risk(n):
    level = {"likelihood": "possible", "severity": "significant"}
    return {"id": f"R{n}", "risk": "Candidates from some groups ranked lower", "inherent": level, "current": level, "target": level,
            "measures": [], "owner": "HR lead"}


FRIA = {"applicable": True, "deployer_status": "public-body", "processes": "Ranks housing applications for review",
        "period": "Daily, from March 2028", "people": "Applicants, including people with disabilities",
        "rights_risks": [{"right": "Non-discrimination", "risk": "Lower priority for some groups", "who": "Applicants", "risk_id": "R1"}],
        "oversight": "Caseworkers review every ranking", "remedies": "Complaint route and re-review", "dpia_overlap": "Risks R1-R3 in the DPIA",
        "notification": "drafted"}


def assessment(root, change):
    path = new_record(root, "aiia", "talentrank", "TalentRank hiring screen", "2026-10-22", "Claude")
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def test_a_blank_assessment_validates_and_renders(root):
    path = assessment(root, lambda d: None)
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "| Fairness and non-discrimination | TBC |" in text and (root / "compliance/assessments/ai-impact/index.md").is_file()


def test_an_assessment_has_all_nine_domains(root):
    assessment(root, lambda d: d.update(domains=d["domains"][:5]))
    assert any("one row for each of the nine domains" in m for m in found(root, "error"))


def test_a_possible_prohibition_blocks_going_ahead(root):
    assessment(root, lambda d: d.update(decision=call("proceed-with-conditions"), risks=[risk(1)]))
    assert any("possible Art. 5 prohibited practice isn't ruled out" in m for m in found(root, "finding"))


def test_a_fria_needs_art27_content_and_linked_risks(root):
    def fria(d):
        d.update(kind="fria", domains=[], fria={"applicable": True})
    assessment(root, fria)
    assert any("fria: set applicable: true and fill in deployer_status" in m for m in found(root, "error"))


def test_a_complete_fria_checks_its_risk_links_and_notification(root):
    def fria(d):
        bad = dict(FRIA, notification="TBC", rights_risks=[dict(FRIA["rights_risks"][0], risk_id="R9")])
        d.update(kind="fria", domains=[], fria=bad, risks=[risk(1)], decision=call("proceed-with-conditions"))
        d["ai_act"]["prohibited"] = call(False)
    path = assessment(root, fria)
    assert found(root, "error") == []
    findings = found(root, "finding")
    assert any("risk row R9 doesn't exist" in m for m in findings)
    assert any("notifies the market surveillance authority" in m for m in findings)
    assert any("link the AI impact assessment the FRIA draws on" in m for m in findings)
    render_tree(root)
    assert "| (a) Processes | Ranks housing applications for review |" in path.with_suffix(".md").read_text()


def test_an_input_pack_renders_as_a_draft_for_customers(root):
    def pack(d):
        d.update(kind="fria-input-pack", domains=[], fria=dict(FRIA, deployer_status="TBC", notification="not-required"), risks=[risk(1)])
    path = assessment(root, pack)
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "DRAFT: not sent." in text and "the deployer's determination" in text
