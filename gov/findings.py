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
            out.append((f"data_categories/{n}/purposes", f"{c['category']}: no purpose uses this data; link it to a purpose, or stop collecting it"))
        if c["source"]["kind"] == "inferred":
            out.append((f"data_categories/{n}/source", f"{c['category']}: elements are inferred; confirm them or move them to an open question"))
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


def _law_action_citing(data: dict, pattern: str) -> bool:
    """An action, open or done, filed as law with a scope citing the given provision."""
    return any(a.get("block_reason") == "law" and re.search(pattern, a.get("scope", "")) for a in data["actions"])


def _action_citing(data: dict, pattern: str) -> bool:
    return any(re.search(pattern, a.get("scope", "") + " " + a["action"]) for a in data["actions"])


def lia(data: dict) -> list:
    out = []
    decision = data["decision"]["value"]
    holds = decision in ("holds", "holds-with-conditions")
    if data["special_category"]["value"] is True:
        out.append(("special_category", "an LIA never supplies an Art. 9 condition; confirm the DPIA names one"))
    if data["special_category"]["value"] is not False and not _action_citing(data, r"Art\.\s*9\b"):
        out.append(("actions/art9", "special category data is or may be involved, but no action addresses the Art. 9 condition"))
    objection = data["objection"]
    if objection["direct_marketing"] is True and not re.search(r"\b(absolute|always|stop|stops)\b", objection["how"], re.I):
        out.append(("objection", "direct marketing makes the right to object absolute (Art. 21(3)); say that processing stops on objection"))
    if objection["notice"] == "gap":
        out.append(("objection/notice", "the notice doesn't name the interest (Art. 13(1)(d), 14(2)(b)); recommend a notice update"))
    if objection["notice"] != "covered" and not _law_action_citing(data, r"Art\.\s*1[34]\b"):
        out.append(("actions/notice", "the notice isn't confirmed to cover this; add a launch-blocking law action for it, with Art. 13 or 14 in scope"))
    if holds:
        for key, call in (("purpose_test", "legitimate"), ("necessity_test", "necessary")):
            test = data[key]
            if test.get("applicable") and test[call]["value"] is not True:
                out.append((key, f"the decision says the interest holds, but {key.replace('_', ' ')} isn't met"))
        balancing = data["balancing"]
        if balancing.get("applicable") and balancing["outcome"]["value"] != "interest-prevails":
            out.append(("balancing", "the decision says the interest holds, but the balance doesn't favor it"))
        recognized = data["recognized_interest"]
        if recognized.get("applicable") and (recognized["conditions_met"]["value"] is not True or recognized["commenced"]["value"] is not True):
            out.append(("recognized_interest", "the decision says the interest holds, but the Annex 1 conditions or commencement aren't confirmed"))
        compat = data["compatibility"]
        if compat.get("applicable") and compat["outcome"]["value"] != "compatible":
            out.append(("compatibility", "the decision says the new purpose is fine, but compatibility isn't established"))
    if is_tbc(data["activity"]["ropa"]):
        out.append(("activity", "link the RoPA entry this assesses"))
    return out


def tia(data: dict) -> list:
    out = []
    decision = data["decision"]["value"]
    if data["mechanism"]["adequacy_checked"]["value"] is not True:
        out.append(("mechanism", "check adequacy and any DPF certification first; if one covers the importer, no TIA is needed"))
    impinges = data["destination_law"]["impinges"]["value"]
    effective = any(m["effective"]["value"] is True for m in data["measures"])
    if decision in ("proceed", "proceed-with-measures"):
        if impinges is not False and not effective:
            out.append(("measures", "the decision is to proceed, but step 3 found a problem or left it open and no measure is shown to work"))
        if data["procedural"]["signed"] is not True:
            out.append(("procedural", "the decision is to proceed, but the transfer tool isn't signed"))
    if not _law_action_citing(data, r"Art\.\s*46\b|IDTA|UK Addendum|FADP\s+Art\.\s*16\b"):
        out.append(("actions/transfer-tool", "no law action covers the transfer tool; add one to sign, or obtain and check, the executed tool, citing Art. 46, and mark it done once checked"))
    if data["transfer_map"]["special_category"]["value"] is True and not data["measures"]:
        out.append(("measures", "special category data is transferred with no supplementary measures recorded"))
    if is_tbc(data["activity"]):
        out.append(("activity", "link the RoPA entry this transfer belongs to"))
    return out


def _analysis(data: dict) -> list:
    return [("analysis", "write the analysis: the full legal reasoning, the provisional view, and what would change it")] if is_tbc(data.get("analysis", "TBC")) else []


def _with_issues(check):
    from gov import issues
    return lambda data: check(data) + _analysis(data) + issues.missing(data)


CERTIFICATION_ROUTES = {"eu-us-dpf", "uk-extension", "swiss-us-dpf", "TBC"}


def tsr(data: dict) -> list:
    out = []
    cert = data["mechanism"]["certification"]
    certified_route = data["mechanism"]["route"] in CERTIFICATION_ROUTES
    if data["decision"]["value"] == "no-tia-needed" and certified_route and (cert["status"] != "active" or cert["scope"] in ("TBC", "not-applicable")):
        out.append(("mechanism", "the screen says no TIA is needed, but the certification isn't shown active and covering this data"))
    if data["mechanism"]["route"] == "adequacy-decision" and cert["status"] not in ("not-applicable", "TBC"):
        out.append(("mechanism", "a country adequacy decision needs no certification; set the certification to not-applicable"))
    if is_tbc(data["activity"]):
        out.append(("activity", "link the RoPA entry this transfer belongs to"))
    return out


def _open_obligations(data: dict) -> list:
    return [o["article"] for o in data["obligations"] if o["status"] not in ("in-place", "not-applicable")]


def aip(data: dict) -> list:
    out = []
    c = data["classification"]
    decision = data["decision"]["value"]
    if data["kind"] == "non-high-risk":
        if c["profiling"]["value"] is not False:
            out.append(("classification/profiling", "an Annex III system that profiles natural persons is always high-risk (Art. 6(3), last subparagraph); confirm it doesn't"))
        if c["art6_3_condition"] in ("none", "TBC", "not-applicable"):
            out.append(("classification/art6_3_condition", "a non-high-risk claim needs an Art. 6(3) condition; without one the system is high-risk"))
    if c["call"]["value"] is True and data["kind"] == "non-high-risk":
        out.append(("classification/call", "the classification says high-risk, but the file is kind non-high-risk"))
    if decision in ("ready", "not-high-risk") and _open_obligations(data):
        out.append(("obligations", f"the decision is {decision}, but these aren't in place: {', '.join(_open_obligations(data))}"))
    if is_tbc(data["application_date"]):
        out.append(("application_date", "record when the obligations apply to this system, checked on EUR-Lex"))
    return out


def aid(data: dict) -> list:
    out = []
    check = data["provider_role_check"]
    triggered = [k for k in ("own_name", "substantial_modification", "new_high_risk_purpose") if check[k]["value"] is True]
    if triggered and data["decision"]["value"] != "becomes-provider":
        out.append(("provider_role_check", f"the deployer becomes the provider under Art. 25 ({', '.join(triggered)}); set the decision to becomes-provider and start a provider file"))
    if data["decision"]["value"] == "ready" and _open_obligations(data):
        out.append(("obligations", f"the decision is ready, but these aren't in place: {', '.join(_open_obligations(data))}"))
    if data["fria"]["required"]["value"] is not False and data["fria"]["record"] in ("TBC", "not-applicable"):
        out.append(("fria", "a FRIA is or may be owed under Art. 27 before first use; plan it with ai-impact-assessment, or record why it isn't owed"))
    if is_tbc(data["application_date"]):
        out.append(("application_date", "record when the deployer duties apply to this system, checked on EUR-Lex"))
    return out


FINDINGS = {"ropa": ropa, "lia": _with_issues(lia), "tia": _with_issues(tia), "tsr": _with_issues(tsr),
            "aip": _with_issues(aip), "aid": _with_issues(aid)}
