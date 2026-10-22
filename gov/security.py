"""Security assessment elements by kind, from rules/security.yaml."""
from __future__ import annotations

from functools import lru_cache

from gov import yamlio
from gov.paths import PACKAGE


@lru_cache(maxsize=None)
def kinds() -> dict:
    return yamlio.load(PACKAGE / "rules" / "security.yaml")["kinds"]


def elements(kind: str) -> dict:
    """{element id: {"label", "cite"}} in the order the law lists them."""
    return {e["id"]: e for e in kinds()[kind]["elements"]}
