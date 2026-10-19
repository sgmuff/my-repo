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


def _blockers(data: dict) -> list:
    return [a["id"] for a in data["actions"] if a["launch_blocking"] and a["status"] == "open"] + [
        q["id"] for q in data["open_questions"] if q["blocks"] == "launch"
    ]


def lia(data: dict) -> dict:
    tests = [data[k] for k in ("purpose_test", "necessity_test") if data[k].get("applicable")]
    open_calls = [t for t in tests for key in ("legitimate", "necessary") if key in t and t[key]["value"] == TBC]
    balancing = data["balancing"]
    return {
        "decision": data["decision"]["value"],
        "open_tests": len(open_calls) + (1 if balancing.get("applicable") and balancing["outcome"]["value"] == "open" else 0),
        "launch_blockers": _blockers(data),
        "blocking_questions": sum(1 for q in data["open_questions"] if q["blocks"] in ("launch", "approval")),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


def tia(data: dict) -> dict:
    return {
        "decision": data["decision"]["value"],
        "effective_measures": sum(1 for m in data["measures"] if m["effective"]["value"] is True),
        "launch_blockers": _blockers(data),
        "blocking_questions": sum(1 for q in data["open_questions"] if q["blocks"] in ("launch", "approval")),
        "launch_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "launch"),
        "approval_questions": sum(1 for q in data["open_questions"] if q["blocks"] == "approval"),
    }


DERIVE = {"ropa": ropa, "lia": lia, "tia": tia}
