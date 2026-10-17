#!/usr/bin/env python3
"""Compute data subject request deadlines.

Usage:
  python3 deadlines.py <received YYYY-MM-DD> <regime> [<regime> ...]

Regimes: gdpr, uk, fadp, ccpa, ccpa-optout, state, iowa, ferpa

Prints each deadline in YYYY-MM-DD form. Weekends are handled; public
holidays are not, so check them by hand (the output says so). The rules
come from _shared/references/dsr-matrix.md, section 3.
"""
import calendar
import datetime as dt
import sys


def add_months(d, months):
    m = d.month - 1 + months
    y = d.year + m // 12
    m = m % 12 + 1
    day = min(d.day, calendar.monthrange(y, m)[1])
    return dt.date(y, m, day)


def next_working_day(d):
    while d.weekday() >= 5:
        d += dt.timedelta(days=1)
    return d


def add_business_days(d, n):
    while n > 0:
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def rules(received):
    r = received
    return {
        "gdpr": [
            ("Respond (one month, Art. 12(3))", next_working_day(add_months(r, 1))),
            ("Latest date to tell the person about an extension", next_working_day(add_months(r, 1))),
            ("Respond if extended (three months in total)", next_working_day(add_months(r, 3))),
        ],
        "uk": [
            ("Respond (one month; may pause for clarification, verify commencement)", next_working_day(add_months(r, 1))),
            ("Respond if extended (three months in total)", next_working_day(add_months(r, 3))),
        ],
        "fadp": [
            ("Respond (30 days, DPO Art. 18)", r + dt.timedelta(days=30)),
        ],
        "ccpa": [
            ("Acknowledge (10 business days, CCPA Regs. § 7021)", add_business_days(r, 10)),
            ("Respond (45 calendar days)", r + dt.timedelta(days=45)),
            ("Respond if extended (90 calendar days in total)", r + dt.timedelta(days=90)),
        ],
        "ccpa-optout": [
            ("Apply opt-out or limit request (15 business days, CCPA Regs. §§ 7026, 7027)", add_business_days(r, 15)),
        ],
        "state": [
            ("Respond (45 days, most states)", r + dt.timedelta(days=45)),
            ("Respond if extended (90 days in total)", r + dt.timedelta(days=90)),
        ],
        "iowa": [
            ("Respond (90 days, verify)", r + dt.timedelta(days=90)),
        ],
        "ferpa": [
            ("Respond (45 days, 34 CFR § 99.10(b))", r + dt.timedelta(days=45)),
        ],
    }


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    try:
        received = dt.date.fromisoformat(argv[1])
    except ValueError:
        sys.exit("Received date must be YYYY-MM-DD")
    table = rules(received)
    unknown = [x for x in argv[2:] if x not in table]
    if unknown:
        sys.exit(f"Unknown regime(s): {', '.join(unknown)}. Use: {', '.join(table)}")
    rows = []
    for regime in argv[2:]:
        for label, due in table[regime]:
            rows.append((due, regime, label))
    rows.sort()
    print(f"Received: {received.isoformat()} ({received.strftime('%A')})")
    for due, regime, label in rows:
        print(f"{due.isoformat()}  {due.strftime('%a')}  {regime:12} {label}")
    print("Earliest substantive deadline:", min(d for d, _, l in rows if "Respond" in l or "Apply" in l).isoformat())
    print("Note: public holidays aren't applied. Check them for each date, and for GDPR move a deadline that falls on one to the next working day.")


if __name__ == "__main__":
    main(sys.argv)
