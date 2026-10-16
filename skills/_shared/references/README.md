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
| `dpa-checklist.md` | DPA and vendor contract checklist, with AI terms | Built from the files above, as of 2026-10-16 | 2026-10-16 | 2027-01-16 | Quarterly |

Planned for later waves: `dsr-matrix.md` (Wave 2, `dsr-response`), `us-breach-notification.md` (Wave 3, `incident-assessment`), and a control library with evidence index (Wave 4, `controls-and-evidence`).

## Updating a file

1. Check the primary sources listed in the file's header.
2. Edit the content. Mark anything still changing as *Volatile* in the text and in the header.
3. Update the header's version, sources, and last-verified date, and this index.
4. Commit with a message that says what changed and why, for example "AIUC-1: update to January 15, 2027 release."
5. Search open deliverables under the output root for citations of anything you changed, and flag them for review.

A skill that finds a file past its "Review by" date says so in the deliverable's document control section and flags the conclusions that rely on it (`../conventions.md`, §4).
