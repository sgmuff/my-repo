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
    scripts/                register index builder (RoPA, AI inventory)
  privacy-governance/       triage for requests that span workflows (Wave 1)
  dpia/                     data protection impact assessments (Wave 0)
  vendor-review/            vendor, subprocessor, and AI provider reviews (Wave 1)
  ropa/                     record of processing activities and its index (Wave 1)
  dsr-response/             data subject and consumer requests (Wave 2)
  ai-intake/                AI system and agent inventory and tiering (Wave 2)
  ai-impact-assessment/     AI impact assessments and FRIAs (Wave 2)
  writing-style/            the house prose style
  install.sh                links the skills into ~/.claude/skills
```

Each skill keeps its own workflow-specific references, templates, examples, and `evals/` (test scenarios). Framework details live only in `_shared/references/`, so updating a law or standard means editing one file.

## Install

```bash
./skills/install.sh
```

The script symlinks each skill folder and `_shared` into `~/.claude/skills`. It skips any folder that already exists there as a real folder, such as an older copy of `writing-style`, and tells you. Move that folder aside and rerun the script to link the repo version.

## First run

Fill in `_shared/company-profile.md`. The skills ask for any missing value they need, and offer to save it.

## Build status

| Wave | Skills | Status |
|---|---|---|
| 0 | Shared foundation; `dpia` refactored onto it | Built |
| 1 | `privacy-governance` (router), `vendor-review`, `ropa` | Built |
| 2 | `dsr-response`, `ai-intake`, `ai-impact-assessment` | Built |
| 3 | `incident-assessment` | Planned; needs counsel review of the breach law reference before live use |
| 4 | `controls-and-evidence`, `program-assessment` | Planned |
| 5 | `notice-and-policy`, `regulatory-change`, `leadership-report` | Planned |

## Keeping references current

Each reference file records its version and last-verified date, and `_shared/references/README.md` lists when each is due for review. AIUC-1 changes every quarter (January 15, April 15, July 15, October 15). Until the `regulatory-change` skill exists, update reference files by hand using the steps in that README.
