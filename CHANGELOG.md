# Changelog

## Unreleased: 1.0.0 candidate

The 1.0 tag waits on the trigger evals and on counsel's open reviews (see the plan's "Remaining roadmap").

### Records

Every assessment and register is a `gov` record: YAML validated against a schema, with Markdown rendered from a fixed
template. Sixteen record types:

| Area | Types |
|---|---|
| Records of processing and screening | `ropa`, `scr` |
| Assessments | `dpia`, `lia`, `tia`, `tsr`, `aip`, `aid`, `aiia` (with FRIAs and input packs), `sra` (security) |
| Operations | `vr` (vendor reviews), `inc` (incidents), `dsr` (requests) |
| Program | `ais` (AI inventory), `ctl` (control library and evidence), `rdy` (AIUC-1 readiness) |

- `gov new`, `validate`, `render`, `next-id`, `required`, `route`, `screen`, `clock`, `deadlines`, `schedule`, and
  `metrics`. `gov` never reads the clock: dated commands take `--as-of`.
- Risk ratings, deadlines, tiers, and approvers are computed, never typed.
- Findings are legal consistency questions that only a person answers; errors fail CI, findings don't.
- Every verify flag links to the action that resolves it.
- `gov metrics` and `gov schedule` read records; no script scrapes Markdown tables.

### Skills

Seventeen governance skills plus `writing-style`. The assessment and operations skills answer first and record
second: Claude answers as a careful lawyer would, checks the answer against the reference files, then fills in the
record.

### Reference files

Each file carries front matter with its last verification, review date, source quality, and counsel review status.
`gov` generates the index, fails closed on missing front matter, and raises findings for overdue files or files counsel
hasn't fully reviewed.

### Evaluations

- AI Act skills: blind holdouts against counsel's keys (version 6), 90.0 with the skills against 82.4 without
  (`docs/evals/ai-act-results.md`).
- DPIA and router holdouts: keys drafted and revised; the DPIA keys' primary-source checks are in
  `docs/evals/dpia-verification.md`, awaiting counsel's sign-off.
- Development runs for every record type, each with a friction log that drove fixes.

### Removed

- `build_register_index.py`, `new_control.py`, and the four date scripts, replaced by `gov`.
- Markdown templates for every type that became a record.

## 0.1.0: 2026-10-16

First suite: Waves 0 to 3 of the skills as Markdown templates, with `gov` for the RoPA.
