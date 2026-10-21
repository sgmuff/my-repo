from conftest import FIXTURES

from gov import yamlio
from gov.cli import main
from gov.screen import rules, screen

ROPA = FIXTURES / "ropa" / "ROPA-0001-gradebook-sync.yaml"


def results(data):
    return {r["criterion"]: r for r in screen(data)["criteria"]}


def test_every_edpb_criterion_appears_once():
    assert [c["id"] for c in rules()["criteria"]] == list(range(1, 10))
    assert rules()["criteria"][8]["label"] == "Processing that blocks a right, service, or contract"


def test_the_gradebook_fixture_suggests_four_and_asks_five():
    out = screen(yamlio.load(ROPA))
    assert out["status"] == "Provisional" and (out["suggested"], out["ask"]) == (4, 5)
    r = results(yamlio.load(ROPA))
    assert {k for k, v in r.items() if v["result"] == "suggested"} == {1, 4, 7, 8}
    assert "data_categories: Support needs (special-category)" in r[4]["evidence"]
    assert "data_subjects: Students (vulnerable true)" in r[7]["evidence"]


def test_false_facts_suggest_nothing():
    data = yamlio.load(ROPA)
    data["ai_used"] = False
    data["us_flags"]["profiling"]["value"] = False
    data["us_flags"]["sensitive_data"]["value"] = False
    for c in data["data_categories"]:
        c["flags"] = []
    for s in data["data_subjects"]:
        s["vulnerable"]["value"] = False
    r = results(data)
    assert {k for k, v in r.items() if v["result"] == "suggested"} == set()
    assert {k for k, v in r.items() if v["result"] == "ask"} == {2, 3, 5, 6, 9}


def test_the_command_prints_a_provisional_table(capsys, monkeypatch, root):
    monkeypatch.setenv("GOV_ROOT", str(root))
    assert main(["screen", str(ROPA)]) == 0
    out = capsys.readouterr().out
    assert "(Provisional)" in out and "| 8 | Innovative use of technology | Suggested | ai_used: true |" in out
    assert "the screening record decides" in out


def test_the_command_rejects_other_records(capsys, monkeypatch, root):
    monkeypatch.setenv("GOV_ROOT", str(root))
    assert main(["screen", str(FIXTURES / "lia" / "LIA-2026-001-lead-scoring.yaml")]) == 2
