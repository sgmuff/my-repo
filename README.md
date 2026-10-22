# Privacy and AI governance suite

Skills for Claude Code that draft the assessments a privacy or AI governance team owes, and `gov`, a command-line tool
that keeps those assessments as structured, checked records. Claude takes a position on each legal question, cites the
provision, and says how settled it is. A person makes every decision.

**This is not legal advice.** Every call the skills make is Provisional until a named person approves it, and some
reference files are still waiting for counsel's review (see [Status](#status)).

## What it covers

| Area | Skills |
|---|---|
| Triage | `privacy-governance` routes a request to the workflows it needs |
| Records | `ropa` (records of processing), `ai-intake` (AI inventory and tiering) |
| Assessments | `dpia`, `lia` (legitimate interests), `tia` (transfers), `ai-act-provider`, `ai-act-deployer`, `ai-impact-assessment` |
| Operations | `vendor-review`, `dsr-response`, `incident-assessment`, `notice-and-policy` |
| Program | `controls-and-evidence`, `program-assessment`, `regulatory-change`, `leadership-report` |

The laws and standards behind them are in [`skills/_shared/references/`](skills/_shared/references/): the GDPR, UK GDPR
and Swiss FADP, the EU AI Act as amended in 2026, US state privacy and breach laws, FERPA, HIPAA, GLBA, NIS2, Quebec
Law 25, NIST frameworks, ISO/IEC 42001, and AIUC-1.

## How it works

The newer skills answer first and record second. Claude answers the request as a careful lawyer would, checks the
answer against the reference files, then fills in a YAML record. `gov` validates the record and renders it to Markdown
in a fixed format. The record never changes the conclusion; it makes the conclusion checkable.

`gov` adds what a model can't promise on its own:

- **Fixed structure.** Each record type has a schema, word limits, and a template, so every DPIA or LIA reads the same.
- **Findings a person must answer.** Legal consistency checks, such as a "ready" decision with open obligations, or an
  Annex III system that profiles people but is called not high-risk. Only a person can mark one as not applying.
- **Issue rules.** Facts in the record raise the issues an assessment must address, from `gov/rules/issues.yaml`.
- **Source checks.** A record that cites a reference file past its review date, or one counsel hasn't reviewed, gets a
  finding, and the rendered document says how each source was verified.
- **Determinism.** `gov` reads only files and arguments, never the clock, so the same input gives the same output.

## Quick start

```sh
git clone https://github.com/sgmuff/my-repo && cd my-repo
./skills/install.sh          # installs gov and links the skills into ~/.claude/skills
```

Then fill in [`skills/_shared/company-profile.md`](skills/_shared/company-profile.md). The skills ask for anything
missing, and `gov validate` won't pass an approved record while the fields that set scope are still `TODO`. See
[`skills/README.md`](skills/README.md) for the plugin install and other details.

## What's enforced and what's measured

Two kinds of promise, checked in different ways:

- **On every commit (CI):** the tests, `gov validate`, and `gov render --check`. These cover structure, IDs,
  findings, issue rules, rendering, routing, and the date arithmetic in the incident clock.
- **By hand, at a point in time:** the quality of the legal analysis. Holdout scenarios the skills weren't built on are
  scored blind against answer keys written by counsel. Results carry the key version and the date of the legal texts
  used, and they age as the law changes. Latest: [AI Act skills](docs/evals/ai-act-results.md), October 21, 2026,
  90.0 with the skills against 82.4 without.

A passing build says the records are well formed and consistent. It says nothing about whether the law in them is
right.

## Status

Built and tested: all 17 skills and `gov`. Still open:

- `us-breach-notification.md` needs counsel's review before `incident-assessment` is used live.
- The DPIA is moving into the record format ([design](docs/design/phase-4-dpia.md)).
- The plan, with progress and the backlog, is in [`docs/design/governance-suite-plan.md`](docs/design/governance-suite-plan.md).

## Contributing

Reference files go stale fastest. To update one, follow "Contributing a reference update" in
[`skills/_shared/references/README.md`](skills/_shared/references/README.md). Legal content changes need counsel's
review before anyone relies on them. Don't copy text from commercial standards such as AIUC-1 or ISO; cite them.

## License

Copyright 2026 Stephen Muff. Licensed under the [Apache License, Version 2.0](LICENSE); see [NOTICE](NOTICE).
