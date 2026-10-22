"""The shared risk matrix (skills/_shared/references/risk-method.md, section 3). Ratings are computed, never typed.
Overall residual risk is the highest rating in the register, never an average."""
from __future__ import annotations

MATRIX = {
    "probable": {"minimal": "Medium", "significant": "High", "severe": "High"},
    "possible": {"minimal": "Low", "significant": "Medium", "severe": "High"},
    "remote": {"minimal": "Low", "significant": "Low", "severe": "Medium"},
}
ORDER = {"Low": 1, "Medium": 2, "High": 3}


def rate(level: dict) -> str:
    """Low, Medium, High, or TBC if either input is TBC."""
    if "TBC" in (level["likelihood"], level["severity"]):
        return "TBC"
    return MATRIX[level["likelihood"]][level["severity"]]


def overall(risks: list, stage: str) -> str:
    """The highest rating at one stage (inherent, current, or target). TBC if any rating is TBC and none is High."""
    ratings = [rate(r[stage]) for r in risks]
    if not ratings:
        return "TBC"
    if "High" in ratings:
        return "High"
    if "TBC" in ratings:
        return "TBC"
    return max(ratings, key=ORDER.get)


def lower(a: str, b: str) -> bool:
    """True if rating a is below rating b; False when either is TBC."""
    return a in ORDER and b in ORDER and ORDER[a] < ORDER[b]
