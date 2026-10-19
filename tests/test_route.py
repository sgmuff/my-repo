import pytest
from conftest import FIXTURES, REPO, golden

from gov import route as routing
from gov import yamlio

SCENARIOS = sorted((FIXTURES / "route").glob("*.facts.yaml"))
PLANNED = {"ai-act-provider", "ai-act-deployer"}  # in the plan, not built yet


@pytest.mark.parametrize("facts_file", SCENARIOS, ids=lambda p: p.name.split(".")[0])
def test_route_golden(facts_file):
    facts = yamlio.load(facts_file) or {}
    result = routing.route(REPO, facts)
    stem = facts_file.name.replace(".facts.yaml", "")
    golden(facts_file.with_name(f"{stem}.plan.yaml"), yamlio.dumps(result))
    golden(facts_file.with_name(f"{stem}.plan.md"), routing.to_markdown(result))


@pytest.mark.parametrize("facts_file", SCENARIOS, ids=lambda p: p.name.split(".")[0])
def test_route_is_deterministic(facts_file):
    facts = yamlio.load(facts_file) or {}
    assert routing.route(REPO, facts) == routing.route(REPO, dict(facts))


def test_time_critical_steps_come_first():
    result = routing.route(REPO, yamlio.load(FIXTURES / "route" / "suspected-breach.facts.yaml"))
    steps = [p["step"] for p in result["plan"]]
    assert steps[:2] == ["containment", "incident-assessment"]


def test_start_after_points_backward():
    result = routing.route(REPO, yamlio.load(FIXTURES / "route" / "lead-scoring.facts.yaml"))
    for p in result["plan"]:
        if p["start"] != "now":
            assert all(int(n) < p["n"] for n in p["start"][len("after "):].split(", "))


def test_dpia_screening_runs_for_all_new_processing_and_reports_indicators():
    result = routing.route(REPO, {"new_processing": True, "children_or_students": True})
    dpia = next(p for p in result["plan"] if p["step"] == "dpia-screening")
    assert dpia["status"] == "required" and dpia["start"] == "now"
    assert dpia["indicators"] == ["children_or_students"]
    assert dpia["gate"] == "policy"


def test_ropa_can_start_before_the_assessments_finish():
    result = routing.route(REPO, yamlio.load(FIXTURES / "route" / "lead-scoring.facts.yaml"))
    ropa = next(p for p in result["plan"] if p["step"] == "ropa")
    assert ropa["start"] == "now" and ropa["finalize_after"]


def test_legal_checks_enter_the_decision_register():
    result = routing.route(REPO, yamlio.load(FIXTURES / "route" / "lead-scoring.facts.yaml"))
    required = {d["about"] for d in result["decisions"] if d["status"] == "required"}
    assert {"indirect-notice", "direct-marketing", "lawful-basis"} <= required


def test_unknown_role_is_a_decision():
    result = routing.route(REPO, {"new_processing": True})
    assert any(d["about"] == "our-role" and d["status"] == "required" for d in result["decisions"])


def test_coppa_only_with_children():
    no_children = routing.route(REPO, {"children_or_students": False})
    assert not any(d["about"] == "coppa" for d in no_children["decisions"])
    under_13 = routing.route(REPO, {"children_or_students": True, "children_under_13": True})
    assert any(d["about"] == "coppa" and d["status"] == "required" for d in under_13["decisions"])


def test_missing_skill_blocks_launch_with_a_note():
    result = routing.route(REPO, {"ai_involved": True, "ai_act_role": "deployer", "ai_high_risk": True})
    n = next(p["n"] for p in result["plan"] if p["step"] == "ai-act-deployer")
    step = next(d for d in result["decisions"] if d["about"] == f"step {n}")
    assert step["blocks_launch"] and step["note"].startswith("No skill yet")


def test_next_questions_skip_unaskable_facts():
    result = routing.route(REPO, {})
    asked = [q["fact"] for q in result["next_questions"]]
    assert len(asked) == 3 and "lawful_basis" not in asked and "ai_high_risk" not in asked


def test_provider_and_deployer_duties_route_separately():
    provider = routing.route(REPO, {"ai_act_role": "provider", "ai_high_risk": True, "ai_involved": True})
    steps = [p["step"] for p in provider["plan"]]
    assert "ai-act-provider" in steps and "ai-act-deployer" not in steps


def test_every_step_skill_exists_or_is_planned():
    for step in routing.table()["steps"]:
        skill = step["skill"]
        if skill and skill not in PLANNED:
            assert (REPO / "skills" / skill / "SKILL.md").is_file(), skill


def test_planned_skills_are_marked_not_built():
    result = routing.route(REPO, {"ai_involved": True, "ai_act_role": "deployer", "ai_high_risk": True})
    assert "ai-act-deployer" in result["not_built"]


def test_unknown_fact_and_bad_value():
    with pytest.raises(routing.RoutingError):
        routing.route(REPO, {"vendor": True})
    with pytest.raises(routing.RoutingError):
        routing.route(REPO, {"vendor_involved": "maybe"})
    with pytest.raises(routing.RoutingError):
        routing.route(REPO, {"lawful_basis": "vibes"})


def test_table_rejects_a_dependency_listed_later():
    bad = {"facts": {"x": {"type": "boolean", "question": "?"}},
           "steps": [{"id": "a", "gate": "law", "when": {"x": True}, "start_after": ["b"], "decision": {}},
                     {"id": "b", "gate": "law", "when": {"x": True}, "decision": {}}]}
    with pytest.raises(routing.RoutingError):
        routing.check_table(bad)


def test_child_questions_wait_for_their_parent():
    asked = [q["fact"] for q in routing.route(REPO, {})["next_questions"]]
    assert "ai_act_role" not in asked and "children_under_13" not in asked
    candidates = [q["fact"] for q in routing.route(REPO, {"ai_involved": True, "new_processing": True})["question_candidates"]]
    assert "ai_influences_decisions" in candidates and "ai_act_role" in candidates


def test_new_checks_fire_on_their_facts():
    facts = {"vendor_involved": True, "vendor_own_use": True, "indirect_collection": True, "scraped_data": True,
             "tracking_tech": True, "session_replay": True, "children_or_students": True, "school_context": True}
    required = {d["about"] for d in routing.route(REPO, facts)["decisions"] if d["status"] == "required"}
    assert {"vendor-own-use", "scraped-source", "session-replay", "student-privacy"} <= required


def test_dpia_step_reads_as_screening():
    plan = routing.route(REPO, {"new_processing": True})["plan"]
    assert next(p for p in plan if p["skill"] == "dpia")["label"] == "DPIA screening"


def test_children_of_a_no_parent_are_no():
    plan = routing.route(REPO, {"ai_involved": False, "new_processing": True})["plan"]
    assert not any(p["step"].startswith(("ai-", "ai_")) for p in plan)


def test_children_questions_rank_when_students_are_involved():
    asked = [q["fact"] for q in routing.route(REPO, yamlio.load(FIXTURES / "route" / "ai-note-taker.facts.yaml"))["next_questions"]]
    assert "children_under_13" in asked or "school_context" in asked


def test_lia_runs_only_when_legitimate_interests_is_proposed():
    assert not any(p["step"] == "lia" for p in routing.route(REPO, {"new_processing": True})["plan"])
    assert any(p["step"] == "lia" for p in routing.route(REPO, {"lawful_basis": "legitimate-interests"})["plan"])


def test_conditional_steps_dont_hold_up_finalizing():
    result = routing.route(REPO, {"new_processing": True, "vendor_involved": True})
    number = {p["step"]: p["n"] for p in result["plan"]}
    ropa = next(p for p in result["plan"] if p["step"] == "ropa")
    assert number["transfer-screening"] not in ropa["finalize_after"]


def test_every_register_item_names_its_gate():
    result = routing.route(REPO, yamlio.load(FIXTURES / "route" / "session-replay.facts.yaml"))
    assert all(d["gate"] in routing.GATES for d in result["decisions"])
    assert any(d["about"] == "us-sale-sharing" and d["status"] == "required" for d in result["decisions"])


def test_ai_act_baseline_applies_to_any_ai():
    result = routing.route(REPO, {"ai_involved": True})
    assert any(d["about"] == "ai-act-baseline" and d["status"] == "required" for d in result["decisions"])
