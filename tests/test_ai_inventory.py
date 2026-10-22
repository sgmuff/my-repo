from gov import yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def call(value, reason="Test"):
    return {"value": value, "status": "Provisional", "reason": reason}


def entry(root, change):
    path = new_record(root, "ais", "hiring-screener", "Resume screener", "2026-10-22", "Claude")
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def tier1(d):
    d.update(source="vendor-product", lifecycle="pilot", personal_data="personal", tier=call("1"))
    d["tiering"][1].update(level="1", fact="Ranks job applicants for interviews")
    d["ai_act"].update(category=call("high-risk"), annex_point="Annex III point 4(a)", company_role=call("deployer"))


def test_the_skeleton_validates_and_renders(root):
    path = entry(root, lambda d: None)
    assert found(root, "error") == []
    render_tree(root)
    assert "# AIS-0001: Resume screener" in path.with_suffix(".md").read_text()
    assert "| AIS-0001 | [Resume screener]" in (path.parent / "index.md").read_text()


def test_the_tier_cannot_sit_below_a_factor(root):
    entry(root, lambda d: (d.update(tier=call("3")), d["tiering"][0].update(level="1", fact="Annex III use")))
    assert any("a factor is at 1, so the tier can't be 3" in m for m in found(root, "finding"))


def test_tier_1_lists_its_follow_ons_and_review_period(root):
    entry(root, tier1)
    findings = found(root, "finding")
    assert any("ai-impact-assessment, dpia-screening, vendor-review, ai-act-deployer" in m for m in findings)
    assert any("Tier 1 entries are reviewed at least every 6 months" in m for m in findings)
    assert any("name at least three risks" in m for m in findings)


def test_a_possible_prohibited_practice_is_a_stop(root):
    def stop(d):
        d.update(lifecycle="live")
        d["ai_act"]["prohibited"] = call(True, "May infer emotions from voice at work")
    entry(root, stop)
    findings = found(root, "finding")
    assert any("that makes it Tier 0" in m for m in findings)


def test_tier_0_in_use_needs_containment_that_reaches_downstream(root):
    def stop(d):
        d.update(lifecycle="live", tier=call("0"), decision=call("stop"))
        d["containment"] = [{"control": "Emotion score switched off", "owner": "IT, approved by privacy lead",
                             "applied": "2026-10-22 10:00 ET", "evidence": "Admin console screenshot", "downstream_stopped": "TBC",
                             "remaining_paths": "Exports from before today", "reenable_when": "Counsel decides"}]
    entry(root, stop)
    findings = found(root, "finding")
    assert any("no longer generated, shown, exported, or used downstream" in m for m in findings)
    assert not any("record the control that stops it" in m for m in findings)


def test_a_done_follow_on_needs_its_record(root):
    entry(root, lambda d: d.update(follow_ons=[{"follow_on": "vendor-review", "why": "Third-party tool", "status": "done", "record": "none"}]))
    assert any("vendor-review is done; link its record" in m for m in found(root, "finding"))
