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
  incident-assessment/      breach notification clocks, analysis, and drafts (Wave 3)
  controls-and-evidence/    control library, evidence, AIUC-1 readiness, schedule (Wave 4)
  program-assessment/       NIST PF profiles, Tier, gaps, and roadmap (Wave 4)
  notice-and-policy/        privacy notice reviews and AI acceptable use policies (Wave 5)
  regulatory-change/        law and standard changes, impact maps, reference updates (Wave 5)
  leadership-report/        board and leadership reports with traceable metrics (Wave 5)
  writing-style/            the house prose style
  install.sh                links the skills into ~/.claude/skills (Claude Code)
  package_desktop.py        builds the Claude Desktop zips in ../dist/claude-desktop/
```

Each skill keeps its own workflow-specific references, templates, examples, and `evals/` (test scenarios). Framework details live only in `_shared/references/`, so updating a law or standard means editing one file.

## Install

### Claude Code

```bash
./skills/install.sh
```

The script symlinks each skill folder and `_shared` into `~/.claude/skills`. It skips any folder that already exists there as a real folder, such as an older copy of `writing-style`, and tells you. Move that folder aside and rerun the script to link the repo version.

### Claude Desktop and claude.ai

The packaged skills are in `dist/claude-desktop/`, one zip per skill. Claude Desktop installs each skill on its own, so each zip carries its own copy of `_shared` (as `shared/`), with the paths rewritten and a note in `shared/conventions.md` on how the suite runs there: deliverables go to the session's outputs folder for download, and earlier records are uploaded when a skill needs them.

1. Turn on code execution: Settings, then Capabilities.
2. Upload each zip under Settings, then Capabilities, then Skills. Install `writing-style` and `privacy-governance` (the router) along with the skills you use.
3. Fill in `shared/company-profile.md` before zipping, or give the company facts in the first conversation. Desktop doesn't keep edits to an installed skill, so save confirmed facts back to the repo and rebuild.

The repo is the source. After changing a skill, rebuild and re-upload the zips that changed:

```bash
python3 skills/package_desktop.py
```

The build validates each SKILL.md and checks that every link resolves inside the zip, and stops with a list of problems if not. Evals stay out of the zips.

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

## Keeping references current

Each reference file records its version and last-verified date, and `_shared/references/README.md` lists when each is due for review. AIUC-1 changes every quarter (January 15, April 15, July 15, October 15). The `regulatory-change` skill processes each release and sweep, and proposes edits for the privacy lead to approve. To edit by hand, follow the steps in that README.
