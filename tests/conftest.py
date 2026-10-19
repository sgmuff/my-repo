import os
import shutil
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
UPDATE = os.environ.get("UPDATE_GOLDEN") == "1"


@pytest.fixture
def root(tmp_path, monkeypatch):
    """An empty suite: the marker file and nothing else."""
    (tmp_path / "skills" / "_shared").mkdir(parents=True)
    shutil.copy(REPO / "skills" / "_shared" / "company-profile.md", tmp_path / "skills" / "_shared")
    shutil.copytree(REPO / "skills" / "_shared" / "references", tmp_path / "skills" / "_shared" / "references")
    monkeypatch.delenv("GOV_ROOT", raising=False)
    return tmp_path


@pytest.fixture
def ropa_root(root):
    """A suite holding the Gradebook Sync fixture, with its ID issued."""
    from gov import ids

    folder = root / "compliance" / "registers" / "ropa"
    folder.mkdir(parents=True)
    shutil.copy(FIXTURES / "ropa" / "ROPA-0001-gradebook-sync.yaml", folder)
    assert ids.next_id(root, "ROPA") == "ROPA-0001"
    return root


def golden(path: Path, actual: str) -> None:
    """Compare with a stored output. UPDATE_GOLDEN=1 rewrites it."""
    if UPDATE or not path.exists():
        path.write_text(actual, encoding="utf-8")
    assert actual == path.read_text(encoding="utf-8"), f"{path.name} differs; rerun with UPDATE_GOLDEN=1 if intended"


@pytest.fixture
def assess_root(ropa_root):
    """The RoPA fixture plus the LIA and TIA fixtures, with their IDs issued."""
    from gov import ids

    for kind in ("lia", "tia"):
        folder = ropa_root / "compliance" / "assessments" / kind
        folder.mkdir(parents=True)
        for path in (FIXTURES / kind).glob("*.yaml"):
            shutil.copy(path, folder)
        ids.next_id(ropa_root, kind.upper(), "2026")
    return ropa_root
