"""Issues an assessment must address, from rules/issues.yaml. Each triggered issue the record doesn't cover is a finding."""
from __future__ import annotations

import re
from functools import lru_cache

from gov import yamlio
from gov.paths import PACKAGE

KIND_REGIME = {"eu-tia": "eu-gdpr", "uk-tra": "uk-gdpr", "ch-tia": "ch-fadp"}
CONDITIONS = {"types", "kinds", "context", "regimes", "countries", "special_category", "routes"}


class IssueRulesError(ValueError):
    pass


@lru_cache(maxsize=None)
def rules() -> dict:
    data = yamlio.load(PACKAGE / "rules" / "issues.yaml")
    check_rules(data)
    return data


def check_rules(data: dict) -> None:
    tags = set(data["context_tags"])
    for issue_id, issue in data["issues"].items():
        for key in ("label", "ask", "cite", "when"):
            if not issue.get(key):
                raise IssueRulesError(f"{issue_id}: missing {key}")
        unknown = set(issue["when"]) - CONDITIONS
        if unknown:
            raise IssueRulesError(f"{issue_id}: unknown condition {sorted(unknown)}")
        bad = set(issue["when"].get("context", [])) - tags
        if bad:
            raise IssueRulesError(f"{issue_id}: unknown context tag {sorted(bad)}")


def _regimes(data: dict) -> set:
    if data.get("regimes"):
        return set(data["regimes"])
    return {KIND_REGIME[data["kind"]]} if data.get("kind") in KIND_REGIME else set()


def _country_matches(names: list, data: dict) -> bool:
    """True if any listed name appears as a whole word in the importer's country, such as "India (Pune)"."""
    country = str((data.get("importer") or {}).get("country", "")).lower()
    return any(re.search(r"(?<![a-z])" + re.escape(name.lower()) + r"(?![a-z])", country) for name in names)


def _special_category(data: dict):
    call = data.get("special_category") or (data.get("transfer_map") or {}).get("special_category")
    return call["value"] if isinstance(call, dict) else None


def _matches(when: dict, data: dict) -> bool:
    if "types" in when and data.get("type") not in when["types"]:
        return False
    if "kinds" in when and data.get("kind") not in when["kinds"]:
        return False
    if "context" in when and not set(when["context"]) & set(data.get("context", [])):
        return False
    if "regimes" in when and not set(when["regimes"]) & _regimes(data):
        return False
    if "countries" in when and not _country_matches(when["countries"], data):
        return False
    if "routes" in when and (data.get("mechanism") or {}).get("route") not in when["routes"]:
        return False
    if when.get("special_category") == "possible" and _special_category(data) is False:
        return False
    return True


def triggered(data: dict) -> list:
    """(issue id, rule) pairs that apply to this record, in rules-file order."""
    return [(i, r) for i, r in rules()["issues"].items() if _matches(r["when"], data)]


def missing(data: dict) -> list:
    """(pointer, message) findings for triggered issues the record doesn't cover."""
    covered = {i["issue"] for i in data.get("issues", [])}
    return [
        (f"issues/{issue_id}", f"address {rule['label'].lower()} ({issue_id}): {rule['ask']} ({rule['cite']})")
        for issue_id, rule in triggered(data)
        if issue_id not in covered
    ]


def unknown(data: dict) -> list:
    known = set(rules()["issues"])
    return [i["issue"] for i in data.get("issues", []) if i["issue"] not in known]


def rows(data: dict) -> list:
    """Rendered issue table: every triggered issue, then any extra the record lists."""
    listed = {i["issue"]: i for i in data.get("issues", [])}
    out, seen = [], set()
    for issue_id, rule in triggered(data):
        seen.add(issue_id)
        entry = listed.get(issue_id)
        out.append({"label": rule["label"], "cite": rule["cite"],
                    "status": entry["status"] if entry else "not-addressed",
                    "note": entry["note"] if entry else rule["ask"]})
    for issue_id, entry in listed.items():
        if issue_id not in seen and issue_id in rules()["issues"]:
            rule = rules()["issues"][issue_id]
            out.append({"label": rule["label"], "cite": rule["cite"], "status": entry["status"], "note": entry["note"]})
    return out
