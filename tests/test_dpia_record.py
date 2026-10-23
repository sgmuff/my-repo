from gov import risk, yamlio
from gov.derive import dpia as derive
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def call(value, status="Provisional"):
    return {"value": value, "status": status, "reason": "Test"}


def level(likelihood, severity):
    return {"likelihood": likelihood, "severity": severity}


def a_risk(n, inherent, current, target, *statuses):
    return {"id": f"R{n}", "risk": f"Risk {n}", "inherent": level(*inherent), "current": level(*current), "target": level(*target),
            "measures": [{"measure": f"Measure {n}{i}", "status": s, "evidence": "A1"} for i, s in enumerate(statuses)], "owner": "SRE lead"}


LOW = ("remote", "minimal")
MEDIUM = ("possible", "significant")
HIGH = ("probable", "severe")


def four_low_risks():
    return [a_risk(n, LOW, LOW, LOW, "verified") for n in range(1, 5)]


def dpia(root, change):
    path = new_record(root, "dpia", "session-replay", "Session replay on the dashboard", "2026-10-21", "Claude")
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def test_the_matrix_matches_risk_method():
    assert risk.rate(level("probable", "significant")) == "High"
    assert risk.rate(level("possible", "minimal")) == "Low"
    assert risk.rate(level("remote", "severe")) == "Medium"
    assert risk.rate(level("TBC", "severe")) == "TBC"


def test_overall_is_the_highest_never_an_average():
    risks = [a_risk(n, LOW, LOW, LOW) for n in range(1, 10)] + [a_risk(10, HIGH, HIGH, LOW, "planned")]
    assert risk.overall(risks, "current") == "High"
    assert risk.overall(risks, "target") == "Low"


def test_a_blank_dpia_validates_and_renders(root):
    path = dpia(root, lambda d: None)
    assert found(root, "error") == []
    assert render_tree(root).problems == []
    text = path.with_suffix(".md").read_text()
    assert "**Residual risk:** not yet confirmed." in text
    assert "Not yet known (the current rating is TBC)" in text
    assert (root / "compliance/assessments/dpia/index.md").is_file()


def test_ratings_are_computed_and_the_approver_follows_the_current_rating(root):
    def medium(d):
        d["risks"] = four_low_risks() + [a_risk(5, HIGH, MEDIUM, LOW, "verified", "planned")]
    path = dpia(root, medium)
    data = yamlio.load(path)
    out = derive(data)
    assert (out["inherent"], out["current"], out["target"]) == ("High", "Medium", "Low")
    assert out["approver"] == "Privacy lead and business owner" and not out["confirmed"]
    render_tree(root)
    assert "| R5 | Risk 5 | High | Measure 50 (verified); Measure 51 (planned) | Medium | Low | SRE lead |" in path.with_suffix(".md").read_text()


def test_a_current_rating_lowered_by_unverified_measures_is_a_finding(root):
    dpia(root, lambda d: d.update(risks=four_low_risks() + [a_risk(5, HIGH, MEDIUM, MEDIUM, "planned")]))
    assert any("R5: the current rating is below the inherent one, but no measure is verified" in m for m in found(root, "finding"))


def test_a_target_with_no_planned_measure_is_a_finding(root):
    dpia(root, lambda d: d.update(risks=four_low_risks() + [a_risk(5, MEDIUM, MEDIUM, LOW, "absent")]))
    assert any("R5: the target rating is below the current one, but no measure is planned" in m for m in found(root, "finding"))


def test_a_high_current_needs_prior_consultation_and_blocks_proceeding(root):
    def high(d):
        d["risks"] = four_low_risks() + [a_risk(5, HIGH, HIGH, MEDIUM, "planned")]
        d["consultation"]["prior_consultation"] = call("TBC")
        d["decision"] = call("proceed-with-conditions")
    path = dpia(root, high)
    findings = found(root, "finding")
    assert any("decide Art. 36 on its test" in m for m in findings)
    assert any("while the current residual rating is High" in m for m in findings)
    # A reasoned no settles the Art. 36 question; the proceed decision still needs its reasons.
    data = yamlio.load(path)
    data["consultation"]["prior_consultation"] = call(False)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    findings = found(root, "finding")
    assert not any("decide Art. 36 on its test" in m for m in findings)
    assert any("while the current residual rating is High" in m for m in findings)


def test_a_confirmed_decision_needs_confirmed_residual_risk(root):
    def confirmed(d):
        d["risks"] = four_low_risks() + [a_risk(5, MEDIUM, MEDIUM, LOW, "planned")]
        d["decision"] = call("proceed-with-conditions", "Confirmed")
    dpia(root, confirmed)
    assert any("confirmed while residual risk isn't" in m for m in found(root, "finding"))


def test_legitimate_interests_needs_a_linked_lia(root):
    def li(d):
        d["necessity"][0].update(position="adequate", basis="Art. 6(1)(f) legitimate interests in fraud prevention", link="none")
    dpia(root, li)
    assert any("link the LIA, or add an action to run lia" in m for m in found(root, "finding"))
    dpia_path = next((root / "compliance/assessments/dpia").glob("DPIA-*.yaml"))
    data = yamlio.load(dpia_path)
    data["necessity"][0]["link"] = "LIA-2026-001"
    dpia_path.write_text(yamlio.dumps(data), encoding="utf-8")
    assert not any("link the LIA" in m for m in found(root, "finding"))


def test_special_category_needs_an_art9_condition(root):
    dpia(root, lambda d: d["processing"].update(special_category=call(True)))
    assert any("add an art9-condition row" in m for m in found(root, "finding"))


def test_too_few_risks_is_a_finding(root):
    dpia(root, lambda d: d.update(risks=[a_risk(1, LOW, LOW, LOW)]))
    assert any("1 risk recorded" in m for m in found(root, "finding"))


def test_a_us_assessment_raises_no_gdpr_findings(root):
    def us(d):
        d["kind"] = "us-assessment"
        d["risks"] = four_low_risks() + [a_risk(5, HIGH, HIGH, MEDIUM, "planned")]
        d["processing"]["special_category"] = call(True)
        d["other_regimes"] = [{"regime": "state-student-privacy", "applies": call(True), "elements": "SOPIPA, NY Educ. Law 2-d"}]
    path = dpia(root, us)
    findings = found(root, "finding")
    assert not any("Art. 36 on its test" in m or "Art. 9(2)" in m for m in findings)
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "GDPR Art. 35 doesn't apply" in text and "State student privacy laws" in text


def test_an_art9_gap_says_what_waits(root):
    def gap(d):
        d["processing"]["special_category"] = call(True)
        d["necessity"].append({"principle": "art9-condition", "position": "gap", "basis": "None yet", "gap": "Mask the box", "link": "none"})
    dpia(root, gap)
    findings = found(root, "finding")
    assert any("no Art. 9(2) condition is in place yet" in m for m in findings)
    assert not any("add an art9-condition row" in m for m in findings)


def test_an_open_action_to_create_the_ropa_entry_answers_the_link_finding(root):
    action = {"id": "A1", "action": "Create the RoPA entry with the ropa skill", "owner": "Privacy lead", "due": "TBC",
              "closure_evidence": "ROPA ID linked", "launch_blocking": False, "status": "open"}
    dpia(root, lambda d: d.update(actions=[action]))
    assert not any("link the RoPA entry" in m for m in found(root, "finding"))


def test_gov_required_explains_it_reads_a_ropa(root, monkeypatch, capsys):
    from gov.cli import main
    path = dpia(root, lambda d: None)
    monkeypatch.setenv("GOV_ROOT", str(root))
    assert main(["required", str(path)]) == 2
    assert "reads a RoPA record or a facts file, not a dpia record" in capsys.readouterr().err


def test_the_fact_register_renders(root):
    fact = {"id": "F1", "fact": "About 25,000 people a year contact support", "status": "stated-by-requester", "source": {"kind": "stated", "ref": "Product lead, 2026-10-21"}}
    path = dpia(root, lambda d: d.update(facts=[fact]))
    assert found(root, "error") == []
    render_tree(root)
    assert "| F1 | About 25,000 people a year contact support | Stated by requester |" in path.with_suffix(".md").read_text()
