"""Compute breach notification clocks.

Usage:
  gov clock --aware 2026-10-16T09:30 [--tz America/New_York]
                            [--regimes gdpr uk fadp nydfs ny2d sec ftc-glba]
                            [--states CA NY TX ...]
                            [--individual-notice YYYY-MM-DD]

--aware   when the company became aware (GDPR) or discovered the breach (US
          states), as YYYY-MM-DDTHH:MM in the given time zone (default UTC).
--individual-notice   date individual notices went or will go out; needed for
          regulator deadlines that run from it (California, Iowa, Louisiana,
          Oklahoma). Omit it and those rows say so.

Deadlines come from _shared/references/us-breach-notification.md (section 2)
and gdpr.md (section 9). Every state row there is Provisional until counsel's
review is recorded; this script inherits that status. States without a fixed
deadline print the statutory standard instead of a date. Public holidays are
not applied.

Hour-based clocks (GDPR's 72 hours) count elapsed time, so a daylight saving
change inside the window moves the local time shown. A local --aware time
that doesn't exist (clocks went forward) is rejected; one that happens twice
(clocks went back) is read as the earlier instant, and the output says so.
"""
import argparse
import datetime as dt
import sys

try:
    from zoneinfo import ZoneInfo
except ImportError:  # Python < 3.9
    ZoneInfo = None

# Fixed individual-notice deadlines, in calendar days from discovery.
STATE_INDIVIDUAL_DAYS = {
    "AL": 45, "AZ": 45, "CA": 30, "CO": 30, "CT": 60, "DE": 60, "FL": 30, "IN": 45,
    "LA": 60, "ME": 30, "MD": 45, "NM": 45, "NY": 30, "OH": 45, "OR": 45, "RI": 45,
    "SD": 60, "TN": 45, "TX": 60, "VT": 45, "WA": 30, "WI": 45,
}
# Regulator deadlines in calendar days from discovery.
STATE_REGULATOR_FROM_DISCOVERY = {
    "AL": (45, ">1,000"), "AZ": (45, ">1,000"), "AR": (45, ">1,000"), "CO": (30, ">=500"),
    "FL": (30, ">=500"), "NM": (45, ">1,000"), "TX": (30, ">=250"), "WA": (30, ">500"),
}
# Regulator deadlines that run from the individual notice date.
STATE_REGULATOR_FROM_NOTICE = {
    "CA": (15, ">500", "calendar"), "IA": (5, ">500", "business"),
    "LA": (10, "any", "calendar"), "OK": (60, ">=500", "calendar"),
}
STATE_REGULATOR_TEXT = {
    "CT": "Not later than individual notice", "DE": "Not later than individual notice (>500)",
    "DC": "Not later than individual notice (>=50)", "IL": "Not later than individual notice (>500)",
    "MD": "Before individual notice", "NE": "Not later than individual notice",
    "NJ": "State Police, before individual notice", "PR": "Within 10 days of detection (verify)",
    "MT": "At the same time as individual notice", "PA": "At the same time as individual notice (>500, verify)",
    "NY": "AG, Department of State, State Police (with individual notice)",
    "MA": "AG and OCABR, any breach", "NC": "Any breach", "VA": "Any breach", "IN": "Any breach",
    "NH": "Any breach", "ME": "Any breach", "OR": "If >250", "ND": "If >250", "SD": "If >250",
    "RI": "If >500", "MO": "If >1,000", "SC": "If >1,000 (Consumer Affairs)", "HI": "If >1,000 (OCP)",
    "UT": "If >=500 (AG and Utah Cyber Center, verify)",
}


def parse_aware(s, tz):
    """The awareness time, and a note if the local time was ambiguous."""
    try:
        naive = dt.datetime.fromisoformat(s)
    except ValueError:
        sys.exit("--aware must be YYYY-MM-DDTHH:MM")
    if naive.tzinfo:
        return naive, None
    if ZoneInfo is None:
        if tz != "UTC":
            sys.exit("Time zones need Python 3.9 or later; pass --aware with a UTC offset instead")
        return naive.replace(tzinfo=dt.timezone.utc), None
    try:
        zone = ZoneInfo(tz)
    except Exception:
        sys.exit(f"Unknown time zone: {tz}")
    first, second = naive.replace(tzinfo=zone, fold=0), naive.replace(tzinfo=zone, fold=1)
    if first.astimezone(dt.timezone.utc).astimezone(zone).replace(tzinfo=None) != naive:
        sys.exit(f"{s} doesn't exist in {tz} (the clocks went forward); check the time and pass it again")
    if first.utcoffset() != second.utcoffset():
        return first, f"{s} happens twice in {tz} (the clocks went back); using the earlier one. Confirm which it was."
    return first, None


def add_business_days(d, n):
    while n > 0:
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def main(argv=None):
    ap = argparse.ArgumentParser(prog="gov clock", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--aware", required=True)
    ap.add_argument("--tz", default="UTC")
    ap.add_argument("--regimes", nargs="*", default=[])
    ap.add_argument("--states", nargs="*", default=[])
    ap.add_argument("--individual-notice")
    a = ap.parse_args(argv)

    aware, note = parse_aware(a.aware, a.tz)
    day0 = aware.date()
    rows = []  # (sort_key, due_text, regime, duty)

    def at(delta, regime, duty):
        due = (aware.astimezone(dt.timezone.utc) + delta).astimezone(aware.tzinfo)
        rows.append((due, due.strftime("%Y-%m-%d %H:%M %Z").strip(), regime, duty))

    def on(date, regime, duty):
        due = dt.datetime.combine(date, dt.time(23, 59), tzinfo=aware.tzinfo)
        rows.append((due, date.isoformat(), regime, duty))

    def text(regime, duty):
        rows.append((dt.datetime.max.replace(tzinfo=aware.tzinfo), "no fixed date", regime, duty))

    reg = {r.lower() for r in a.regimes}
    if "gdpr" in reg:
        at(dt.timedelta(hours=72), "GDPR", "Notify the lead supervisory authority, unless unlikely to result in a risk (Art. 33(1)); phased reporting allowed (Art. 33(4))")
        text("GDPR", "Notify individuals without undue delay if likely high risk (Art. 34)")
    if "uk" in reg:
        at(dt.timedelta(hours=72), "UK GDPR", "Notify the Information Commission, unless unlikely to result in a risk")
    if "fadp" in reg:
        text("FADP", "Notify the FDPIC as soon as possible if likely high risk (Art. 24)")
    if "nydfs" in reg:
        at(dt.timedelta(hours=72), "NYDFS", "Notify DFS (23 NYCRR 500.17), covered entities only")
    if "ny2d" in reg:
        on(day0 + dt.timedelta(days=7), "NY Ed Law 2-d", "Notify each educational agency (8 NYCRR 121.10(a))")
    if "sec" in reg:
        text("SEC 8-K 1.05", "Within 4 business days of determining the incident is material (clock runs from the materiality determination)")
    if "ftc-glba" in reg:
        on(day0 + dt.timedelta(days=30), "FTC Safeguards Rule", "Notify the FTC if >=500 consumers' unencrypted data (16 CFR 314.4(j))")

    notice = None
    if a.individual_notice:
        try:
            notice = dt.date.fromisoformat(a.individual_notice)
        except ValueError:
            sys.exit("--individual-notice must be YYYY-MM-DD")

    for s in [x.upper() for x in a.states]:
        if s in STATE_INDIVIDUAL_DAYS:
            on(day0 + dt.timedelta(days=STATE_INDIVIDUAL_DAYS[s]), s, f"Notify residents (outer limit {STATE_INDIVIDUAL_DAYS[s]} days; most expedient time possible applies first)")
        else:
            text(s, "Notify residents in the most expedient time possible, without unreasonable delay")
        if s in STATE_REGULATOR_FROM_DISCOVERY:
            days, thr = STATE_REGULATOR_FROM_DISCOVERY[s]
            on(day0 + dt.timedelta(days=days), s, f"Notify the regulator if {thr} residents")
        elif s in STATE_REGULATOR_FROM_NOTICE:
            days, thr, kind = STATE_REGULATOR_FROM_NOTICE[s]
            if notice:
                due = add_business_days(notice, days) if kind == "business" else notice + dt.timedelta(days=days)
                on(due, s, f"Notify the regulator if {thr} residents ({days} {kind} days after individual notice)")
            else:
                text(s, f"Notify the regulator if {thr} residents, {days} {kind} days after individual notice (pass --individual-notice)")
        elif s in STATE_REGULATOR_TEXT:
            text(s, "Regulator: " + STATE_REGULATOR_TEXT[s])

    if not rows:
        sys.exit("Nothing to compute: pass --regimes and/or --states")
    rows.sort(key=lambda r: r[0])
    print(f"Aware or discovered: {aware.strftime('%Y-%m-%d %H:%M %Z')} (working deadlines until this time is confirmed)")
    if note:
        print(note)
    for _, due, regime, duty in rows:
        print(f"{due:22} {regime:20} {duty}")
    print("\nAll rows are Provisional: state rows depend on us-breach-notification.md, which needs counsel review before live use.")
    print("Contractual deadlines (customer DPAs, district agreements, cyber insurance) aren't included. Add them from the contracts.")
    print("These are outer limits, not targets: set internal milestones (decision review, filing buffer) before each one.")

