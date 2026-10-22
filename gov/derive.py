"""Values computed from records, so nobody types a summary that can drift from the facts."""
from __future__ import annotations

import re

TBC = "TBC"


def is_tbc(value) -> bool:
    """TBC, including TBC with an explanation, such as "TBC (entities not named)"."""
    return value == TBC or (isinstance(value, str) and re.match(r"TBC\b", value.strip()) is not None)


SPECIAL = {"special-category", "criminal", "biometric"}
CHILDREN = {"children", "education-record"}


def ropa(data: dict) -> dict:
    rtype = data["record_type"]["value"]
    flags = [c["flags"] for c in data["data_categories"]]
    return {
        "record_type": rtype,
        "is_controller": rtype in ("controller", "both"),
        "is_processor": rtype in ("processor", "both"),
        "lawful_basis_status": _basis_status(data["purposes"]),
        "special_category": _any_flag(flags, SPECIAL),
        "children_or_students": _any_flag(flags, CHILDREN),
        "restricted_transfers": _transfers(data["transfers"]),
        "sale_or_sharing": data["us_flags"]["sale_or_sharing"]["value"],
        "ai_used": data["ai_used"],
        "assessment": data["related"]["assessment"],
        "required_tbc": len(ropa_missing(data)),
        "missing": ropa_missing(data),
        "blocking_questions": sum(1 for q in data["open_questions"] if q["blocks"] in ("launch", "approval")),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
        "blocking_actions": sum(1 for a in data["actions"] if a["launch_blocking"] and a["status"] == "open"),
        "launch_blockers": [a["id"] for a in data["actions"] if a["launch_blocking"] and a["status"] == "open"]
        + [q["id"] for q in data["open_questions"] if q["blocks"] == "launch"],
        "launch_groups": _blocker_groups(data),
    }


def ropa_missing(data: dict) -> list:
    """Art. 30 elements still TBC, each counted once, in the order the article lists them."""
    rtype = data["record_type"]["value"]
    controller = rtype in ("controller", "both", TBC)
    processor = rtype in ("processor", "both")
    missing = []
    company = data["company"]
    if is_tbc(company["name"]) or is_tbc(company["contact"]):
        missing.append("Art. 30(1)(a)/(2)(a): company name and contact")
    if processor:
        pr = data["processor_record"]
        if not pr.get("applicable") or is_tbc(pr.get("controllers")):
            missing.append("Art. 30(2)(a): controllers served")
        if not pr.get("applicable") or is_tbc(pr.get("processing")):
            missing.append("Art. 30(2)(b): categories of processing")
    if controller:
        if any(is_tbc(p["purpose"]) for p in data["purposes"]):
            missing.append("Art. 30(1)(b): purposes")
        if any(is_tbc(s["category"]) for s in data["data_subjects"]):
            missing.append("Art. 30(1)(c): data subjects")
        if any(is_tbc(c["category"]) or is_tbc(c["elements"]) for c in data["data_categories"]):
            missing.append("Art. 30(1)(c): personal data")
        if is_tbc(data["recipients"]):
            missing.append("Art. 30(1)(d): recipients")
    if is_tbc(data["transfers"]):
        missing.append("Art. 30(1)(e)/(2)(c): transfers")
    if controller and any(is_tbc(r["current_practice"]) and is_tbc(r["proposed_policy"]) for r in data["retention"]):
        missing.append("Art. 30(1)(f): time limits for erasure")
    if is_tbc(data["security"]["baseline"]):
        missing.append("Art. 30(1)(g)/(2)(d): security measures")
    return missing


def _basis_status(purposes: list) -> str:
    calls = [p["lawful_basis"] for p in purposes]
    if any(c["value"] == TBC for c in calls):
        return "Open"
    return "Confirmed" if all(c["status"] == "Confirmed" for c in calls) else "Provisional"


def _transfers(value):
    if value == "none":
        return False
    if value == TBC:
        return TBC
    return True


def _any_flag(flags: list, wanted: set):
    if any(f != TBC and wanted & {x["flag"] for x in f} for f in flags):
        return True
    if any(f == TBC for f in flags):
        return TBC
    return False


def vendor_slugs(data: dict) -> list:
    """Vendor folder names: the recipient's vendor field, or a slug of its name for outside processors."""
    recipients = data["recipients"] if isinstance(data["recipients"], list) else []
    slugs = set()
    for r in recipients:
        if r.get("vendor"):
            slugs.add(r["vendor"])
        elif r["kind"] in ("processor", "sub-processor"):
            slug = re.sub(r"[^a-z0-9]+", "-", re.sub(r"\(.*?\)", "", r["name"]).lower()).strip("-")
            if slug:
                slugs.add(slug)
    return sorted(slugs)


BLOCK_GROUPS = ("law", "risk", "policy")


def _blocker_groups(data: dict) -> list:
    """Open launch blockers grouped by why they block: law, risk, policy, then open questions."""
    open_actions = [a for a in data["actions"] if a["launch_blocking"] and a["status"] == "open"]
    groups = [(key, [a["id"] for a in open_actions if a.get("block_reason") == key]) for key in BLOCK_GROUPS]
    groups.append(("open question", [q["id"] for q in data["open_questions"] if q["blocks"] == "launch"]))
    return [(label, ids) for label, ids in groups if ids]


def _blockers(data: dict) -> list:
    return [a["id"] for a in data["actions"] if a["launch_blocking"] and a["status"] == "open"] + [
        q["id"] for q in data["open_questions"] if q["blocks"] == "launch"
    ]


LIA_TESTS = (
    ("Purpose", "purpose_test", "legitimate"),
    ("Necessity", "necessity_test", "necessary"),
    ("Balancing", "balancing", "outcome"),
    ("Annex 1 conditions", "recognized_interest", "conditions_met"),
    ("Compatibility", "compatibility", "outcome"),
)


def lia(data: dict) -> dict:
    tests = [data[k] for k in ("purpose_test", "necessity_test") if data[k].get("applicable")]
    results = [(name, data[key][call]["value"]) for name, key, call in LIA_TESTS if data[key].get("applicable")]
    open_calls = [t for t in tests for key in ("legitimate", "necessary") if key in t and t[key]["value"] == TBC]
    balancing = data["balancing"]
    return {
        "decision": data["decision"]["value"],
        "test_results": results,
        "open_tests": len(open_calls) + (1 if balancing.get("applicable") and balancing["outcome"]["value"] == "open" else 0),
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "blocking_questions": sum(1 for q in data["open_questions"] if q["blocks"] in ("launch", "approval")),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def tia(data: dict) -> dict:
    return {
        "decision": data["decision"]["value"],
        "effective_measures": sum(1 for m in data["measures"] if m["effective"]["value"] is True),
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "blocking_questions": sum(1 for q in data["open_questions"] if q["blocks"] in ("launch", "approval")),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def tsr(data: dict) -> dict:
    return {
        "decision": data["decision"]["value"],
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def ai_act(data: dict) -> dict:
    return {
        "decision": data["decision"]["value"],
        "gaps": sum(1 for o in data["obligations"] if o["status"] in ("gap", "TBC")),
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def scr(data: dict) -> dict:
    from gov.screen import rules
    results = [c["result"] for c in data["criteria"]]
    return {
        "decision": data["decision"]["value"],
        "present": results.count("present"),
        "unclear": results.count("unclear"),
        "criterion_labels": {c["id"]: c["label"] for c in rules()["criteria"]},
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


APPROVER = {"Low": "Privacy lead", "Medium": "Privacy lead and business owner", "High": "Executive risk approver",
            "TBC": "Not yet known (the current rating is TBC)"}


def dpia(data: dict) -> dict:
    from gov import risk
    measures = [m for k in data["risks"] for m in k["measures"]]
    current, target = risk.overall(data["risks"], "current"), risk.overall(data["risks"], "target")
    rows = [{"id": k["id"], "risk": k["risk"], "owner": k["owner"],
             "inherent": risk.rate(k["inherent"]), "current": risk.rate(k["current"]), "target": risk.rate(k["target"]),
             "measures": "; ".join(f"{m['measure']} ({m['status']})" for m in k["measures"]) or "None"}
            for k in data["risks"]]
    return {
        "decision": data["decision"]["value"],
        "inherent": risk.overall(data["risks"], "inherent"),
        "current": current,
        "target": target,
        "confirmed": bool(data["risks"]) and current == target and all(m["status"] == "verified" for m in measures),
        "approver": APPROVER[current],
        "risk_rows": rows,
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def vr(data: dict) -> dict:
    from gov import risk
    rows = data["clauses"] + (data["ai"]["items"] if data["ai"]["applicable"] else [])
    current = risk.overall(data["risks"], "current")
    return {
        "decision": data["decision"]["value"],
        "gaps": sum(1 for r in rows if r["rating"] in ("partial", "missing", "conflicts", "not-provided", "TBC")),
        "inherent": risk.overall(data["risks"], "inherent"),
        "current": current,
        "target": risk.overall(data["risks"], "target"),
        "approver": APPROVER[current],
        "risk_rows": [{"id": k["id"], "risk": k["risk"], "owner": k["owner"], "inherent": risk.rate(k["inherent"]),
                       "current": risk.rate(k["current"]), "target": risk.rate(k["target"]),
                       "measures": "; ".join(f"{m['measure']} ({m['status']})" for m in k["measures"]) or "None"} for k in data["risks"]],
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def aiia(data: dict) -> dict:
    from gov import risk
    current = risk.overall(data["risks"], "current")
    return {
        "decision": data["decision"]["value"],
        "inherent": risk.overall(data["risks"], "inherent"),
        "current": current,
        "target": risk.overall(data["risks"], "target"),
        "approver": APPROVER[current],
        "risk_rows": [{"id": k["id"], "risk": k["risk"], "owner": k["owner"], "inherent": risk.rate(k["inherent"]),
                       "current": risk.rate(k["current"]), "target": risk.rate(k["target"]),
                       "measures": "; ".join(f"{m['measure']} ({m['status']})" for m in k["measures"]) or "None"} for k in data["risks"]],
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


REGIME_NAMES = {"gdpr": "GDPR Arts. 33-34", "uk": "UK GDPR Arts. 33-34", "fadp": "FADP Art. 24", "nydfs": "23 NYCRR 500.17",
                "ny2d": "NY Education Law 2-d", "sec": "SEC Form 8-K Item 1.05", "ftc-glba": "FTC Safeguards Rule (16 CFR 314.4(j))"}


def clock_rows(data: dict):
    """(rows, note, error): the statutory clocks from the record's awareness time, as gov clock computes them."""
    import datetime as dt
    from gov import clock
    aw = data["awareness"]
    if is_tbc(aw["time"]):
        return [], None, None
    try:
        aware, note = clock.parse(str(aw["time"]), aw["tz"])
    except ValueError as exc:
        return [], None, str(exc)
    notice = None if is_tbc(data["individual_notice"]) else dt.date.fromisoformat(str(data["individual_notice"]))
    rows = [{"due": due, "regime": regime, "duty": duty, "key": key} for key, due, regime, duty in clock.compute(aware, data["regimes"], data["states"], notice)]
    for m in data["matrix"]:
        due = m.get("due")
        if not due:
            continue
        if due == "immediately":
            key, text = aware, "Immediately"
        elif "T" in due:
            key = dt.datetime.fromisoformat(due).replace(tzinfo=aware.tzinfo); text = key.strftime("%Y-%m-%d %H:%M %Z")
        else:
            key = dt.datetime.combine(dt.date.fromisoformat(due), dt.time(23, 59), tzinfo=aware.tzinfo); text = due
        rows.append({"due": text, "regime": m["deadline_kind"].capitalize() if m["deadline_kind"] != "none" else "Matrix",
                     "duty": f"{m['recipient']}: {m['basis']}", "key": key})
    rows.sort(key=lambda r: r["key"])
    return rows, note, None


def inc(data: dict) -> dict:
    rows, note, error = clock_rows(data)
    return {
        "decision": data["decision"]["value"],
        "clock": rows,
        "clock_note": note,
        "earliest": next((r for r in rows if r["due"] != "no fixed date"), None),
        "regime_names": [REGIME_NAMES[r] for r in data["regimes"]],
        "notice_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "notice"),
        "open_rows": sum(1 for m in data["matrix"] if m["status"] not in ("sent", "delivered", "not-required")),
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def rdy(data: dict) -> dict:
    scope = [x for x in data["soa"] if x["applicability"] in ("in-scope", "opted-in")]
    return {
        "decision": data["decision"]["value"],
        "gate": "Audit start",
        "in_scope": len(scope),
        "excluded": sum(1 for x in data["soa"] if x["applicability"] == "excluded"),
        "undecided": sum(1 for x in data["soa"] if x["applicability"] == "undecided"),
        "gaps": sum(1 for x in scope if x["gap"] != "none"),
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


TIER_NAMES = {"0": "Tier 0 (Stop)", "1": "Tier 1 (High)", "2": "Tier 2 (Elevated)", "3": "Tier 3 (Standard)", "TBC": "TBC"}
LEVEL_TIER = {"stop": "0", "high": "1", "elevated": "2", "standard": "3"}


def factor_tier(data: dict) -> str:
    """The tier the highest factor level sets, or TBC when no factor is set."""
    tiers = [LEVEL_TIER[t["level"]] for t in data["tiering"] if t["level"] != TBC]
    return min(tiers) if tiers else TBC


def ais_follow_ons(data: dict) -> list:
    """The follow-ons tiering.md requires for the record's tier, cumulative, plus those its classification calls for.
    A TBC source or personal data counts as third-party and personal until it's known."""
    tier = data["tier"]["value"]
    third_party = data["source"] != "in-house"
    personal = data["personal_data"] != "none"
    need = []
    if tier in ("1", "2"):
        need.append("ai-impact-assessment")
    if tier in ("0", "1", "2") and personal:
        need.append("dpia-screening")
    if tier != TBC and third_party:
        need.append("vendor-review")
    if tier == "1":
        need += ["human-oversight", "testing-plan"]
    if data["ai_act"]["art50"]["value"] is not False and tier != TBC:
        need.append("art50-check")
    if data["ai_act"]["category"]["value"] == "high-risk":
        role = data["ai_act"]["company_role"]["value"]
        if role in ("provider", "provider-and-deployer"):
            need.append("ai-act-provider")
        if role in ("deployer", "provider-and-deployer"):
            need.append("ai-act-deployer")
    if tier == "1" and data["aiuc"]["mode"] == "readiness":
        need.append("aiuc-readiness")
    if personal and data["related"]["ropa"] in ("none", TBC):
        need.append("ropa-update")
    return need


def ais(data: dict) -> dict:
    tier = data["tier"]["value"]
    return {
        "decision": data["decision"]["value"],
        "tier": tier,
        "tier_name": TIER_NAMES[tier],
        "factor_tier": factor_tier(data),
        "follow_ons_open": sum(1 for f in data["follow_ons"] if f["status"] in ("recommended", "in-progress")),
        "follow_ons_needed": ais_follow_ons(data),
        "gate": "Use" if data["lifecycle"] in ("pilot", "live") else "Launch",
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def ctl(data: dict) -> dict:
    return {
        "objectives": [o["cco"] for o in data["objectives"]],
        "operation_evidence": sum(1 for e in data["evidence"] if e["shows"] == "operation" and e["status"] == "on-file"),
        "last_result": max(data["testing"], key=lambda t: t["date"])["result"] if data["testing"] else "none",
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def dsr_deadlines(data: dict) -> list:
    """Every deadline gov deadlines computes for the record's regimes, earliest first."""
    import datetime as dt
    from gov import deadlines
    table = deadlines.rules(dt.date.fromisoformat(str(data["received"]["date"])))
    rows = [{"due": due.isoformat(), "regime": regime, "step": step, "substantive": "Respond" in step or "Apply" in step}
            for regime in data["regimes"] for step, due in table[regime]]
    rows += [{"due": str(c["due"]), "regime": "contract", "step": f"{c['step']} ({c['basis']})", "substantive": True}
             for c in data["contract_deadlines"]]
    return sorted(rows, key=lambda r: (r["due"], r["regime"]))


def dsr(data: dict) -> dict:
    import datetime as dt
    from gov.skeleton import add_months
    rows = dsr_deadlines(data)
    substantive = [r for r in rows if r["substantive"] and "if extended" not in r["step"]]
    earliest = substantive[0] if substantive else None
    due = data["extended_deadline"] or (earliest["due"] if earliest else None)
    return {
        "deadlines": rows,
        "gate": "Response",
        "role_values": sorted({r["role"]["value"] for r in data["roles"]}),
        "earliest": earliest,
        "due": str(due) if due else None,
        "open": data["status"] not in ("Responded", "Closed"),
        "days_to_respond": (dt.date.fromisoformat(str(data["responded"])) - dt.date.fromisoformat(str(data["received"]["date"]))).days
        if data["responded"] else None,
        "retain_until": add_months(str(data["closed"]), 24) if data["closed"] else None,
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def sra(data: dict) -> dict:
    from gov import risk, security
    current = risk.overall(data["risks"], "current")
    applies = [e for e in data["elements"] if e["applicability"] != "not-applicable"]
    return {
        "decision": data["decision"]["value"],
        "kind_name": security.kinds()[data["kind"]]["name"],
        "met": sum(1 for e in applies if e["status"] == "met"),
        "gaps": sum(1 for e in applies if e["status"] in ("partial", "gap", "TBC")),
        "applies": len(applies),
        "inherent": risk.overall(data["risks"], "inherent"),
        "current": current,
        "target": risk.overall(data["risks"], "target"),
        "approver": APPROVER[current],
        "risk_rows": [{"id": k["id"], "risk": k["risk"], "owner": k["owner"], "inherent": risk.rate(k["inherent"]),
                       "current": risk.rate(k["current"]), "target": risk.rate(k["target"]),
                       "measures": "; ".join(f"{m['measure']} ({m['status']})" for m in k["measures"]) or "None"} for k in data["risks"]],
        "launch_blockers": _blockers(data),
        "launch_groups": _blocker_groups(data),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


DERIVE = {"sra": sra, "dsr": dsr, "ctl": ctl, "ais": ais, "rdy": rdy, "inc": inc, "aiia": aiia, "vr": vr, "dpia": dpia, "ropa": ropa, "lia": lia, "tia": tia, "tsr": tsr, "aip": ai_act, "aid": ai_act, "scr": scr}
