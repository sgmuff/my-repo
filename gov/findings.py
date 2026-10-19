"""Legal consistency checks. Each raises a finding for a person to resolve; none draws a conclusion."""
from __future__ import annotations

import re

from gov.derive import is_tbc

TBC = "TBC"
SAFE_REGIONS = {
    # EEA
    "austria", "belgium", "bulgaria", "croatia", "cyprus", "czechia", "czech republic", "denmark", "estonia",
    "finland", "france", "germany", "greece", "hungary", "ireland", "italy", "latvia", "lithuania", "luxembourg",
    "malta", "netherlands", "poland", "portugal", "romania", "slovakia", "slovenia", "spain", "sweden",
    "iceland", "liechtenstein", "norway", "eu", "eea", "european union",
    # UK and Switzerland
    "united kingdom", "uk", "switzerland",
}
INDEFINITE = re.compile(r"\b(indefinite(ly)?|forever|no (limit|deletion)|never deleted|kept until deleted)\b", re.I)


def ropa(data: dict) -> list:
    """(pointer, message) pairs."""
    out = []
    rtype = data["record_type"]["value"]

    for n, p in enumerate(data["purposes"]):
        where = f"purposes/{n}"
        if rtype == "processor" and p["decided_by"] == "company":
            out.append((where, f"{p['id']}: the company decides this purpose, so it's a controller for it (Art. 28(10)); record it as both or link a controller entry"))
        if p["decided_by"] == "customer" and p["lawful_basis"]["value"] not in ("controller-to-confirm", "not-applicable"):
            out.append((where, f"{p['id']}: a customer decides this purpose, so the customer chooses the lawful basis; use controller-to-confirm"))

    special_purposes = set()
    for n, c in enumerate(data["data_categories"]):
        if c["flags"] != TBC and any(f["flag"] == "special-category" for f in c["flags"]):
            special_purposes.update(c["purposes"])
        if not c["purposes"] and not is_tbc(c["category"]):
            out.append((f"data_categories/{n}", f"{c['category']}: no purpose uses this data; link it to a purpose, or stop collecting it"))
        if c["source"]["kind"] == "inferred":
            out.append((f"data_categories/{n}", f"{c['category']}: elements are inferred; confirm them or move them to an open question"))
    for n, p in enumerate(data["purposes"]):
        if p["id"] in special_purposes and p["art9_condition"]["value"] == "none":
            out.append((f"purposes/{n}", f"{p['id']} uses data flagged special category but records no Art. 9 condition"))

    recipients = data["recipients"] if isinstance(data["recipients"], list) else []
    abroad = [r["name"] for r in recipients if r["kind"] != "internal" and _outside_safe_regions(r["location"])]
    if abroad and data["transfers"] == "none":
        out.append(("transfers", f"transfers are none, but {', '.join(abroad)} store or access data outside the EEA, UK, and Switzerland; screen them"))

    for r in recipients:
        if r["kind"] not in ("processor", "sub-processor") or r["vendor_review"].startswith("VR-"):
            continue
        name = r["name"]
        if not _mentioned_as_blocker(data, name):
            out.append(("recipients", f"{name}: no reviewed contract on file, and nothing open blocks launch on it; Art. 28 requires the contract before processing starts. Add a launch-blocking action, or record why not"))
        if not _has_store(data, name):
            out.append(("retention", f"{name} holds a copy, but no retention row covers that store"))

    if data["ai_used"] is True and not data["related"]["ai_intake"].startswith("AIS-") \
            and not any(f["skill"] == "ai-intake" for f in data["follow_ons"]):
        out.append(("related/ai_intake", "AI is used, but there is no AI inventory entry or ai-intake follow-on"))

    for n, r in enumerate(data["retention"]):
        if INDEFINITE.search(r["current_practice"]) and not _has_action_about(data, r["data_category"]):
            out.append((f"retention/{n}", f"{r['data_category']} is kept indefinitely with no action to set a limit"))

    for key, call in data["us_flags"].items():
        if call["value"] is False and _open_question_on(data, f"us_flags/{key}"):
            out.append((f"us_flags/{key}", "recorded as false while an open question could change it; use TBC"))
    return out


def _outside_safe_regions(location: str) -> bool:
    if is_tbc(location):
        return False
    parts = [p.strip().lower() for p in re.split(r",|;|/|\band\b", location) if p.strip()]
    return any(p not in SAFE_REGIONS for p in parts)


def _has_action_about(data: dict, category: str) -> bool:
    words = {w for w in re.findall(r"[a-z_]+", category.lower()) if len(w) > 3}
    return any(words & set(re.findall(r"[a-z_]+", a["action"].lower())) for a in data["actions"])


def _key_words(name: str) -> set:
    return {w for w in re.findall(r"[a-z0-9]+", re.sub(r"\(.*?\)", "", name).lower()) if len(w) > 2 and w not in {"the", "vendor", "service", "tool"}}


def _mentioned_as_blocker(data: dict, name: str) -> bool:
    words = _key_words(name)
    texts = [a["action"] for a in data["actions"] if a["launch_blocking"] and a["status"] == "open"]
    texts += [q["question"] for q in data["open_questions"] if q["blocks"] == "launch"]
    return any(words & set(re.findall(r"[a-z0-9]+", t.lower())) for t in texts)


def _has_store(data: dict, name: str) -> bool:
    words = _key_words(name)
    return any(words & set(re.findall(r"[a-z0-9]+", f"{r['store']} {r['data_category']}".lower())) for r in data["retention"])


def _open_question_on(data: dict, field: str) -> bool:
    return any(q["field"] == field for q in data["open_questions"])


FINDINGS = {"ropa": ropa}
