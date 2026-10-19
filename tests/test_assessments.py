from conftest import FIXTURES, golden

from gov import yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree

LIA = "compliance/assessments/lia/LIA-2026-001-lead-scoring.yaml"
TIA = "compliance/assessments/tia/TIA-2026-001-crm-vendor-us.yaml"


def edit(root, rel, change):
    path = root / rel
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def test_fixtures_are_valid(assess_root):
    assert found(assess_root, "error") == []
    assert found(assess_root, "finding") == [
        "objection/notice: the notice doesn't name the interest (Art. 13(1)(d), 14(2)(b)); recommend a notice update"
    ]


def test_goldens(assess_root):
    assert render_tree(assess_root).problems == []
    for kind, stem in (("lia", "LIA-2026-001-lead-scoring"), ("tia", "TIA-2026-001-crm-vendor-us")):
        folder = assess_root / "compliance" / "assessments" / kind
        golden(FIXTURES / kind / f"{stem}.expected.md", (folder / f"{stem}.md").read_text())
        golden(FIXTURES / kind / "index.expected.md", (folder / "index.md").read_text())


def test_skeletons_are_valid(root):
    for kind in ("lia", "tia"):
        new_record(root, kind, "blank", "Blank", "2026-10-18", "Claude")
    assert found(root, "error") == []
    assert render_tree(root).problems == []


def test_lia_kind_decides_the_sections(assess_root):
    edit(assess_root, LIA, lambda d: d.update(kind="compatibility"))
    errors = found(assess_root, "error")
    assert any("compatibility: a compatibility assessment must fill in this section" in m for m in errors)
    assert any("purpose_test: a compatibility assessment must set applicable: false" in m for m in errors)


def test_recognized_interest_is_uk_only(assess_root):
    def change(d):
        d["kind"] = "recognized-interest"
        for key in ("purpose_test", "necessity_test", "balancing"):
            d[key] = {"applicable": False}
        d["recognized_interest"] = {"applicable": True, "annex1_purpose": "Safeguarding vulnerable individuals",
                                    "conditions_met": {"value": "TBC", "status": "Provisional", "reason": "Not yet assessed"},
                                    "commenced": {"value": "TBC", "status": "Provisional", "reason": "Check gdpr.md section 1"}}
    edit(assess_root, LIA, change)
    assert any("exist only under the UK GDPR" in m for m in found(assess_root, "error"))


def test_holds_with_an_open_test_is_a_finding(assess_root):
    edit(assess_root, LIA, lambda d: d["decision"].update(value="holds"))
    findings = found(assess_root, "finding")
    assert any("necessity test isn't met" in m for m in findings)
    assert any("the balance doesn't favor it" in m for m in findings)


def test_direct_marketing_objection_must_be_absolute(assess_root):
    edit(assess_root, LIA, lambda d: d["objection"].update(how="Email us"))
    assert any("Art. 21(3)" in m for m in found(assess_root, "finding"))


def test_special_category_in_an_lia(assess_root):
    edit(assess_root, LIA, lambda d: d["special_category"].update(value=True))
    assert any("never supplies an Art. 9 condition" in m for m in found(assess_root, "finding"))


def test_tia_tool_must_fit_the_kind(assess_root):
    edit(assess_root, TIA, lambda d: d.update(kind="uk-tra"))
    assert any("sccs doesn't fit a uk-tra" in m for m in found(assess_root, "error"))


def test_tia_proceed_without_effective_measures(assess_root):
    edit(assess_root, TIA, lambda d: d["decision"].update(value="proceed"))
    findings = found(assess_root, "finding")
    assert any("no measure is shown to work" in m for m in findings)
    assert any("isn't signed" in m for m in findings)


def test_tia_adequacy_must_be_checked(assess_root):
    edit(assess_root, TIA, lambda d: d["mechanism"]["adequacy_checked"].update(value="TBC"))
    assert any("check adequacy and any DPF certification first" in m for m in found(assess_root, "finding"))


def test_ropa_can_cite_an_lia_on_file(assess_root):
    edit(assess_root, "compliance/registers/ropa/ROPA-0001-gradebook-sync.yaml",
         lambda d: d["assessments"].append({"assessment": "lia", "status": "on-file", "record": "LIA-2026-001"}))
    assert found(assess_root, "error") == []
    edit(assess_root, "compliance/registers/ropa/ROPA-0001-gradebook-sync.yaml",
         lambda d: d["assessments"].append({"assessment": "tia", "status": "on-file", "record": "TIA-2026-009"}))
    assert any("refers to TIA-2026-009, which doesn't exist" in m for m in found(assess_root, "error"))


def test_only_a_person_answers_a_finding(assess_root):
    edit(assess_root, TIA, lambda d: d["finding_responses"].append({"pointer": "activity", "response": "No RoPA yet", "by": "Claude (privacy-governance suite)"}))
    assert any("only a person answers a finding" in m for m in found(assess_root, "error"))


def rendered(root, rel):
    render_tree(root)
    return (root / rel).with_suffix(".md").read_text()


def test_findings_render_open_and_answered(assess_root):
    assert "| objection/notice | the notice doesn't name the interest" in rendered(assess_root, LIA)
    edit(assess_root, LIA, lambda d: d["finding_responses"].append(
        {"pointer": "objection/notice", "response": "Notice update scheduled in A3", "by": "Pat Lee, privacy lead"}))
    assert "| Notice update scheduled in A3 | Pat Lee, privacy lead |" in rendered(assess_root, LIA)


def test_failed_tests_show_as_failed_not_open(assess_root):
    def fail(d):
        d["necessity_test"]["necessary"] = {"value": False, "status": "Provisional", "reason": "Less intrusive options exist"}
        d["balancing"]["outcome"] = {"value": "rights-prevail", "status": "Provisional", "reason": "Intrusive"}
    edit(assess_root, LIA, fail)
    assert "**Tests:** Purpose Yes · Necessity No · Balancing Rights prevail\n" in rendered(assess_root, LIA)


def test_law_block_needs_a_provision(assess_root):
    def uncited(d):
        d["actions"][0].pop("scope")
    edit(assess_root, LIA, uncited)
    assert any("block_reason law needs scope" in m for m in found(assess_root, "error"))
    edit(assess_root, LIA, lambda d: d["actions"][0].update(scope="internal policy"))
    assert any("block_reason law needs scope" in m for m in found(assess_root, "error"))
    edit(assess_root, LIA, lambda d: d["actions"][0].update(scope="GDPR Art. 14(3)"))
    assert not any("block_reason law" in m for m in found(assess_root, "error"))


def test_missing_notice_action_is_a_finding(assess_root):
    edit(assess_root, LIA, lambda d: d["actions"][0].update(block_reason="policy", scope="notice"))
    assert any("add a launch-blocking law action for it" in m for m in found(assess_root, "finding"))


def test_special_category_needs_an_art9_action(assess_root):
    edit(assess_root, LIA, lambda d: d.update(special_category={"value": True, "status": "Provisional", "reason": "Health data"}))
    assert any("no action addresses the Art. 9 condition" in m for m in found(assess_root, "finding"))


def test_unsigned_tool_needs_a_law_action(assess_root):
    edit(assess_root, TIA, lambda d: d["actions"][0].update(scope="GDPR Art. 28(3)"))
    assert any("isn't confirmed signed" in m for m in found(assess_root, "finding"))


def test_every_kind_has_a_method():
    from gov.paths import PACKAGE
    methods = yamlio.load(PACKAGE / "rules" / "methods.yaml")
    for kind in ("lia", "tia"):
        kinds = yamlio.load(PACKAGE / "schemas" / f"{kind}.schema.yaml")["properties"]["kind"]["enum"]
        assert set(kinds) == set(methods[kind]), kind
