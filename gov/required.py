"""`gov required`: the assessments an activity owes, from the catalog and the activity's facts."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from gov import derive, yamlio
from gov.paths import PACKAGE
from gov.route import table as routing_table

TBC = "TBC"
STATUSES = ("owed", "tbc", "not-yet-applicable", "no-reference")
GATES = ("law", "policy", "risk")


class CatalogError(Exception):
    pass


@lru_cache(maxsize=None)
def catalog() -> dict:
    data = yamlio.load(PACKAGE / "rules" / "assessments.yaml")
    check_catalog(data)
    return data


def vocabulary(data: dict | None = None) -> dict:
    """Facts the catalog can use: routing.yaml's, plus its own."""
    data = data or catalog()
    facts = dict(routing_table()["facts"])
    for key, spec in data.get("facts", {}).items():
        if key in facts:
            raise CatalogError(f"fact {key} is already declared in routing.yaml")
        facts[key] = spec
    return facts


def check_catalog(data: dict) -> None:
    facts = vocabulary(data)
    seen = set()
    for entry in data["entries"]:
        eid = entry["id"]
        if eid in seen:
            raise CatalogError(f"entry {eid} appears twice")
        seen.add(eid)
        for key in ("name", "citation", "owed_by", "gate", "applies_from", "produced_by", "reference"):
            if not entry.get(key):
                raise CatalogError(f"entry {eid} has no {key}")
        if entry["gate"] not in GATES:
            raise CatalogError(f"entry {eid}: gate must be one of {', '.join(GATES)}")
        if not (entry.get("when") or entry.get("when_any")):
            raise CatalogError(f"entry {eid} has no trigger")
        for key, want in {**entry.get("when", {}), **entry.get("when_any", {})}.items():
            if key not in facts:
                raise CatalogError(f"entry {eid} uses undeclared fact {key}")
            spec = facts[key]
            for value in want if isinstance(want, list) else [want]:
                if spec["type"] == "boolean" and not isinstance(value, bool):
                    raise CatalogError(f"entry {eid}: {key} takes true or false")
                if spec["type"] == "enum" and value not in spec["values"]:
                    raise CatalogError(f"entry {eid}: {key} has no value {value!r}")


def evaluate(facts: dict, as_of: str, root: Path | None = None) -> list:
    """Every catalog entry that applies or might apply, in catalog order. Facts not given are TBC."""
    declared = vocabulary()
    unknown = sorted(set(facts) - set(declared))
    if unknown:
        raise CatalogError(f"unknown facts: {', '.join(unknown)}")
    refs = (root / "skills" / "_shared" / "references") if root else None
    results = []
    for entry in catalog()["entries"]:
        state, open_facts = _evaluate(entry, facts)
        if state is False:
            continue
        if refs is not None and not (refs / entry["reference"]).is_file():
            status, reason = "no-reference", f"{entry['reference']} doesn't exist yet; add it before this entry applies"
        elif entry["applies_from"] > as_of:
            status, reason = "not-yet-applicable", f"applies from {entry['applies_from']}"
        elif state is None:
            status, reason = "tbc", "depends on " + ", ".join(open_facts)
        else:
            status, reason = "owed", "triggered by " + ", ".join(_matched(entry, facts))
        results.append({
            "assessment": entry["id"],
            "name": entry["name"],
            "citation": entry["citation"],
            "gate": entry["gate"],
            "produced_by": entry["produced_by"],
            "status": status,
            "reason": reason,
            "open_facts": open_facts if state is None else [],
        })
    return results


def entry(assessment_id: str) -> dict:
    for e in catalog()["entries"]:
        if e["id"] == assessment_id:
            return e
    raise KeyError(assessment_id)


def facts_from_ropa(data: dict) -> dict:
    """The catalog facts a RoPA entry settles. Everything else stays TBC."""
    d = derive.ropa(data)
    transfers = data["transfers"]
    facts = {
        "new_processing": True,
        "company_role": d["record_type"] if d["record_type"] in ("controller", "processor", "both") else TBC,
        "special_category": d["special_category"],
        "children_or_students": d["children_or_students"],
        "profiling": data["us_flags"]["profiling"]["value"],
        "ai_involved": data["ai_used"],
        "cross_border_access": d["restricted_transfers"],
    }
    bases = sorted({p["lawful_basis"]["value"] for p in data["purposes"]} - {TBC, "controller-to-confirm", "not-applicable"})
    if bases:
        facts["lawful_basis"] = bases
    elif all(p["lawful_basis"]["value"] in ("controller-to-confirm", "not-applicable") for p in data["purposes"]):
        facts["lawful_basis"] = "not-proposed"
    if isinstance(transfers, list):
        mechanisms = sorted({t["mechanism"] for t in transfers} - {TBC})
        if mechanisms:
            facts["transfer_mechanism"] = mechanisms
        regimes = {t["regime"] for t in transfers}
        if "eu-gdpr" in regimes:
            facts["eu_people"] = True
        if "uk-gdpr" in regimes:
            facts["uk_people"] = True
        if "ch-fadp" in regimes:
            facts["ch_people"] = True
    return {k: v for k, v in facts.items() if v != TBC}


def _evaluate(item: dict, facts: dict):
    """(True | False | None, open facts). None means it depends on facts still TBC."""
    open_facts = []
    if item.get("when"):
        for key, want in item["when"].items():
            result = _match(facts.get(key, TBC), want)
            if result is False:
                return False, []
            if result is None:
                open_facts.append(key)
    if item.get("when_any"):
        results = {k: _match(facts.get(k, TBC), w) for k, w in item["when_any"].items()}
        if not any(r is True for r in results.values()):
            if all(r is False for r in results.values()):
                return False, []
            open_facts += [k for k, r in results.items() if r is None]
    return (None, open_facts) if open_facts else (True, [])


def _matched(item: dict, facts: dict) -> list:
    conditions = {**item.get("when", {}), **item.get("when_any", {})}
    return [k for k, w in conditions.items() if _match(facts.get(k, TBC), w) is True]


def _match(value, want):
    if value == TBC:
        return None
    wanted = want if isinstance(want, list) else [want]
    values = value if isinstance(value, list) else [value]
    return any(v in wanted for v in values)


def to_markdown(results: list) -> str:
    if not results:
        return "No catalog entry applies to these facts.\n"
    lines = ["| Assessment | Law | Gate | Status | Why | Produced by |", "|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['name']} | {r['citation']} | {r['gate'].capitalize()} | {r['status']} | {r['reason']} | `{r['produced_by']}` |")
    return "\n".join(lines) + "\n"
