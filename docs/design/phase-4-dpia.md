# Phase 4: the DPIA in the record format

Status: in progress, 2026-10-21. Slices 1 (`gov screen`), 2 (the `scr` screening record), and 3 (the `dpia` record) are built and tested, and the skill is rewritten answer-first (slice 4);
the screening findings and indicator rules are drafts until counsel decides the items marked **Counsel**.

## Why

`dpia` is the most-used skill and the last large one that writes Markdown by hand. Its template runs 1,629 words
blank over 12 sections. Phase 1 showed what the record format buys: deterministic structure, findings a person must
answer, issue rules, and rendering a regulator can read in one pass. The holdouts also showed it doesn't buy better
legal analysis on its own, so the skill moves to answer-first, like `lia` and `tia`.

## What gets built, in order

Each slice is usable on its own and ships with tests.

1. **`gov screen`.** Reads a RoPA record and reports which screening indicators its facts suggest, each Provisional and
   tied to the field that raised it. It never concludes that a DPIA is or isn't needed; that's the screening record's
   job. Rules live in `gov/rules/screening.yaml`, in the same shape as `issues.yaml`.
2. **Screening record (`scr`, prefix SCR, in `assessments/dpia/screening/`).** One row per regime screened (EU GDPR Art. 35(3) and the EDPB criteria,
   the lead authority's Art. 35(4) list, UK ICO list, FADP Art. 22, US state triggers, AI Act), each criterion Present,
   Not present, or Unclear with fact references, then the outcome: warranted, recommended, or not indicated. Findings:
   two or more criteria present with "not indicated" and no reasoning; an Art. 35(3) case not marked warranted; a
   state trigger present with no state assessment linked.
3. **DPIA record (`dpia`, prefix DPIA).** Ratings are computed from likelihood and severity by the `risk-method.md` matrix, never typed, and the approver follows the current rating. The sections in the plan's example table: header, decision, processing,
   necessity and proportionality, risks and measures with the three ratings (inherent, current, target), consultation,
   other regimes, sign-off. Findings: a current High with no prior-consultation call; a target rating below the current
   with no verified control; a legitimate-interests basis with no linked LIA; an Art. 9 category with no condition;
   residual risk "confirmed" while any control is unverified.
4. **Skill rewrite, answer-first.** The same five steps as `lia`: answer, check against the references, record,
   validate and render, reply.
5. **Evals.** The existing `dpia` evals as the development set, then a holdout with counsel's keys, scored blind.

The processor assistance pack stays a Markdown deliverable for now; it is a document for a customer, not a record of
the company's own decision.

## Decisions

| # | Question | Proposal | Owner |
|---|---|---|---|
| 1 | Which RoPA facts suggest which EDPB criteria in `gov screen` | See the draft table below | **Counsel** |
| 2 | Whether `gov screen` should count criteria ("2 or more") | Report the count, never a conclusion from it; WP248 says two or more "in most cases" | **Counsel** |
| 3 | National Art. 35(4) lists | A list per authority in a reference file, starting with the lead authority in the company profile; until a list is verified, the row is Unclear with a verify flag | **Counsel** |
| 4 | DPIA word budget | Warn at 1,500 words, as the plan assumes | Privacy lead |
| 5 | Existing Markdown DPIAs | Leave them; new and updated DPIAs use the record. No migration script | Privacy lead |

### Draft indicator rules for `gov screen` (decision 1)

| EDPB criterion (WP248) | Raised by, in the RoPA record |
|---|---|
| 1 Evaluation or scoring | `us_flags.profiling` true or TBC |
| 2 Automated decisions with significant effect | Not raised; the skill asks |
| 3 Systematic monitoring | Not raised; the RoPA has no field for it, so the skill asks |
| 4 Sensitive or highly personal data | A data category flagged `special-category`, `criminal`, `biometric`, `us-sensitive`, `government-id`, or `financial`; `us_flags.sensitive_data` true or TBC |
| 5 Large scale | Not raised; the skill asks with the WP29 factors |
| 6 Matching or combining datasets | Not raised; `systems.data_sources` is free text, so the skill asks |
| 7 Vulnerable data subjects | A data subject with `vulnerable` true or TBC; a data category flagged `children` or `education-record` |
| 8 Innovative technology | `ai_used` true or TBC |
| 9 Blocks a right, service, or contract | Not raised; the skill asks |

Rows marked "not raised" print as "Ask" so the screening record can't skip them.

Each raised row says "suggested by <field>"; the screening record decides Present, Not present, or Unclear.
