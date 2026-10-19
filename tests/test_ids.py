import pytest

from gov import ids


def test_ids_count_up_and_never_reuse(root):
    assert ids.next_id(root, "ROPA") == "ROPA-0001"
    assert ids.next_id(root, "ROPA") == "ROPA-0002"
    # Nothing tracks deletions, so a deleted record's number stays used.
    assert ids.next_id(root, "ROPA") == "ROPA-0003"


def test_yearly_ids_count_per_year(root):
    assert ids.next_id(root, "DPIA", "2026") == "DPIA-2026-001"
    assert ids.next_id(root, "DPIA", "2026") == "DPIA-2026-002"
    assert ids.next_id(root, "DPIA", "2027") == "DPIA-2027-001"


def test_year_rules(root):
    with pytest.raises(ids.IdError):
        ids.next_id(root, "DPIA")
    with pytest.raises(ids.IdError):
        ids.next_id(root, "ROPA", "2026")
    with pytest.raises(ids.IdError):
        ids.next_id(root, "NOPE")


def test_parse_and_find():
    assert ids.parse_id("DPIA-2026-004") == ("DPIA", "2026", 4)
    assert ids.parse_id("ROPA-0042") == ("ROPA", None, 42)
    assert ids.parse_id("ROPA-42") is None
    assert ids.parse_id("DPIA-004") is None
    assert ids.find_ids("See VR-2026-007 and ROPA-0001; not LR-2026-Q3.") == ["VR-2026-007", "ROPA-0001"]
