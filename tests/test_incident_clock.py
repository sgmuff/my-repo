"""gov clock: the one command that reasons about time zones. Every expected time here is worked out by hand in UTC."""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def clock(*args):
    return subprocess.run([sys.executable, "-m", "gov", "clock", *args], capture_output=True, text=True, cwd=REPO)


def rows(*args):
    result = clock(*args)
    assert result.returncode == 0, result.stderr
    return result.stdout.splitlines()


def due(lines, regime):
    return [line for line in lines if f" {regime} " in f" {line} "]


def test_72_hours_in_utc():
    assert due(rows("--aware", "2026-10-16T09:30", "--regimes", "gdpr"), "GDPR")[0].startswith("2026-10-19 09:30 UTC")


def test_spring_forward_inside_the_window_counts_elapsed_hours():
    # 10:00 CET is 09:00 UTC; plus 72 hours is 09:00 UTC on 30 March, which is 11:00 CEST.
    lines = rows("--aware", "2026-03-27T10:00", "--tz", "Europe/Berlin", "--regimes", "gdpr")
    assert due(lines, "GDPR")[0].startswith("2026-03-30 11:00 CEST")


def test_fall_back_inside_the_window_isnt_an_hour_late():
    # 18:00 BST is 17:00 UTC; plus 72 hours is 17:00 UTC on 26 October, which is 17:00 GMT, not 18:00.
    lines = rows("--aware", "2026-10-23T18:00", "--tz", "Europe/London", "--regimes", "uk")
    assert due(lines, "UK GDPR")[0].startswith("2026-10-26 17:00 GMT")


def test_a_time_that_happens_twice_uses_the_earlier_one_and_says_so():
    # 01:30 EDT is 05:30 UTC; plus 72 hours is 05:30 UTC on 4 November, which is 00:30 EST.
    lines = rows("--aware", "2026-11-01T01:30", "--tz", "America/New_York", "--regimes", "gdpr")
    assert any("happens twice" in line for line in lines)
    assert due(lines, "GDPR")[0].startswith("2026-11-04 00:30 EST")


def test_a_time_that_doesnt_exist_is_rejected():
    result = clock("--aware", "2026-03-29T02:30", "--tz", "Europe/Berlin", "--regimes", "gdpr")
    assert result.returncode != 0
    assert "doesn't exist" in result.stderr


def test_friday_evening_discovery_runs_through_the_weekend():
    # GDPR's 72 hours are calendar hours: Friday 18:00 runs to Monday 18:00, with no weekend extension.
    lines = rows("--aware", "2026-10-16T18:00", "--tz", "Europe/Dublin", "--regimes", "gdpr")
    assert due(lines, "GDPR")[0].startswith("2026-10-19 18:00 IST")


def test_an_explicit_offset_overrides_tz():
    lines = rows("--aware", "2026-10-16T09:30+02:00", "--tz", "America/New_York", "--regimes", "gdpr")
    assert due(lines, "GDPR")[0].startswith("2026-10-19 09:30 UTC+02:00")


def test_state_days_run_from_the_discovery_date():
    lines = rows("--aware", "2026-10-16T23:30", "--tz", "America/Los_Angeles", "--states", "TX", "WA")
    assert due(lines, "TX")[0].startswith("2026-11-15")  # regulator, 30 days
    assert any(line.startswith("2026-12-15") for line in due(lines, "TX"))  # individuals, 60 days
    assert any(line.startswith("2026-11-15") for line in due(lines, "WA"))


def test_iowa_counts_business_days_from_individual_notice():
    # Notice on Friday 23 October; five business days ends Friday 30 October.
    lines = rows("--aware", "2026-10-01T09:00", "--states", "IA", "--individual-notice", "2026-10-23")
    assert due(lines, "IA")[0].startswith("2026-10-30")
    # Notice on Thursday 29 October; the weekend is skipped, so it ends Thursday 5 November.
    lines = rows("--aware", "2026-10-01T09:00", "--states", "IA", "--individual-notice", "2026-10-29")
    assert due(lines, "IA")[0].startswith("2026-11-05")


def test_notice_based_deadlines_need_the_notice_date():
    lines = rows("--aware", "2026-10-01T09:00", "--states", "CA")
    assert any("pass --individual-notice" in line for line in due(lines, "CA"))
    lines = rows("--aware", "2026-10-01T09:00", "--states", "CA", "--individual-notice", "2026-10-20")
    assert any(line.startswith("2026-11-04") for line in due(lines, "CA"))


def test_rows_are_in_deadline_order_with_open_ones_last():
    lines = rows("--aware", "2026-10-16T09:30", "--tz", "America/New_York", "--regimes", "gdpr", "ny2d", "sec", "--states", "CA")
    table = [line for line in lines[1:] if line and line[0] in "2n"]
    dated = [line[:10] for line in table if line[0] == "2"]
    assert dated == sorted(dated)
    assert table.index(next(line for line in table if line.startswith("no fixed date"))) == len(dated)


def test_bad_input_fails_clearly():
    assert "Unknown time zone" in clock("--aware", "2026-10-16T09:30", "--tz", "Mars/Olympus", "--regimes", "gdpr").stderr
    assert "--aware must be" in clock("--aware", "16/10/2026", "--regimes", "gdpr").stderr
    assert "Nothing to compute" in clock("--aware", "2026-10-16T09:30").stderr
