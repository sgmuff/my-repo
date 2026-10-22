# Reference files

Framework details live here, so they can be updated as laws and standards change without rewriting the skills. Each file opens with its own header (version covered, sources, last verified, review interval, volatile points). This index summarizes those headers. Update both when a file changes.

| File | Covers | Version covered | Last verified | Review by | Interval |
|---|---|---|---|---|---|
| `gdpr.md` | EU GDPR, UK GDPR and DUAA, Swiss FADP | EU GDPR unamended (Omnibus pending); DUAA commenced in stages | 2026-10-16 | 2027-01-16 | Quarterly |
| `us-state-privacy.md` | 24 comprehensive state privacy laws, CCPA regulations, state AI laws | Status as of 2026-10-16 | 2026-10-16 | 2027-01-16 | Quarterly |
| `ferpa.md` | FERPA, COPPA, and state student privacy laws | eCFR current to 2026-07-10; COPPA as amended 2025 | 2026-10-16 | 2027-04-16 | Six months |
| `nist-privacy-framework.md` | NIST Privacy Framework | 1.0 (2020); 1.1 still a draft | 2026-10-16 | 2027-01-16 | Quarterly until 1.1 is final |
| `aiuc-1.md` | AIUC-1 | October 15, 2026 release | 2026-10-16 | 2027-01-29 (two weeks after the Jan 15 release) | Quarterly |
| `eu-ai-act.md` | EU AI Act as amended by Reg. (EU) 2026/1744 | In force from 2026-07-27 | 2026-10-16 | 2027-01-16 | Quarterly |
| `nist-ai-rmf.md` | NIST AI RMF and Generative AI Profile | AI RMF 1.0; AI 600-1 | 2026-10-16 | 2027-04-16 | Six months |
| `iso-42001.md` | ISO/IEC 42001 checklist (public paraphrase) | ISO/IEC 42001:2023 | 2026-10-16 | 2027-10-16 | Annual |
| `risk-method.md` | Shared scoring method, catalog, and mitigations | Suite method | 2026-10-16 | 2027-10-16 | Annual |
| `dsr-matrix.md` | Data subject request rights, deadlines, verification, exceptions | As of 2026-10-16 | 2026-10-16 | 2027-01-16 | Quarterly |
| `us-breach-notification.md` | US state, territory, and federal breach notification laws | As of 2026-10-21; **draft, needs counsel review** | 2026-10-21 | 2027-01-21 | Quarterly |
| `crosswalk.md` | 32 common control objectives mapped across all frameworks | Built 2026-10-16 | 2026-10-16 | 2027-01-29 (after the Jan 15 AIUC-1 release) | Quarterly |
| `hipaa.md` | HIPAA Privacy, Security, and Breach Notification Rules for covered entities and business associates | Rules through the 2013 Omnibus Rule; 2025 Security Rule proposal noted | 2026-10-18, secondary sources; counsel-approved 2026-10-19 | 2027-04-19 | Six months |
| `glba.md` | GLBA Safeguards Rule, including higher education and service providers | 16 CFR Part 314 as amended 2021 and 2023 | 2026-10-18, secondary sources; counsel-approved 2026-10-19 | 2027-04-19 | Six months |
| `nis2.md` | NIS2 risk-management and reporting duties | Directive 2022/2555; Implementing Regulation 2024/2690 | 2026-10-18, secondary sources; counsel-approved 2026-10-19 | 2027-01-19 | Quarterly |
| `quebec-law-25.md` | Quebec private-sector privacy act as amended by Law 25 | All phases in force | 2026-10-18, secondary sources; counsel-approved 2026-10-19 | 2027-04-19 | Six months |
| `eu-ai-act-gpai.md` | AI Act duties for general-purpose AI model providers | Chapter V as amended by Reg. (EU) 2026/1744 | 2026-10-18, secondary sources; counsel-approved 2026-10-19 | 2027-01-19 | Quarterly |
| `dpa-checklist.md` | DPA and vendor contract checklist, with AI terms | Built from the files above, as of 2026-10-16 | 2026-10-16 | 2027-01-16 | Quarterly |

The company's own control library and evidence index live under the output root (`registers/controls/`), not here. They're company records, mapped through `crosswalk.md`.

## Updating a file

The `regulatory-change` skill runs these steps: it proposes the edits in a change memo, and applies them only after the privacy lead approves. To update by hand:

1. Check the primary sources listed in the file's header.
2. Edit the content. Mark anything still changing as *Volatile* in the text and in the header.
3. Update the header's version, sources, and last-verified date, and this index.
4. Commit with a message that says what changed and why, for example "AIUC-1: update to January 15, 2027 release."
5. Search open deliverables under the output root for citations of anything you changed, and flag them for review.

## Contributing a reference update

You don't need to know the rest of the suite to update a file. In one change:

1. **Edit the file.** Keep the opening header table: Covers, Version covered, Sources, Last verified, Review interval,
   Volatile points. Quote primary sources (EUR-Lex, legislation.gov.uk, eCFR, a regulator's site), and mark anything you
   couldn't check against one as *Verify*.
2. **Bump the dates.** Set "Last verified" in the file's header to the day you checked. In the table above, set the same
   date under "Last verified" and the next review under "Review by" (last verified plus the interval). Keep the table's
   six columns and the file name in backticks: `gov` reads the first date in each of those two cells.
3. **Don't copy third-party standards.** Statutes, regulations, and EU and US government publications can be quoted. A
   commercial standard (AIUC-1, ISO) can be cited and paraphrased in your own words, not reproduced; see each file's
   header for its terms.
4. **Run the tests:** `pip install -e '.[test]'`, then `pytest -q`, `gov validate`, and `gov render --check`. The tests
   check the index parses; `gov validate` will now raise a finding on any record that cited the old version.
5. **Say what changed and why** in the commit message, for example "gdpr.md: DUAA commencement regulations 2027".

What you don't need to touch: `gov/rules/assessments.yaml` names a file per catalog entry (`reference:`), and an entry
is skipped only if its file doesn't exist. Renaming or deleting a file does need that file updated; editing one doesn't.
Legal content changes need counsel's review before they're relied on (`../approvals.md`).

A skill that finds a file past its "Review by" date says so in the deliverable's document control section and flags the conclusions that rely on it (`../conventions.md`, §4).
