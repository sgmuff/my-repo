# Key risk indicators

Pick 6 to 8 that fit the program's stage and the audience. Thresholds below are starting points. Set the company's own with the privacy lead, record them in the report's appendix, and keep them stable across periods so the trend means something.

| KRI | From `program_metrics.py` | Starting threshold (amber / red) | Why leadership cares |
|---|---|---|---|
| Open High current residual risks | §2 | Any open past its action due date / any older than 90 days | Unmitigated exposure the company is carrying now |
| Launch blockers past due | §3 | 1 / 3 or more | Product launches at risk, or launches going ahead without required controls |
| DSRs answered within the statutory deadline | §4 | Under 95% / under 85% | Statutory deadlines; regulators and plaintiffs look for patterns |
| DSRs open past deadline | §4 | 1 / 2 or more | Each may be a missed legal deadline (provisional until the deadline is confirmed) |
| Personal data breaches this period | §5 | Trend up / any notifiable to regulators | Notification cost, regulator scrutiny, customer trust |
| Vendors in use without a review | §6 | 1 / any processing sensitive or student data | Unassessed third-party risk, missing contract terms |
| Live high-tier AI systems without an assessment | §7 | Any / any making decisions about people | AI Act, state AI laws, and AIUC-1 readiness |
| Records past review | §3 | Over 10% / over 25% of a register | Registers going stale, so other numbers become unreliable |
| Controls evidenced (share implemented and evidenced) | §8 | Under 70% / under 50% | Shows whether controls work, not just exist |
| Regulatory changes open past due | §9 | 1 / any with an effective date within 90 days | Readiness for new obligations |

## Definitions

Record these in the report's appendix and keep them the same from period to period.

| KRI | Counts | Denominator |
|---|---|---|
| Open High current residual risks | Risk register rows rated High on verified controls only, in records not closed | Total open risk rows; give age of the oldest |
| Launch blockers past due | Open actions marked as launch blockers with a due date before period end | All open launch blockers |
| DSR statutory timeliness | Responses on or before the statutory deadline (extended deadline if a valid extension went out) | Cases whose deadline fell in the period |
| DSR internal target | Responses on or before `internal_target` | Cases with an internal target due in the period |
| Incidents | Security incidents logged; of those, personal data breaches (provisional or confirmed); of those, notified to a regulator | Shown as three nested counts |
| Vendors without a review | Vendors named in RoPA entries with no vendor review folder; flag those handling sensitive or student data | Vendors named in the RoPA |
| High-tier AI without assessment | AI inventory entries at Tier 1 with lifecycle live (deployed to staff, customers, or production) and no AI impact assessment | Live Tier 1 entries |
| Controls evidenced | Controls with operating status "implemented and evidenced" | All active controls in the library |

## Direction and status

- Show the previous value and an arrow or word (up, down, flat). Say whether up is good or bad for that KRI.
- Status is green, amber, or red against the threshold. Use words as well as color, so the report reads in plain text.
- Amber means off threshold with a named owner and a plan. Without both, it's red.
- A KRI with an incomplete source register is "not reliable this period," with the reason, not a number that looks reassuring.

## Wording risk for leadership

| Instead of | Write |
|---|---|
| "R1 is High (Probable × Significant)" | "Deletion requests from schools may fail because a nightly sync restores deleted student records. Rated High until the fix is tested (DPIA-2026-004, R1)." |
| "We are GDPR compliant" | "The 12 activities in the RoPA have documented lawful bases. 2 are overdue for review." |
| "No breaches" | "No incidents were assessed as personal data breaches this period." (and only if the incident log is kept) |
| "AIUC-1 certified by Q2" | "Readiness assessment shows 31 of 50 requirements evidenced. Certification is decided by the accredited auditor." |
