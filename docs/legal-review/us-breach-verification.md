# Verification sheet: us-breach-notification.md

Prepared October 21, 2026, to speed counsel's review of
[`skills/_shared/references/us-breach-notification.md`](../../skills/_shared/references/us-breach-notification.md), the
one reference file `incident-assessment` needs reviewed before live use. Claude gathered the text; counsel verifies.

**Scope.** The rows that set a date or a threshold, which drive `gov clock`: every fixed individual-notice
deadline, every regulator deadline, and the rows the file flags *verify*. Rows that say only "most expedient" or
"without unreasonable delay" weren't re-read.

**Sources.** Official state code sites where they allow automated access, then official agency pages (attorneys
general). Where both were blocked, secondary sources, marked as such. Quotes are short fragments of the statute text.

**Result key.** **Matches**: the statute text supports the row. **Correct**: the row needs the edit shown. **Secondary**:
supported only by secondary sources. **Not checked**: no source reached.

## Fixed deadlines and thresholds

| Jurisdiction | Row says | Source checked | Result |
|---|---|---|---|
| Arizona | 45 days; >1,000: AG and homeland security director (*verify*), CRAs | A.R.S. § 18-552(B), azleg.gov | **Matches.** "within forty-five days after the determination"; >1,000 notify CRAs and "the attorney general and the director of the Arizona department of homeland security". The *verify* can go. |
| California | 30 calendar days; >500: sample to AG within 15 days of individual notice (SB 446, from Jan. 1, 2026) | Cal. Civ. Code § 1798.82; leginfo blocked automated access. AG page (oag.ca.gov) confirms the >500 sample notice | **Secondary** for the 30- and 15-day rules, **approved by counsel as written on 2026-10-22** (law-firm alerts on SB 446, signed October 3, 2025). Sources differ on whether the 15 days run from individual notice; check the chaptered text. |
| Connecticut | 60 days; AG not later than individual notice; 24 months of identity theft protection for SSN or TIN | Conn. Gen. Stat. § 36a-701b, cga.ct.gov | **Matches.** "not later than sixty days after the discovery"; AG "not later than the time when notice is provided to the resident". **Add:** P.A. 23-98 added precise geolocation data to "personal information". |
| Delaware | 60 days; >500: AG not later than individual notice; 1 year of credit monitoring for SSN | 6 Del. C. § 12B-102(c)-(e), delcode.delaware.gov | **Matches.** |
| Florida | 30 days; ≥500: AG within 30 days; CRAs >1,000 | Fla. Stat. § 501.171(3)-(5), leg.state.fl.us | **Matches.** **Add:** 15 more days for notice on written good cause to the department within the 30 days; a third-party agent notifies within 10 days. |
| Iowa | AG >500, within 5 business days of individual notice | Iowa Code § 715C.2(8), legis.iowa.gov | **Matches** on the threshold (notice to "the director of the consumer protection division"). |
| Maine | 30 days after becoming aware | 10 M.R.S. § 1348(1), legislature.maine.gov | **Correct:** 30 days after the person "becomes aware of a breach of security **and identifies its scope**". CRAs >1,000. |
| Maryland | 45 days; AG before individual notice | Md. Code, Com. Law § 14-3504, mgaleg.maryland.gov | **Matches** on 45 days ("not later than 45 days after the business discovers or is notified"). AG timing: the fetched text confirms AG notice and its contents; the "before" wording wasn't isolated. |
| New York | 30 days after discovery; AG, Department of State, State Police, and DFS for covered entities; CRAs >5,000 | GBL § 899-aa(2), (8), nysenate.gov (revised March 28, 2025) | **Matches.** |
| North Dakota | AG >250 | N.D.C.C. § 51-30-02, ndlegis.gov | **Matches** (AG notice where a breach "exceeds two hundred fifty individuals", in the most expedient time possible). The 2025 financial-institution rule wasn't checked. |
| Ohio | 45 days; CRAs >1,000 | ORC § 1349.19(B)(2), (G), codes.ohio.gov | **Matches.** |
| Oklahoma | ≥500: AG within 60 days of individual notice, from Jan. 1, 2026 | Enrolled SB 626, § 163(E), oklegislature.gov | **Matches.** "in no event more than sixty (60) days after providing notice to impacted residents"; fewer than 500 exempt (1,000 for credit bureaus). |
| Oregon | 45 days; AG >250; CRAs >1,000 | ORS 646A.604(1), (3), (6), oregonlegislature.gov | **Matches.** **Add:** a vendor notifies the AG itself for >250 consumers unless the covered entity has. |
| Texas | 60 days; AG ≥250 within 30 days (*verify* threshold) | Texas AG data breach reporting page; statutes.capitol.texas.gov didn't load | **Matches** on the AG rule ("affects 250 or more Texans ... no later than 30 days after the discovery"), from the AG's official page. The *verify* can go. Individual 60 days not re-read. |
| Vermont | 45 days; preliminary AG notice within 14 business days | 9 V.S.A. § 2435(b), legislature.vermont.gov | **Matches.** |
| Washington | 30 days; AG >500 within 30 days | RCW 19.255.010(7)-(8), app.leg.wa.gov | **Matches** ("no more than thirty calendar days after the breach was discovered"). |
| Wisconsin | 45 days; CRAs >1,000 | Wis. Stat. § 134.98(2)-(3), docs.legis.wisconsin.gov | **Correct:** CRAs at **1,000 or more** ("1,000 or more individuals"), not more than 1,000. 45 days matches ("not to exceed 45 days after the entity learns"). |

| Colorado | 30 days; ≥500: AG within 30 days; CRAs >1,000 | Colorado AG data breach page (coag.gov); C.R.S. § 6-1-716 text not reached | **Matches**, from the AG's official guidance: notice "within 30 days after the date of determination"; AG for "500 or more"; CRAs for "more than 1,000". |
| South Dakota | 60 days; AG >250 | SDCL § 22-40-20, sdlegislature.gov | **Matches** on 60 days ("not later than sixty days from the discovery or notification"). The AG threshold (§ 22-40-23) wasn't isolated. |
| Alabama, Indiana, New Mexico, Rhode Island, Tennessee, Utah, Pennsylvania | Fixed deadlines and thresholds as in the table | Official sites blocked automated access or rendered only in a browser | **Not checked by Claude; approved by counsel as written on 2026-10-22.** |

## Corrections applied to the reference file

The file now carries the two corrections (Maine, Wisconsin) and the three additions (Connecticut, Florida, Oregon), and
drops *verify* from Arizona's AG and homeland security notice and Texas's AG threshold. Its status stays "Draft, needs
counsel review": this sheet supports that review; it doesn't replace it.

## What this sheet doesn't cover

- Rows with no fixed deadline ("most expedient", "without unreasonable delay"), RoH availability, and definitions of
  personal information, except where noted.
- Federal and sector laws (§4) and student data (§5).
- Changes after October 21, 2026.
