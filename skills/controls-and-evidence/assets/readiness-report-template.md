---
id: ISO-YYYY-NNN       # from `gov next-id ISO --year <YYYY>`; AIUC-1 readiness is a gov rdy record
type: iso-readiness
title: <ISO/IEC 42001 readiness: scope, or audit evidence pack: request>
framework: <ISO/IEC 42001 | audit evidence pack>
framework_version: <ISO/IEC 42001:2023 (public checklist)>
status: Draft
stage: Draft complete
scope: <product, agent, capabilities>
requesting_business_area: <business area>
system_owner: <team or person>
prepared_by: Claude (privacy-governance suite), for <privacy lead>
date_prepared: YYYY-MM-DD
next_review: YYYY-MM-DD
references:
  - aiuc-1.md (Oct 15, 2026 release), last verified 2026-10-16
  - crosswalk.md (built 2026-10-16), last verified 2026-10-16
---

# <Framework> readiness: <scope>

## 1. Summary

> **Readiness status:** Draft. This report prepares for an audit; it doesn't certify, and it doesn't claim the company meets the standard.
> **Coverage (Provisional):** <n> requirements Covered, <n> Partly covered, <n> Not covered, <n> Not applicable.
> **Release audited against:** <release>. A newer release <is | isn't> out; grace period ends <date>.
> **Top gaps:** <requirement IDs, one line each>.

> **Decision needed:** <scope, exclusions, opt-ins, target audit date, for the privacy lead and system owner>

## 2. Scope

| Field | Value |
|---|---|
| Agent or system | |
| Capabilities (capability tags) | |
| Deployment context | |
| Out of scope, and why | |

## 3. Statement of Applicability

<Output of `make_checklist.py aiuc-1 soa` (or `iso-42001 soa`), filled in. A mandatory requirement is excluded only where the agent lacks the tagged capability, with a short justification.>

## 4. Coverage by requirement

| Requirement | Applicability rationale | Responsible (company, model provider, shared) | Controls (CTL) | Evidence (EV), by category | Testing (third-party? frequency) | Coverage | Gap | Action |
|---|---|---|---|---|---|---|---|---|

Evidence categories for AIUC-1: legal policies, operational practices, technical implementation, third-party evaluations.

## 5. Testing schedule

| Duty | Requirement | Frequency | Last done | Next due | Control |
|---|---|---|---|---|---|
| Third-party testing, data and privacy | A009 | At least every 3 months | | | |
| Third-party testing, security | B001 | At least every 3 months | | | |
| Third-party testing, safety | C010 | At least every 3 months | | | |
| Third-party testing, reliability | D004 | At least every 3 months | | | |
| Third-party testing, accountability | E018 | At least every 3 months | | | |
| Internal process review | E008 | Regular | | | |
| Re-certification | — | Annual | | | |

## 5a. Milestones (gates, not commitments)

| Gate | Target date | Entry condition | Status |
|---|---|---|---|
| Testing arrangements (AIUC evaluations) and auditor confirmed | | | |
| Critical agent safety gaps fixed (authorization, action limits, disclosure) | | | |
| Baseline third-party evaluations done | | | |
| Evidence pack complete | | | |
| Audit start | | No critical findings open | |
| Certificate | | | |

## 6. Action plan

<Action plan block from ../../_shared/templates/action-plan.md. Each gap gets an action with an owner, due date, acceptance criterion, and the evidence that closes it.>

## 7. Sign-off

<Sign-off block from ../../_shared/templates/approval-record.md.>
