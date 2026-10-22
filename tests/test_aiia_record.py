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


def test_section_sign_citations_count_as_law(root):
    from gov.validate import PROVISION
    for scope in ("NYC Admin. Code § 20-871", "42 U.S.C. § 12112(b)", "Cal. Civ. Code §§ 1798.100", "GDPR Art. 35(1)"):
        assert PROVISION.search(scope), scope
    assert not PROVISION.search("our internal policy")


def test_an_action_naming_the_inventory_entry_answers_the_system_finding(root):
    action = {"id": "A1", "action": "Create AIS-0001 for TalentRank", "owner": "Privacy lead", "due": "TBC",
              "closure_evidence": "Entry exists", "launch_blocking": False, "status": "open"}
    assessment(root, lambda d: d.update(actions=[action]))
    assert not any("link the AI inventory entry" in m for m in found(root, "finding"))


def test_a_fria_can_cite_the_assessments_risk_rows(root):
    def pair(d):
        d.update(kind="fria", domains=[], fria=dict(FRIA, rights_risks=[dict(FRIA["rights_risks"][0], risk_id="AIIA-2026-001/R1")]))
    assessment(root, pair)
    assert not any("doesn't exist in this record" in m for m in found(root, "finding"))


def test_the_company_role_is_a_call_and_renders_without_a_gdpr_label(root):
    def role(d):
        d["ai_act"]["company_role"] = {"value": "provider-and-deployer", "status": "Provisional", "reason": "Rebranded under Art. 25(1)(a)"}
    path = assessment(root, role)
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "company role Provider and deployer" in text and "Controller and processor" not in text
