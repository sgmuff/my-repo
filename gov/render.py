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
    env.filters.update(cell=cell, yn=yn, label=label, src=src, join_or_tbc=join_or_tbc, flags=flags, call=call)
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
    extra = {"findings": finding_rows(rec, root), "method": method,
             "issue_rows": issues.rows(rec.data) if rec.type != "ropa" else []}
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
        by_type.setdefault(rec.type, []).append(rec)
    for record_type, spec in ids.managed_types().items():
        folder = output_root(root) / spec["folder"]
        if folder.is_dir() or by_type.get(record_type):
            outputs[folder / "index.md"] = render_index(record_type, by_type.get(record_type, []))

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
