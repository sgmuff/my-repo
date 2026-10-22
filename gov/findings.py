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
    if data["kind"] == "outside-scope" and c["route"] in ("annex-i", "annex-iii"):
        out.append(("classification/route", f"the route is {c['route']}, so the system isn't outside the annexes; use kind high-risk, or non-high-risk with an Art. 6(3) condition"))
    if c["call"]["value"] is True and data["kind"] in ("non-high-risk", "outside-scope"):
        out.append(("classification/call", f"the classification says high-risk, but the file is kind {data['kind']}"))
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


def scr(data: dict) -> list:
    out = []
    decision = data["decision"]["value"]
    present = [c["criterion"] for c in data["criteria"] if c["result"] == "present"]
    always = [k for k, v in data["art35_3"].items() if v["value"] is True]
    if always and decision != "warranted":
        out.append(("art35_3", f"an Art. 35(3) case applies ({', '.join(always)}), so a DPIA is required; set the decision to warranted"))
    if len(present) >= 2 and decision == "not-indicated":
        out.append(("criteria", f"{len(present)} criteria are present ({', '.join(map(str, present))}); WP248 says that will need a DPIA in most cases, so the analysis must say why high risk is still unlikely"))
    if decision == "not-indicated" and any(c["result"] == "unclear" for c in data["criteria"]):
        out.append(("decision", "the decision is not-indicated while some criteria are unclear; resolve them, or keep the decision open"))
    if data["national_list"]["result"] == "listed" and decision != "warranted":
        out.append(("national_list", "the processing is on the authority's Art. 35(4) list, so a DPIA is required; set the decision to warranted"))
    if data["state_assessment"]["required"]["value"] is not False and not data["actions"]:
        out.append(("state_assessment", "a US state assessment is or may be owed whatever the GDPR outcome; add an action to produce it, or record why it isn't owed"))
    if is_tbc(data["activity"]) and not _ropa_action(data):
        out.append(("activity", "link the RoPA entry this screening covers, or add an action to create it"))
    return out


LEGITIMATE_INTERESTS = re.compile(r"6\(1\)\(f\)|legitimate interest", re.IGNORECASE)


def dpia(data: dict) -> list:
    from gov import risk
    out = []
    decision = data["decision"]["value"]
    risks = data["risks"]
    current = risk.overall(risks, "current")
    if len(risks) < 4:
        out.append(("risks", f"{len(risks)} {'risk' if len(risks) == 1 else 'risks'} recorded; a typical activity has 5 to 12, and fewer than 4 usually means one was missed (risk-method.md)"))
    out += _risk_levels(risks)
    if current == "High" and data["kind"] == "controller" and data["consultation"]["prior_consultation"]["value"] is not True:
        out.append(("consultation/prior_consultation", "the current residual rating is High; decide Art. 36 on its test (whether the DPIA shows a high risk the controller's measures don't mitigate) and record the call with its reasons"))
    if current == "High" and decision in ("proceed", "proceed-with-conditions"):
        out.append(("decision", "the decision lets processing go ahead while the current residual rating is High; record why Art. 36 consultation isn't required, or wait for it or for verified measures"))
    if risks and data["decision"]["status"] == "Confirmed" and not _residual_confirmed(data):
        out.append(("decision", "the decision is confirmed while residual risk isn't: some measures are unverified or the target differs from the current rating"))
    for n, row in enumerate(data["necessity"]):
        if row["principle"] == "lawful-basis" and LEGITIMATE_INTERESTS.search(row["basis"]) and not str(row["link"]).startswith("LIA-") \
                and not _open_action(data, r"\bLIA\b|legitimate interests assessment"):
            out.append((f"necessity/{n}/link", "the lawful basis is legitimate interests; link the LIA, or add an action to run lia"))
    art9 = [r for r in data["necessity"] if r["principle"] == "art9-condition"]
    if data["kind"] == "controller" and data["processing"]["special_category"]["value"] is not False:
        if not art9:
            out.append(("necessity", "special category data is or may be processed; add an art9-condition row with the Art. 9(2) condition relied on"))
        elif not any(r["position"] in ("adequate", "not-applicable") for r in art9):
            out.append(("necessity", "special category data is or may be processed, and no Art. 9(2) condition is in place yet; processing it waits until one is, or the design keeps the data out"))
    if is_tbc(data["screening"]):
        out.append(("screening", "link the screening record that found this DPIA warranted or recommended"))
    if is_tbc(data["activity"]) and not _ropa_action(data):
        out.append(("activity", "link the RoPA entry this DPIA covers, or add an action to create it"))
    return out


def _open_action(data: dict, pattern: str) -> bool:
    return any(re.search(pattern, a["action"], re.IGNORECASE) and a["status"] != "done" for a in data.get("actions", []))


def _ropa_action(data: dict) -> bool:
    return _open_action(data, r"\bRoPA\b|record of processing")


def _risk_levels(risks: list) -> list:
    from gov import risk
    out = []
    for n, k in enumerate(risks):
        statuses = {m["status"] for m in k["measures"]}
        if risk.lower(risk.rate(k["current"]), risk.rate(k["inherent"])) and "verified" not in statuses:
            out.append((f"risks/{n}/current", f"{k['id']}: the current rating is below the inherent one, but no measure is verified; only verified measures lower the current rating"))
        if risk.lower(risk.rate(k["target"]), risk.rate(k["current"])) and not statuses & {"planned", "unverified", "verified"}:
            out.append((f"risks/{n}/target", f"{k['id']}: the target rating is below the current one, but no measure is planned"))
    return out


TIA_TOOLS = {"sccs", "uk-idta", "uk-addendum", "bcrs"}
SCREEN_ROUTES = {"adequacy", "eu-us-dpf", "uk-extension", "swiss-us-dpf"}
GAPS = {"partial", "missing", "conflicts", "not-provided"}


def vr(data: dict) -> list:
    out = []
    decision = data["decision"]["value"]
    rows = data["clauses"] + (data["ai"]["items"] if data["ai"]["applicable"] else [])
    asked = {i.strip() for r in data["requests"] for i in str(r["item"]).split(",")}
    gaps = [r["item"] for r in rows if r["rating"] in GAPS]
    fixed = {r["item"] for r in rows if str(r["fix"]).strip().lower() not in ("", "none", "tbc")}
    if decision == "approve" and gaps:
        out.append(("decision", f"the recommendation is approve without conditions, but these items are gaps or weren't provided: {', '.join(gaps)}"))
    core = [r["item"] for r in data["clauses"] if r["item"].startswith("2.") and r["rating"] in ("missing", "conflicts")]
    if core and decision in ("approve", "approve-with-conditions"):
        out.append(("clauses", f"Art. 28(3) terms are missing or overridden ({', '.join(core)}); a signed fix is a condition before personal data flows"))
    unasked = [i for i in gaps if i not in asked and i not in fixed]
    if unasked:
        out.append(("requests", f"these gaps have no request and no fix: {', '.join(unasked)}; add a request to the vendor, or record the fix or compensating control in the item"))
    if data["kind"] == "notice" and is_tbc(data.get("objection_deadline", "TBC")):
        out.append(("objection_deadline", "record the last day to object under the DPA; the objection decision comes first"))
    if data["ai"]["applicable"]:
        training = next((r for r in data["ai"]["items"] if r["item"] == "6.1"), None)
        if training and training["rating"] != "present" and decision in ("approve", "approve-with-conditions") and "6.1" not in asked:
            out.append(("ai/items", "training and improvement terms (6.1) aren't settled; ask for them before customer data reaches the AI feature"))
    for n, t in enumerate(data["transfers"]):
        if t["mechanism"] in TIA_TOOLS and not str(t["link"]).startswith("TIA-") and not _open_action(data, r"\bTIA\b|transfer impact"):
            out.append((f"transfers/{n}/link", f"{t['flow']} relies on {t['mechanism']}; link the TIA, or add an action to run tia"))
        elif t["mechanism"] in SCREEN_ROUTES and not str(t["link"]).startswith(("TSR-", "TIA-")) and not _open_action(data, r"\bTSR\b|transfer screen"):
            out.append((f"transfers/{n}/link", f"{t['flow']} relies on {t['mechanism']}; link the transfer screen (TSR), or add an action to run tia"))
        elif t["mechanism"] == "TBC" and not _open_action(data, r"transfer|\bTIA\b|\bTSR\b|mechanism"):
            out.append((f"transfers/{n}/mechanism", f"{t['flow']}: the transfer mechanism isn't known yet; add an action to establish it"))
    if data["depth"]["value"] == "deep" and data["security"]["covers_service"]["value"] is not True and decision in ("approve", "approve-with-conditions"):
        out.append(("security", "a deep review recommends approval without a security report shown to cover the service"))
    out += _risk_levels(data["risks"])
    if any(is_tbc(a) for a in data["activities"]) and not _ropa_action(data):
        out.append(("activities", "link the RoPA entries that use this vendor, or add an action to update them"))
    return out


def aiia(data: dict) -> list:
    from gov import risk
    out = []
    decision = data["decision"]["value"]
    ids = {k["id"] for k in data["risks"]}
    if data["ai_act"]["prohibited"]["value"] is not False and decision in ("proceed", "proceed-with-conditions"):
        out.append(("ai_act/prohibited", "a possible Art. 5 prohibited practice isn't ruled out; prohibitions already apply, so the use can't go ahead until it is"))
    if data["kind"] == "aiia":
        open_domains = [g["domain"] for g in data["domains"] if g["position"] == "TBC"]
        if data["tier"] == "1" and open_domains and decision in ("proceed", "proceed-with-conditions"):
            out.append(("domains", f"a Tier 1 assessment proposes going ahead with domains not yet assessed: {', '.join(open_domains)}"))
        if not data["risks"]:
            out.append(("risks", "no risks recorded; rate the harms to people and groups that the domains raise"))
    elif all(k in data["fria"] for k in ("deployer_status", "rights_risks", "notification")):  # else validate reports the gap
        fr = data["fria"]
        if data["kind"] == "fria" and fr["deployer_status"] == "not-owed":
            out.append(("fria/deployer_status", "the record is a FRIA, but says the deployer doesn't owe one; record the reason in analysis, or change the kind"))
        if not fr["rights_risks"]:
            out.append(("fria/rights_risks", "Art. 27(1)(d) needs the specific risks of harm to the people and groups affected"))
        for n, k in enumerate(fr["rights_risks"]):
            if k["risk_id"] not in ids and k["risk_id"] != "none" and not re.fullmatch(r"AIIA-\d{4}-\d{3}/R\d+", k["risk_id"]):
                out.append((f"fria/rights_risks/{n}/risk_id", f"{k['right']}: risk row {k['risk_id']} doesn't exist in this record"))
        if data["kind"] == "fria" and fr["notification"] in ("TBC", "not-required") and decision in ("proceed", "proceed-with-conditions"):
            out.append(("fria/notification", "a deployer notifies the market surveillance authority of the FRIA's results (Art. 27(3)) unless an exemption applies; record which"))
        if is_tbc(data["related"]["aiia"]) or data["related"]["aiia"] == "none":
            out.append(("related/aiia", "link the AI impact assessment the FRIA draws on, or add an action to produce one"))
    if risk.overall(data["risks"], "current") == "High" and decision == "proceed":
        out.append(("decision", "the current residual rating is High, but the decision is to proceed without conditions"))
    out += _risk_levels(data["risks"])
    if is_tbc(data["system"]) and not _open_action(data, r"inventory|ai-intake|\bAIS\b"):
        out.append(("system", "link the AI inventory entry, or add an action to run ai-intake"))
    return out


def inc(data: dict) -> list:
    out = []
    aw = data["awareness"]
    if is_tbc(aw["time"]):
        out.append(("awareness/time", "record when the company became aware, with the zone; the clocks start there"))
    elif not aw["confirmed"]:
        out.append(("awareness/confirmed", "every deadline is a working deadline until the incident commander confirms the awareness time"))
    if is_tbc(data["commander"]):
        out.append(("commander", "name one incident commander who owns the timeline"))
    roles = {r for d in data["datasets"] for r in d["roles"]}
    recipients = " ".join(m["recipient"].lower() for m in data["matrix"])
    if roles & {"processor", "maintainer"} and not re.search(r"controller|customer|owner", recipients):
        out.append(("matrix", "the company is a processor or maintainer for some data; notifying each controller or owner comes first"))
    if "school-official" in roles and not re.search(r"district|institution|school|university|college", recipients):
        out.append(("matrix", "the company is a school official for some data; each institution must be notified under its agreement"))
    if "gdpr" in data["regimes"] and "controller" in roles:
        if not re.search(r"authority|dpc|cnil|ico|regulator|commissioner", recipients):
            out.append(("matrix", "add the supervisory authority as its own row (Art. 33), even if the decision is not to notify"))
        if not re.search(r"individual|data subject|resident|customer|user|people", recipients):
            out.append(("matrix", "add individuals as their own row (Art. 34), decided separately from the authority"))
    drafted = {n["recipient"] for n in data["notices"]}
    for n, m in enumerate(data["matrix"]):
        if m["required"]["value"] is True and m["status"] in ("not-started", "drafting") and m["recipient"] not in drafted:
            out.append((f"matrix/{n}", f"{m['recipient']}: notice is required but no draft exists yet"))
        if m["status"] in ("sent", "delivered") and is_tbc(m.get("sent", "TBC")):
            out.append((f"matrix/{n}/sent", f"{m['recipient']}: record when the notice went, how, to whom, and whether delivery was confirmed"))
    if data["decision"]["value"] in ("notify", "notify-some", "no-notice-required") and not data["decisions"]:
        out.append(("decisions", "the record states a notification position, but the decision log has no decision by counsel or the privacy lead"))
    if data["ongoing"]["value"] is not False and not data["containment"]:
        out.append(("containment", "the incident is or may be ongoing; record security's containment measures and their status"))
    return out


def rdy(data: dict) -> list:
    from gov.aiuc import THIRD_PARTY_TESTING
    out = []
    decision = data["decision"]["value"]
    scope = [x for x in data["soa"] if x["applicability"] in ("in-scope", "opted-in")]
    gaps = [x["requirement"] for x in scope if x["gap"] != "none"]
    if decision == "ready" and gaps:
        out.append(("decision", f"the report says ready, but these requirements have gaps or aren't assessed: {', '.join(gaps)}"))
    bare = [x["requirement"] for x in scope if not x["controls"]
            and not (x["gap"] == "missing" and _open_action(data, rf"\b{x['requirement']}\b"))]
    if bare:
        out.append(("soa", f"no control carries these in-scope requirements: {', '.join(bare)}; map a control, or record the gap as missing with an open action naming the requirement"))
    undecided = [x["requirement"] for x in data["soa"] if x["applicability"] == "undecided"]
    if undecided:
        out.append(("soa", f"the business hasn't decided whether to opt in to these optional requirements: {', '.join(undecided)}"))
    timed = {t["requirement"]: t for t in data["testing"]}
    for x in scope:
        if x["requirement"] in THIRD_PARTY_TESTING:
            t = timed.get(x["requirement"])
            if not t or is_tbc(t["next_due"]):
                out.append(("testing", f"{x['requirement']} needs third-party testing at least every 3 months; record the next date and the control that carries it"))
    if is_tbc(data["release"]):
        out.append(("release", "record the AIUC-1 release the audit runs against; it's fixed at kickoff"))
    if is_tbc(data["system"]) and not _open_action(data, r"inventory|ai-intake|\bAIS\b"):
        out.append(("system", "link the AI inventory entry, or add an action to run ai-intake"))
    return out


def ais(data: dict) -> list:
    import datetime as dt
    from gov import derive
    from gov.skeleton import add_months
    out = []
    tier = data["tier"]["value"]
    floor = derive.factor_tier(data)
    if tier != TBC and floor != TBC and int(tier) > int(floor):
        out.append(("tier", f"the tier is the highest level any factor reaches; a factor is at {floor}, so the tier can't be {tier}"))
    if data["ai_act"]["prohibited"]["value"] is True and tier != "0":
        out.append(("tier", "the record says the function could be an Art. 5 prohibited practice; that makes it Tier 0 (Stop)"))
    if tier == "0" and data["decision"]["value"] != "stop":
        out.append(("decision", "a Tier 0 system is a stop until the privacy lead and counsel decide"))
    if tier == "0" and data["lifecycle"] in ("pilot", "live") and not data["containment"]:
        out.append(("containment", "a Tier 0 function is in use; record the control that stops it, with evidence"))
    for n, c in enumerate(data["containment"]):
        if c["downstream_stopped"] is not True:
            out.append((f"containment/{n}/downstream_stopped", "confirm the output is no longer generated, shown, exported, or used downstream"))
    if data["ai_act"]["category"]["value"] == "high-risk" and (is_tbc(data["ai_act"]["annex_point"]) or data["ai_act"]["annex_point"] == "none"):
        out.append(("ai_act/annex_point", "a high-risk classification needs the Annex III point or the Art. 6(1) basis"))
    listed = {f["follow_on"] for f in data["follow_ons"]}
    missing = [f for f in derive.ais_follow_ons(data) if f not in listed]
    if missing:
        out.append(("follow_ons", f"the tier and classification call for these follow-ons, which the record doesn't list: {', '.join(missing)}"))
    for n, f in enumerate(data["follow_ons"]):
        if f["status"] in ("in-progress", "done") and (is_tbc(f["record"]) or f["record"] == "none"):
            out.append((f"follow_ons/{n}/record", f"{f['follow_on']} is {f['status']}; link its record"))
    if tier in ("1", "2") and len(data["top_risks"]) < 3:
        out.append(("top_risks", "name at least three risks from the AI risk catalog (risk-method.md section 2a)"))
    months = {"1": 6, "2": 6, "3": 12}.get(tier)
    if months:
        start = dt.date.fromisoformat(str(data["last_reviewed"] or data["date_prepared"]))
        if dt.date.fromisoformat(str(data["next_review"])) > dt.date.fromisoformat(add_months(start.isoformat(), months)):
            out.append(("next_review", f"Tier {tier} entries are reviewed at least every {months} months"))
    return out


def _residual_confirmed(data: dict) -> bool:
    from gov import derive
    return derive.dpia(data)["confirmed"]


FINDINGS = {"ais": _with_issues(ais), "rdy": _with_issues(rdy), "inc": _with_issues(inc), "aiia": _with_issues(aiia), "vr": _with_issues(vr), "dpia": _with_issues(dpia), "scr": _with_issues(scr), "ropa": ropa, "lia": _with_issues(lia), "tia": _with_issues(tia), "tsr": _with_issues(tsr),
            "aip": _with_issues(aip), "aid": _with_issues(aid)}
