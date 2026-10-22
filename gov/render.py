"""Markdown rendering from records. The model never writes these files."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from gov import derive, ids
from gov.paths import PACKAGE, output_root
from gov.records import load, record_files
from gov.validate import Problem, _rel, validate_tree

LABELS = {
    "data-subject": "Data subject",
    "parent-or-guardian": "Parent or guardian",
    "authorized-agent": "Authorized agent",
    "access": "Access",
    "deletion": "Deletion",
    "correction": "Correction",
    "portability": "Portability",
    "opt-out": "Opt-out",
    "limit": "Limit use of sensitive data",
    "restriction": "Restriction",
    "automated-decision": "Automated decision",
    "appeal": "Appeal",
    "consent-withdrawal": "Withdraw consent or refuse further use",
    "stated-by-staff": "Stated by company staff",
    "verified": "Verified",
    "failed": "Failed",
    "delete": "Delete",
    "correct": "Correct",
    "export": "Export",
    "stop-processing": "Stop processing",
    "acknowledgment": "Acknowledgment",
    "verification-request": "Verification request",
    "extension-notice": "Extension notice",
    "response": "Response",
    "referral": "Referral to the controller or institution",
    "clarification": "Clarification request",
    "in-use": "In use",
    "none-yet": "None yet",
    "semiannual": "Semiannual",
    "on-file": "On file",
    "designed": "Designed",
    "implemented": "Implemented",
    "not-in-place": "Not yet in place",
    "evidenced": "Implemented and evidenced",
    "unverified": "Implemented but unverified",
    "absent": "Absent",
    "continuous": "Continuous",
    "daily": "Daily",
    "weekly": "Weekly",
    "monthly": "Monthly",
    "quarterly": "Quarterly",
    "annual": "Annual",
    "per-event": "Per event",
    "full": "Full",
    "test-result": "Test result",
    "report": "Report",
    "attestation": "Attestation",
    "design": "Design",
    "operation": "Operation",
    "inspection": "Inspection",
    "sample": "Sample",
    "re-performance": "Re-performance",
    "third-party-evaluation": "Third-party evaluation",
    "pass": "Pass",
    "exceptions": "Exceptions",
    "fail": "Fail",
    "system": "AI system",
    "vendor-model": "Built on a vendor model",
    "vendor-product": "Vendor product",
    "embedded-feature": "Embedded feature",
    "in-house": "In-house",
    "idea": "Idea",
    "pilot": "Pilot",
    "live": "Live",
    "retired": "Retired",
    "proceed-to-follow-ons": "Proceed to the follow-ons; not authorized for use by this intake",
    "prohibited": "Possibly prohibited (Art. 5)",
    "minimal": "Minimal risk",
    "not-ai": "Not an AI system",
    "L0-suggest": "L0: suggests only",
    "L1-act-with-approval": "L1: acts with approval",
    "L2-act-within-limits": "L2: acts within limits",
    "L3-act-broadly": "L3: acts broadly",
    "informs": "Informs a decision a person makes",
    "decides": "Makes low-stakes decisions itself",
    "significant": "Makes or materially influences significant decisions",
    "stop": "Stop",
    "high": "High",
    "elevated": "Elevated",
    "applied": "Applied",
    "art50-check": "Art. 50 transparency check",
    "testing-plan": "Quarterly testing plan",
    "notice-update": "Notice update (notice-and-policy)",
    "ropa-update": "RoPA entry (ropa)",
    "personal": "Personal",
    "sensitive": "Sensitive",
    "benchmark": "Vendor benchmark",
    "ai-act-use": "Use under the EU AI Act",
    "decisions-about-people": "Decisions about people",
    "people-affected": "People affected",
    "data": "Data",
    "autonomy": "Autonomy",
    "reach-and-reversibility": "Reach and reversibility",
    "ai-impact-assessment": "AI impact assessment (ai-impact-assessment)",
    "dpia-screening": "DPIA screening (dpia)",
    "vendor-review": "Vendor review (vendor-review)",
    "aup": "AUP coverage (notice-and-policy)",
    "ai-act-provider": "AI Act provider file (ai-act-provider)",
    "ai-act-deployer": "AI Act deployer checks (ai-act-deployer)",
    "aiuc-readiness": "AIUC-1 readiness (controls-and-evidence)",
    "not-needed": "Not needed",
    "undecided": "Undecided (optional)",
    "never": "Never",
    "source": "Source",
    "readiness": "AIUC-1 readiness",
    "not-ready": "Not ready",
    "in-scope": "In scope",
    "excluded": "Excluded",
    "opted-in": "Opted in",
    "model-provider": "Model provider",
    "shared": "Shared",
    "met": "Met",
    "incident": "Incident",
    "notify": "Notify",
    "notify-some": "Notify some recipients",
    "no-notice-required": "No notice required",
    "undetermined": "Undetermined pending review",
    "maintainer": "Maintainer",
    "school-official": "School official",
    "statutory": "Statutory",
    "not-started": "Not started",
    "drafting": "Drafting",
    "awaiting-approval": "Awaiting approval",
    "delivered": "Delivered",
    "done-verified": "Done and verified",
    "done-unverified": "Done, not verified",
    "in-progress": "In progress",
    "unknown": "Unknown",
    "provider-and-deployer": "Provider and deployer",
    "not-yet-due": "Not yet due",
    "aiia": "AI impact assessment",
    "fria": "Fundamental rights impact assessment",
    "fria-input-pack": "FRIA input pack",
    "fairness": "Fairness and non-discrimination",
    "human-oversight": "Human oversight",
    "data-provenance": "Data provenance and quality",
    "reliability": "Reliability and model limitations",
    "safety": "Safety",
    "security": "Security",
    "accountability": "Accountability",
    "society": "Society",
    "public-body": "Body governed by public law",
    "public-service": "Private entity providing public services",
    "annex-iii-5b": "Deployer of an Annex III point 5(b) system",
    "annex-iii-5c": "Deployer of an Annex III point 5(c) system",
    "not-owed": "Not owed",
    "drafted": "Drafted",
    "sent": "Sent",
    "not-required": "Not required",
    "provider": "Provider",
    "distributor": "Distributor",
    "service-provider": "Service provider",
    "contractor": "Contractor",
    "joint-controller": "Joint controller",
    "missing": "Missing",
    "conflicts": "Conflicts",
    "not-provided": "Not provided",
    "provided": "Provided",
    "requested": "Requested",
    "partial": "Partial",
    "light": "Light",
    "standard": "Standard",
    "deep": "Deep",
    "approve": "Approve",
    "approve-with-conditions": "Approve with conditions",
    "do-not-approve": "Do not approve as proposed",
    "new": "New vendor",
    "renewal": "Renewal",
    "reassessment": "Reassessment",
    "notice": "Change notice",
    "document": "Document",
    "contract-change": "Contract change",
    "configuration": "Configuration",
    "question": "Question",
    "objection": "Objection",
    "none-needed": "None needed",
    "controller": "Controller",
    "processor": "Processor",
    "both": "Controller and processor",
    "consent": "Consent (Art. 6(1)(a))",
    "contract": "Contract (Art. 6(1)(b))",
    "legal-obligation": "Legal obligation (Art. 6(1)(c))",
    "vital-interests": "Vital interests (Art. 6(1)(d))",
    "public-task": "Public task (Art. 6(1)(e))",
    "legitimate-interests": "Legitimate interests (Art. 6(1)(f))",
    "not-applicable": "Not applicable",
    "internal": "Internal",
    "authority": "Authority",
    "adequacy": "Adequacy decision",
    "eu-us-dpf": "EU-US Data Privacy Framework",
    "sccs": "SCCs",
    "uk-idta": "UK IDTA",
    "uk-addendum": "UK Addendum",
    "bcrs": "BCRs",
    "art49-derogation": "Art. 49 derogation",
    "covered": "Covered",
    "gap": "Gap",
    "approved": "Approved",
    "approved-with-conditions": "Approved with conditions",
    "rejected": "Rejected",
    "recommended": "Recommended",
    "none": "None",
    "special-category": "Special category",
    "criminal": "Criminal",
    "biometric": "Biometric",
    "us-sensitive": "US-sensitive",
    "education-record": "Education record",
    "children": "Children",
    "government-id": "Government ID",
    "financial": "Financial",
    "company": "Company",
    "customer": "Customer",
    "joint": "Joint",
    "controller-to-confirm": "Controller to confirm",
    "sub-processor": "Sub-processor",
    "eu-gdpr": "EU GDPR",
    "uk-gdpr": "UK GDPR",
    "ch-fadp": "Swiss FADP",
    "stored": "Stored",
    "remote-access": "Remote access",
    "uk-extension": "UK Extension to the DPF",
    "swiss-us-dpf": "Swiss-US DPF",
    "launch": "Launch",
    "lia": "Legitimate interests assessment",
    "recognized-interest": "UK recognized legitimate interest",
    "compatibility": "Compatibility assessment",
    "holds": "Holds",
    "holds-with-conditions": "Holds with conditions",
    "does-not-hold": "Does not hold as proposed",
    "interest-prevails": "Interest prevails",
    "rights-prevail": "Rights prevail",
    "compatible": "Compatible",
    "not-compatible": "Not compatible",
    "third-party": "Third party",
    "in-place": "In place",
    "planned": "Planned",
    "eu-tia": "EU transfer impact assessment",
    "uk-tra": "UK transfer risk assessment",
    "ch-tia": "Swiss transfer assessment",
    "ch-sccs": "SCCs with Swiss adaptations",
    "proceed": "Proceed",
    "proceed-with-measures": "Proceed with measures",
    "suspend": "Suspend",
    "technical": "Technical",
    "contractual": "Contractual",
    "organizational": "Organizational",
    "law": "law",
    "policy": "policy",
    "risk": "risk",
    "approval": "Approval",
    "record": "Record",
    "open": "Open",
    "done": "Done",
    "addressed": "Addressed",
    "not-addressed": "Not addressed",
    "no-tia-needed": "No TIA needed",
    "tia-needed": "TIA needed",
    "adequacy-decision": "Adequacy decision",
    "active": "Active",
    "inactive": "Inactive",
    "not-listed": "Not listed",
    "hr": "HR data",
    "non-hr": "Non-HR data",
    "hr-and-non-hr": "HR and non-HR data",
    "art6-4": "Art. 6(4) Documented assessment that it isn't high-risk",
    "art49-2": "Art. 49(2) Registration of a non-high-risk Annex III system",
    "art9": "Art. 9 Risk management system",
    "art10": "Art. 10 Data and data governance",
    "art11": "Art. 11 Technical documentation (Annex IV)",
    "art12": "Art. 12 Automatic logging",
    "art13": "Art. 13 Transparency and instructions for use",
    "art14": "Art. 14 Human oversight",
    "art15": "Art. 15 Accuracy, robustness, and cybersecurity",
    "art17": "Art. 17 Quality management system",
    "art43": "Art. 43 Conformity assessment",
    "art47-49": "Arts. 47-49 Declaration of conformity, CE marking, and registration",
    "art72": "Art. 72 Post-market monitoring plan",
    "art73": "Art. 73 Serious incident reporting",
    "art4": "Art. 4 AI literacy",
    "art26-1": "Art. 26(1) Use per the instructions",
    "art26-2": "Art. 26(2) Human oversight assigned",
    "art26-4": "Art. 26(4) Input data relevant and representative",
    "art26-5": "Art. 26(5) Monitoring, suspension, and incident reporting",
    "art26-6": "Art. 26(6) Logs kept at least 6 months",
    "art26-7": "Art. 26(7) Workers and their representatives informed",
    "art26-9": "Art. 26(9) DPIA using the provider's information",
    "art26-11": "Art. 26(11) People told a high-risk system is used",
    "art50": "Art. 50 Transparency to people",
    "art86": "Art. 86 Right to an explanation",
    "outside-scope": "Not high-risk (outside Annexes I and III)",
    "warranted": "DPIA warranted",
    "proceed-with-conditions": "Proceed with conditions",
    "prior-consultation": "Prior consultation, unless verified measures lower the current rating first",
    "do-not-proceed": "Do not proceed",
    "lawful-basis": "Lawful basis",
    "art9-condition": "Art. 9 condition",
    "minimization": "Data minimization",
    "purpose-limitation": "Purpose limitation",
    "transparency": "Transparency",
    "rights": "Data subject rights",
    "retention": "Retention",
    "automated-decisions": "Profiling and automated decisions",
    "transfers": "Transfers",
    "adequate": "Adequate",
    "not-met": "Not met",
    "cppa": "CPPA risk assessment",
    "coppa": "COPPA",
    "state-student-privacy": "State student privacy laws",
    "confirmed": "Confirmed",
    "stated-by-requester": "Stated by requester",
    "stated-by-vendor": "Stated by vendor",
    "assumption": "Assumption",
    "not-indicated": "DPIA not indicated",
    "present": "Present",
    "not-present": "Not present",
    "unclear": "Unclear",
    "listed": "Listed",
    "us-states": "US states",
    "ferpa": "FERPA",
    "eu-ai-act": "EU AI Act",
    "non-high-risk": "Not high-risk (Art. 6(3))",
    "high-risk": "High-risk",
    "deployer": "Deployer",
    "not-high-risk": "Not high-risk",
    "ready": "Ready",
    "gaps": "Gaps",
    "becomes-provider": "Becomes the provider (Art. 25)",
    "annex-i": "Annex I",
    "annex-iii": "Annex III",
    "narrow-procedural-task": "Narrow procedural task",
    "improves-completed-human-activity": "Improves a completed human activity",
    "detects-patterns-without-replacing-assessment": "Detects patterns without replacing human assessment",
    "preparatory-task": "Preparatory task",
}
SOURCE_KINDS = {"document": "Document", "stated": "Stated by", "inferred": "Inferred", "tbc": "TBC"}


def cell(value) -> str:
    if value is None:
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def yn(value) -> str:
    if isinstance(value, bool):
        return "Yes" if value else "No"
    return cell(value)


def label(value) -> str:
    if value is None:
        return "—"
    return LABELS.get(value, cell(value))


def src(source: dict) -> str:
    kind = SOURCE_KINDS[source["kind"]]
    return f"{kind}: {cell(source['ref'])}" if source.get("ref") else kind


def join_or_tbc(value) -> str:
    return "TBC" if value == "TBC" else ", ".join(cell(v) for v in value)


def flags(value) -> str:
    if value == "TBC":
        return "TBC"
    if not value:
        return "None"
    return "; ".join(f"{label(f['flag'])} ({f['status']}: {cell(f['reason'])})" for f in value)


def call(position: dict) -> str:
    """A position with its status and reason: "Contract (Art. 6(1)(b)). Provisional: reason"."""
    value = position["value"]
    shown = yn(value) if isinstance(value, bool) else label(value)
    if value == "TBC":
        return f"TBC: {cell(position['reason'])}"
    return f"{shown}. {position['status']}: {cell(position['reason'])}"


@lru_cache(maxsize=None)
def _env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(PACKAGE / "templates")),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        autoescape=False,
    )
    env.filters.update(tier_name=lambda t: derive.TIER_NAMES.get(t, t), cell=cell, yn=yn, label=label, src=src, join_or_tbc=join_or_tbc, flags=flags, call=call)
    return env


STATUS_TEXT = {
    "owed": "Owed",
    "tbc": "May be owed",
    "not-yet-applicable": "Not yet applicable",
    "no-reference": "Waiting for its reference file",
    "on-file": "On file",
    "planned": "Planned",
    "not-applicable": "Not applicable",
}


def required_rows(root, data: dict) -> list:
    """The catalog's verdict for this activity, merged with the record's responses, in catalog order."""
    from gov import required as req
    responses = {a["assessment"]: a for a in data.get("assessments", [])}
    computed = {r["assessment"]: r for r in req.evaluate(req.facts_from_ropa(data), data["date_prepared"], root)}
    rows = []
    for e in req.catalog()["entries"]:
        eid = e["id"]
        if eid not in computed and eid not in responses:
            continue
        r = computed.get(eid)
        a = responses.get(eid)
        if a:
            status = STATUS_TEXT[a["status"]]
            detail = a.get("record") or ""
            if a.get("reason"):
                detail = (detail + "; " if detail else "") + a["reason"]
            if a["status"] == "not-applicable":
                detail += f" ({a['by']})"
        else:
            status, detail = STATUS_TEXT[r["status"]], r["reason"]
        rows.append({"name": e["name"], "citation": e["citation"], "gate": e["gate"].capitalize(),
                     "status": status, "detail": detail, "skill": e["produced_by"],
                     "kind": "listed" if a or r["status"] == "owed" else r["status"], "open": (r or {}).get("open_facts", []),
                     "applies_from": e["applies_from"], "reference": e["reference"]})
    return rows


@lru_cache(maxsize=None)
def _methods() -> dict:
    from gov import yamlio
    return yamlio.load(PACKAGE / "rules" / "methods.yaml")


def finding_rows(rec, root=None) -> list:
    """Every current finding with its response, then responses whose finding no longer arises."""
    from gov import references
    from gov.findings import FINDINGS
    responses = {r["pointer"]: r for r in rec.data.get("finding_responses", [])}
    rows, seen = [], set()
    stale = references.findings(root, rec.data) if root else []
    for pointer, message in FINDINGS[rec.type](rec.data) + stale:
        r = responses.get(pointer)
        seen.add(pointer)
        rows.append({"pointer": pointer, "finding": message, "response": r["response"] if r else "Open", "by": r["by"] if r else None})
    for pointer, r in responses.items():
        if pointer not in seen:
            rows.append({"pointer": pointer, "finding": "No longer raised", "response": r["response"], "by": r["by"]})
    return rows


def render_record(rec, root=None) -> str:
    template = _env().get_template(f"{rec.type}.md.j2")
    from gov import issues
    method = _methods().get(rec.type, {}).get(rec.data.get("kind"))
    if isinstance(method, dict):
        method = method.get((rec.data.get("regimes") or ["eu-gdpr"])[0])
    from gov import references
    extra = {"findings": finding_rows(rec, root), "method": method, "ref_notes": references.notes(root, rec.data),
             "issue_rows": issues.rows(rec.data) if rec.type != "ropa" else [], "issue_rules_apply": issues.covers(rec.type),
             "gate": derive.DERIVE[rec.type](rec.data).get("gate", "Launch")}
    if rec.type == "ctl":
        from gov import crosswalk
        extra["crosswalk"] = crosswalk.objectives(root)
    if rec.type == "rdy":
        from gov import aiuc
        extra["aiuc"] = aiuc.requirements(root)
    if rec.type == "inc":
        entry = references.index(root).get("us-breach-notification.md") if root else None
        counsel = (entry or {}).get("front", {}).get("counsel_review", {})
        if counsel.get("status") != "approved":
            extra["breach_review"] = ("counsel has reviewed only part of us-breach-notification.md (" + counsel.get("scope", "") + "); confirm the state rules relied on here"
                                      if counsel.get("status") == "partial" else "counsel hasn't reviewed us-breach-notification.md; confirm every state rule relied on here")
    if rec.type == "vr":
        from gov.vendor_items import item_text
        extra["item_text"] = item_text(root)
    if rec.type == "ropa":
        extra.update(vendors=derive.vendor_slugs(rec.data), required=required_rows(root, rec.data))
    text = template.render(r=rec.data, d=derive.DERIVE[rec.type](rec.data), source_file=rec.path.name, **extra)
    return _tidy(text)


def render_index(record_type: str, records: list) -> str:
    rows = [
        {"r": rec.data, "d": derive.DERIVE[record_type](rec.data), "file": rec.markdown_path.name}
        for rec in sorted(records, key=lambda r: r.id)
    ]
    template = _env().get_template(f"{record_type}-index.md.j2")
    text = template.render(
        rows=rows,
        approved=sum(1 for row in rows if row["r"]["status"].startswith("Approved")),
        tbc=sum(row["d"].get("required_tbc", 0) for row in rows),
    )
    return _tidy(text)


@dataclass
class RenderResult:
    written: list
    stale: list
    problems: list


def render_tree(root: Path, check: bool = False) -> RenderResult:
    """Render every record and index. With check, write nothing and report drift."""
    problems = [p for p in validate_tree(root) if p.level == "error"]
    if problems:
        return RenderResult([], [], problems)

    outputs = {}
    by_type = {}
    for path in record_files(root):
        rec = load(path)
        outputs[rec.markdown_path] = render_record(rec, root)
        if rec.type == "inc" and rec.data.get("notices"):
            outputs[rec.path.parent / "notices" / f"{rec.path.stem}-notices.md"] = _tidy(
                _env().get_template("inc-notices.md.j2").render(r=rec.data, source_file=rec.path.name))
        if rec.type == "dsr" and rec.data.get("messages"):
            outputs[rec.path.parent / "drafts" / f"{rec.path.stem}-drafts.md"] = _tidy(
                _env().get_template("dsr-drafts.md.j2").render(r=rec.data, source_file=rec.path.name))
        if rec.type == "vr" and rec.data.get("requests"):
            outputs[rec.path.parent / "requests" / f"{rec.path.stem}-requests.md"] = _tidy(
                _env().get_template("vr-requests.md.j2").render(r=rec.data, source_file=rec.path.name))
        by_type.setdefault(rec.type, []).append(rec)
    for record_type, spec in ids.managed_types().items():
        folder = output_root(root) / spec["folder"]
        if folder.is_dir() or by_type.get(record_type):
            outputs[folder / "index.md"] = render_index(record_type, by_type.get(record_type, []))
    from gov import references
    readme = references.readme(root)
    if readme is not None:
        outputs[root / references.INDEX] = readme

    written, stale = [], []
    for path, text in sorted(outputs.items()):
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        if check:
            stale.append(_rel(root, path))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            written.append(_rel(root, path))
    return RenderResult(written, stale, [])


def _tidy(text: str) -> str:
    """Collapse runs of blank lines left by conditional blocks."""
    lines, blank = [], False
    for line in text.splitlines():
        if not line.strip():
            if not blank and lines:
                lines.append("")
            blank = True
        else:
            lines.append(line.rstrip())
            blank = False
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines) + "\n"


__all__ = ["render_record", "render_index", "render_tree", "RenderResult", "Problem"]
