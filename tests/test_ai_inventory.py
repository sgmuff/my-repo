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
    d["tiering"][1].update(level="high", fact="Ranks job applicants for interviews")
    d["ai_act"].update(category=call("high-risk"), annex_point="Annex III point 4(a)", company_role=call("deployer"), art50=call(False))


def test_the_skeleton_validates_and_renders(root):
    path = entry(root, lambda d: None)
    assert found(root, "error") == []
    render_tree(root)
    assert "# AIS-0001: Resume screener" in path.with_suffix(".md").read_text()
    assert "| AIS-0001 | [Resume screener]" in (path.parent / "index.md").read_text()


def test_the_tier_cannot_sit_below_a_factor(root):
    entry(root, lambda d: (d.update(tier=call("3")), d["tiering"][0].update(level="high", fact="Annex III use")))
    assert any("a factor sets Tier 1, so the tier can't be 3" in m for m in found(root, "finding"))


def test_tier_1_lists_its_follow_ons_and_review_period(root):
    entry(root, tier1)
    findings = found(root, "finding")
    assert any("ai-impact-assessment, dpia-screening, vendor-review, human-oversight, testing-plan, ai-act-deployer, ropa-update" in m for m in findings)
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
        d["containment"] = [{"control": "Emotion score switched off", "status": "applied", "owner": "IT, approved by privacy lead",
                             "applied": "2026-10-22 10:00 ET", "evidence": "Admin console screenshot", "downstream_stopped": "TBC",
                             "remaining_paths": "Exports from before today", "reenable_when": "Counsel decides"}]
    entry(root, stop)
    findings = found(root, "finding")
    assert any("no longer generated, shown, exported, or used downstream" in m for m in findings)
    assert not any("record the control that stops it" in m for m in findings)


def test_a_done_follow_on_needs_its_record(root):
    entry(root, lambda d: d.update(follow_ons=[{"follow_on": "vendor-review", "why": "Third-party tool", "status": "done", "record": "none"}]))
    assert any("vendor-review is done; link its record" in m for m in found(root, "finding"))


def test_a_requested_containment_needs_an_action(root):
    def requested(d):
        d.update(lifecycle="live")
        d["containment"] = [{"control": "Score off for all users", "status": "requested", "owner": "IT, approved by privacy lead",
                             "applied": "Requested 2026-10-22", "evidence": "TBC", "downstream_stopped": "TBC",
                             "remaining_paths": "Dashboards already shared", "reenable_when": "Counsel decides"}]
    path = entry(root, requested)
    assert any("is requested, not applied; add an action" in m for m in found(root, "finding"))
    data = yamlio.load(path)
    data["actions"] = [{"id": "A1", "action": "Switch off the score for all users", "owner": "IT", "due": "2026-10-23",
                        "closure_evidence": "Admin screenshot", "launch_blocking": True, "block_reason": "law", "scope": "AI Act Art. 5(1)(f)", "status": "open"}]
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    findings = found(root, "finding")
    assert not any("is requested, not applied" in m for m in findings)
    assert not any("downstream" in m for m in findings)
    render_tree(root)
    assert "| Closure evidence | Blocks use | Status |" in path.with_suffix(".md").read_text()


def test_art50_and_tier_0_still_need_their_follow_ons(root):
    def stop(d):
        d.update(source="embedded-feature", personal_data="sensitive", tier=call("0"), decision=call("stop"))
        d["ai_act"]["prohibited"] = call(True)
    entry(root, stop)
    assert any("dpia-screening, vendor-review, art50-check, ropa-update" in m for m in found(root, "finding"))


def test_unlinked_verify_flags_are_findings(root):
    entry(root, lambda d: d.update(verify=[{"id": "V1", "claim": "Vendor doesn't train on inputs", "why": "Decides the vendor terms",
                                             "check": "Current AI terms", "owner": "Counsel", "needed_by": "TBC"}]))
    assert any("V1 has no action" in m for m in found(root, "finding"))
