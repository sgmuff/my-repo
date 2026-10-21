# Privacy and AI governance skills

A suite of Claude Code skills that handle the repeatable parts of a privacy and AI governance program: screening, intake, drafting, citation, and record-keeping. Judgment calls, risk acceptance, and anything sent outside the organization stay with a person. Every deliverable is a draft until someone approves it.

## Layout

```
skills/
  _shared/                  shared by every skill; not a skill itself
    conventions.md          style, citations, verify flags, roles, output layout, IDs
    company-profile.md      company facts, filled in once
    approvals.md            who approves what, and how approval is recorded
    connectors.md           Jira, ServiceNow, document sources, email (no calendars)
    references/             one versioned file per framework (see references/README.md)
    templates/              risk register, action plan, approval record
    scripts/                register indexes, checklist generator, compliance schedule
  privacy-governance/       triage for requests that span workflows (Wave 1)
  dpia/                     data protection impact assessments (Wave 0)
  vendor-review/            vendor, subprocessor, and AI provider reviews (Wave 1)
  ropa/                     record of processing activities and its index (Wave 1)
  dsr-response/             data subject and consumer requests (Wave 2)
  ai-intake/                AI system and agent inventory and tiering (Wave 2)
  ai-impact-assessment/     AI impact assessments and FRIAs (Wave 2)
  lia/                      legitimate interests and compatibility assessments (suite phase 1)
  tia/                      transfer screens and transfer impact assessments (suite phase 1)
  ai-act-provider/          AI Act provider files: classification and provider obligations (suite phase 2)
  ai-act-deployer/          AI Act deployer checks: Art. 25, Art. 26 duties, and the FRIA trigger (suite phase 2)
  incident-assessment/      breach notification clocks, analysis, and drafts (Wave 3)
  controls-and-evidence/    control library, evidence, AIUC-1 readiness, schedule (Wave 4)
  program-assessment/       NIST PF profiles, Tier, gaps, and roadmap (Wave 4)
  notice-and-policy/        privacy notice reviews and AI acceptable use policies (Wave 5)
  regulatory-change/        law and standard changes, impact maps, reference updates (Wave 5)
  leadership-report/        board and leadership reports with traceable metrics (Wave 5)
  writing-style/            the house prose style
  install.sh                installs gov and links the skills into ~/.claude/skills
```

The `gov` command, at the repository root in `gov/`, owns IDs, validation, rendering, and triage routing. Records it manages, so far the RoPA, live as YAML under `compliance/`. See `docs/design/governance-suite-plan.md`.

Each skill keeps its own workflow-specific references, templates, examples, and `evals/` (test scenarios). Framework details live only in `_shared/references/`, so updating a law or standard means editing one file.

## Install

### Claude Code

Install one way, not both:

- **Script:** `./skills/install.sh` installs `gov` (with `uv` if present, otherwise `pip --user`) and symlinks each skill and `_shared` into `~/.claude/skills`. It skips any folder already there as a real folder, and tells you; move that folder aside and rerun.
- **Plugin:** the repository is a Claude Code plugin (`.claude-plugin/plugin.json`). Install `gov` separately with `pip install -e .` from the repository root.

The skills need `gov` on your PATH. Each skill checks for it first and stops if it's missing.

Skills uploaded to claude.ai earlier are out of date and don't use `gov`. Remove them, or Claude Code sees two copies of each skill.

Claude Desktop isn't supported: it keeps no edits between sessions, so it can't hold the registers or ID counters.

## First run

Fill in `_shared/company-profile.md`. The skills ask for any missing value they need, and offer to save it.

## Build status

| Wave | Skills | Status |
|---|---|---|
| 0 | Shared foundation; `dpia` refactored onto it | Built |
| 1 | `privacy-governance` (router), `vendor-review`, `ropa` | Built |
| 2 | `dsr-response`, `ai-intake`, `ai-impact-assessment` | Built |
| 3 | `incident-assessment` | Built; needs counsel review of `us-breach-notification.md` before live use |
| 4 | `controls-and-evidence`, `program-assessment` | Built |
| 5 | `notice-and-policy`, `regulatory-change`, `leadership-report` | Built |
| Suite 1 | `lia`, `tia`, the assessment catalog, and `gov` records | Built; answer-first, holdout-tested |
| Suite 2 | `ai-act-provider`, `ai-act-deployer` | Built; evals pending |

## Keeping references current

Each reference file records its version and last-verified date, and `_shared/references/README.md` lists when each is due for review. AIUC-1 changes every quarter (January 15, April 15, July 15, October 15). The `regulatory-change` skill processes each release and sweep, and proposes edits for the privacy lead to approve. To edit by hand, follow the steps in that README.

## License

Copyright 2026 Stephen Muff. Licensed under the [Apache License, Version 2.0](../LICENSE); see [NOTICE](../NOTICE).
