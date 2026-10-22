"""Proposed issue rules awaiting counsel must merge cleanly into gov/rules/issues.yaml."""
import copy

from conftest import REPO
from gov import issues, yamlio
from gov.skeleton import new_record

PROPOSALS = REPO / "docs/legal-review/issue-rules-scr-dpia.yaml"


def merged():
    live = copy.deepcopy(issues.rules())
    proposed = yamlio.load(PROPOSALS)["issues"]
    assert not set(proposed) & set(live["issues"]), "a proposed rule reuses a live rule's ID"
    live["issues"].update(proposed)
    issues.check_rules(live)
    return live


def test_proposals_merge_and_trigger(root, monkeypatch):
    rules = merged()
    monkeypatch.setattr(issues, "rules", lambda: rules)
    path = new_record(root, "dpia", "wearables", "Wearables pricing", "2026-10-22", "Claude")
    data = yamlio.load(path)
    data["processing"]["special_category"] = {"value": True, "status": "Provisional", "reason": "Health data"}
    data["context"] = ["employees", "ai-system"]
    triggered = {i for i, _ in issues.triggered(data)}
    assert {"dpia-art9-condition", "dpia-workplace-monitoring", "dpia-ai-act"} <= triggered
    assert "dpia-eprivacy" not in triggered
