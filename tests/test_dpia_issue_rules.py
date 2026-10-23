from gov import issues, yamlio
from gov.skeleton import new_record
from gov.validate import validate_tree


def test_dpia_rules_trigger_on_the_record_facts(root):
    path = new_record(root, "dpia", "wearables", "Wearables pricing", "2026-10-22", "Claude")
    data = yamlio.load(path)
    data["processing"]["special_category"] = {"value": True, "status": "Provisional", "reason": "Health data"}
    data["context"] = ["employees", "ai-system"]
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    triggered = {i for i, _ in issues.triggered(data)}
    assert {"dpia-art9-condition", "dpia-workplace-monitoring", "dpia-ai-act"} <= triggered
    assert "dpia-eprivacy" not in triggered
    assert any("(dpia-art9-condition)" in p.message for p in validate_tree(root) if p.level == "finding")
    data["kind"] = "us-assessment"
    assert "dpia-art9-condition" not in {i for i, _ in issues.triggered(data)}


def test_screening_rules_trigger(root):
    path = new_record(root, "scr", "proctoring", "Remote proctoring", "2026-10-22", "Claude")
    data = yamlio.load(path)
    data["context"] = ["children", "monitoring"]
    assert {"scr-vulnerable-people", "scr-monitoring"} <= {i for i, _ in issues.triggered(data)}


def test_every_issue_id_can_be_recorded(root):
    import re
    from gov.records import schema
    pattern = schema("common")["$defs"]["issues"]["items"]["properties"]["issue"]["pattern"]
    assert all(re.fullmatch(pattern, i) for i in issues.rules()["issues"])
