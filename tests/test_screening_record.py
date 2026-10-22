from gov import yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def screening(root, change):
    path = new_record(root, "scr", "session-replay", "Session replay on the dashboard", "2026-10-21", "Claude")
    data = yamlio.load(path)
    data["activity"] = "TBC"
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def call(value):
    return {"value": value, "status": "Provisional", "reason": "Test"}


def set_criteria(present=(), unclear=()):
    return [{"criterion": n, "result": "present" if n in present else "unclear" if n in unclear else "not-present", "facts": "F1"} for n in range(1, 10)]


def test_a_blank_screening_validates_and_renders(root):
    path = screening(root, lambda d: None)
    assert found(root, "error") == []
    assert render_tree(root).problems == []
    text = path.with_suffix(".md").read_text()
    assert "| 9 | Processing that blocks a right, service, or contract | Unclear | TBC |" in text
    assert (root / "compliance/assessments/dpia/screening/index.md").is_file()


def test_each_criterion_must_appear_once(root):
    def dup(d):
        d["criteria"][8]["criterion"] = 1
    screening(root, dup)
    assert any("criterion 1 to 9 exactly once" in m for m in found(root, "error"))


def test_two_present_and_not_indicated_is_a_finding(root):
    def two(d):
        d["criteria"] = set_criteria(present=(3, 7))
        d["decision"] = call("not-indicated")
    screening(root, two)
    assert any("2 criteria are present (3, 7)" in m for m in found(root, "finding"))


def test_an_art35_3_case_requires_warranted(root):
    def always(d):
        d["criteria"] = set_criteria()
        d["art35_3"]["c_public_monitoring"] = call(True)
        d["decision"] = call("recommended")
    screening(root, always)
    assert any("an Art. 35(3) case applies (c_public_monitoring)" in m for m in found(root, "finding"))


def test_not_indicated_with_unclear_criteria_is_a_finding(root):
    def hasty(d):
        d["criteria"] = set_criteria(unclear=(5,))
        d["decision"] = call("not-indicated")
    screening(root, hasty)
    assert any("while some criteria are unclear" in m for m in found(root, "finding"))


def test_a_listed_processing_requires_warranted_and_a_state_assessment_needs_an_action(root):
    def listed(d):
        d["criteria"] = set_criteria(present=(8,))
        d["national_list"] = {"authority": "CNIL", "result": "listed", "item": "Large-scale employee monitoring"}
        d["decision"] = call("recommended")
    screening(root, listed)
    findings = found(root, "finding")
    assert any("Art. 35(4) list" in m for m in findings)
    assert any("US state assessment is or may be owed" in m for m in findings)
