import pytest
from conftest import FIXTURES, REPO
from test_validate import edit, messages

from gov import required as req
from gov import yamlio

CONTROLLER = {"company_role": "controller"}


def statuses(facts, as_of="2026-10-18"):
    return {r["assessment"]: r["status"] for r in req.evaluate(facts, as_of, REPO)}


def test_catalog_loads_and_rejects_unknown_facts():
    assert len(req.catalog()["entries"]) >= 20
    bad = {"facts": {}, "entries": [{"id": "x", "name": "x", "citation": "c", "owed_by": "o", "gate": "law",
                                     "applies_from": "2020-01-01", "produced_by": "dpia", "reference": "gdpr.md",
                                     "when": {"no_such_fact": True}}]}
    with pytest.raises(req.CatalogError):
        req.check_catalog(bad)


def test_lia_is_owed_for_a_controller_relying_on_legitimate_interests():
    assert statuses({**CONTROLLER, "lawful_basis": "legitimate-interests"})["lia"] == "owed"
    assert "lia" not in statuses({**CONTROLLER, "lawful_basis": "contract"})
    assert "lia" not in statuses({"company_role": "processor", "lawful_basis": "legitimate-interests"})


def test_tia_needs_eu_people_a_transfer_and_sccs():
    assert statuses({"eu_people": True, "cross_border_access": True, "transfer_mechanism": "sccs"})["tia"] == "owed"
    assert statuses({"eu_people": True, "cross_border_access": True})["tia"] == "tbc"
    assert "tia" not in statuses({"eu_people": True, "cross_border_access": True, "transfer_mechanism": "eu-us-dpf"})


def test_list_valued_facts_match_any_value():
    assert statuses({**CONTROLLER, "lawful_basis": ["contract", "legitimate-interests"]})["lia"] == "owed"


def test_future_duties_wait_for_their_date():
    facts = {"ai_act_role": "deployer", "ai_high_risk": True}
    assert statuses(facts)["ai-deployer-duties"] == "not-yet-applicable"
    assert statuses(facts, "2027-12-02")["ai-deployer-duties"] == "owed"


def test_entries_wait_for_their_reference_files(root):
    (root / "skills" / "_shared" / "references" / "hipaa.md").unlink()
    result = {r["assessment"]: r["status"] for r in req.evaluate({"phi": True}, "2026-10-18", root)}
    assert result["hipaa-risk-analysis"] == "no-reference"


def test_conditional_regimes_apply_once_their_references_exist():
    assert statuses({"phi": True})["hipaa-risk-analysis"] == "owed"
    assert statuses({"gpai_model": True})["gpai-duties"] == "owed"


def test_dates_come_from_the_caller():
    early = {r["assessment"]: r["status"] for r in req.evaluate({"ai_involved": True}, "2025-01-01", REPO)}
    assert early["ai-prohibited-screening"] == "not-yet-applicable"


def test_facts_from_the_gradebook_entry():
    facts = req.facts_from_ropa(yamlio.load(FIXTURES / "ropa" / "ROPA-0001-gradebook-sync.yaml"))
    assert facts["company_role"] == "processor" and facts["ai_involved"] is True
    assert facts["special_category"] is True and "cross_border_access" not in facts


def test_owed_assessment_is_a_finding_in_draft(ropa_root):
    edit(ropa_root, lambda d: d.update(assessments=[]))
    assert any("owes Security risk assessment" in m for m in messages(ropa_root, "finding"))


def test_owed_assessment_blocks_review(ropa_root):
    def review(d):
        d["status"] = "In review"
        d["assessments"] = []
    edit(ropa_root, review)
    assert any("owes Security risk assessment" in m for m in messages(ropa_root))


def test_open_facts_block_review(ropa_root):
    edit(ropa_root, lambda d: d.update(status="In review"))
    assert any("may owe COPPA written information security program" in m for m in messages(ropa_root))


def test_not_applicable_needs_who_decided(ropa_root):
    edit(ropa_root, lambda d: d["assessments"].append({"assessment": "tia", "status": "not-applicable", "reason": "No EU data"}))
    assert any("by" in m for m in messages(ropa_root))


def test_unknown_assessment_id(ropa_root):
    edit(ropa_root, lambda d: d["assessments"].append({"assessment": "made-up", "status": "planned"}))
    assert any("isn't in the catalog" in m for m in messages(ropa_root))


def test_every_catalog_skill_is_routed_or_known():
    from gov import route as routing
    routed = {s["skill"] for s in routing.table()["steps"]} | {"controls-and-evidence"}
    for e in req.catalog()["entries"]:
        assert e["produced_by"] in routed, e["id"]


def test_every_schema_and_rules_file_parses():
    from gov.paths import PACKAGE
    for path in sorted((PACKAGE / "schemas").glob("*.yaml")) + sorted((PACKAGE / "rules").glob("*.yaml")):
        assert isinstance(yamlio.load(path), dict), path.name
