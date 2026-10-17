---
id: AIIA-YYYY-NNN
type: ai-impact-assessment
title: <System name>: <use assessed>
status: Draft
stage: Draft complete   # Screening complete | Draft complete | Ready for sign-off | Authorized to launch
version: 0.1
system: AIS-NNNN
tier: <1 High | 2 Elevated> (from intake)
requesting_business_area: <business area>
system_owner: <team or person>
prepared_by: Claude (privacy-governance suite), for <privacy lead>
date_prepared: YYYY-MM-DD
next_review: YYYY-MM-DD
eu_ai_act: {category: <…> (provisional), role: <provider | deployer | both> (provisional)}
aiuc_1: {mode: <readiness | benchmark>, release: Oct 15, 2026}
residual_risk: {current: <rating>, target: <rating>, confirmed: false}
launch_authorized: false
related: {dpia: <DPIA-…>, vendor_review: <VR-…>, fria: <file or n/a>}
references:
  - aiuc-1.md (Oct 15, 2026 release), last verified 2026-10-16
  - eu-ai-act.md (as amended by Reg. (EU) 2026/1744), last verified 2026-10-16
  - nist-ai-rmf.md (AI RMF 1.0), last verified 2026-10-16
tickets: []
---

# AI impact assessment: <System name>

## Document control

| Field | Value |
|---|---|
| Assessment ID | |
| Status and stage | Draft · <stage> |
| System (inventory ID) and use assessed | |
| Tier and sections in scope | <tier>; <sections, with reasons for any left out> |
| Requesting business area · system owner | |
| Roles (Provisional) | |
| Related records | Inventory entry, DPIA, vendor review, FRIA |
| Reference files relied on | |

### Version history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | | | First draft |

## 1. Executive summary

> **Assessment status:** Draft, not approved. Stage: <stage>.
> **Classification:** <EU AI Act category> (Provisional). Prohibition check: <clear | concern: …> (status).
> **Residual risk:** not yet confirmed. Current: **<rating>**. Target: **<rating>**, subject to verification of A….
> **FRIA:** <required (deployer) | input pack for customers (provider) | not required> (Provisional).
> **Launch decision:** Not authorized by this draft. The system must not be used for <use> until the approver named in §14 has reviewed the completed assessment, confirmed the classification and roles, verified the launch-blocking actions with evidence, and recorded the residual-risk decision.

<Short paragraphs: what the system does and for whom; the findings that drive the rating; the conditions for going ahead.>

> **Decision needed:** <determinations and risk acceptance, with approvers>

## 2. Fact register

| # | Fact | Status | Evidence or source | Owner | Needed by | Blocks launch? |
|---|---|---|---|---|---|---|

### 2a. Verification register

| # | Claim being checked | Why it matters | Source to check | Owner | Blocks launch? | Action |
|---|---|---|---|---|---|---|

## 3. Intended purpose and context

## 4. Fairness and non-discrimination

| Group or proxy | Metric | Result | Sample and conditions | Finding (status) |
|---|---|---|---|---|

**Conclusion:** <Adequate, Gap, or Not met> (status). Basis: <AIUC-1 C003, C010; NIST MEASURE 2.11; AI Act Art. 10>

## 5. Transparency and explainability

| Duty | Who | What they're told, and when | Evidence | Finding (status) |
|---|---|---|---|---|

## 6. Human oversight

| Question | Answer | Evidence | Finding (status) |
|---|---|---|---|
| What the reviewer sees | | | |
| Independent reason required before acting? | | | |
| Override or disagreement rate | | | |
| Can the reviewer stop the system? | | | |
| Remedies for affected people | | | |

## 7. Data provenance and quality

## 8. Reliability and model limitations

| Measure | Result | Test set and conditions | Date | Finding (status) |
|---|---|---|---|---|

Known limitations and out-of-scope uses:

## 9. Safety

## 10. Security (summary; security team owns the detail)

## 11. Accountability

| Item | Owner | Evidence | Finding (status) |
|---|---|---|---|
| System owner and change approver | | | |
| Failure plans (security breach, harmful output, hallucination) | | | |
| Logging | | | |
| Incident reporting | | | |

## 12. Society

## 13. Risk register

<Register block from ../../_shared/templates/risk-register.md, using the AI risk catalog (risk-method.md §2a). Name who is affected: individuals, groups, or society. Add reach, reversibility, and autonomy to severity.>

## 14. Action plan

<Action plan block from ../../_shared/templates/action-plan.md. For AIUC-1 readiness, include the quarterly third-party testing as recurring actions (A009, B001, C010, D004, E018). No calendar events.>

## 14a. Launch gates

Each gate has an owner, a measurable test, and the evidence that closes it. Every gate must be met, or explicitly accepted by the accountable approver, before use.

| # | Gate | Type (Legal or Readiness) | Owner | Test or threshold | Evidence that closes it | Status |
|---|---|---|---|---|---|---|
| G1 | Human review | | | Low-scoring cases get meaningful review and can be advanced regardless of score | Workflow, override statistics | Open |
| G2 | Fairness | | | Disparities investigated; relevant groups tested with adequate samples | Test report | Open |
| G3 | Vendor assurance | | | Validation report, intended purpose, change and incident processes reviewed | Documents | Open |
| G4 | Legal classification | | | Roles, applicable dates, Art. 22, and jurisdiction-specific duties confirmed | Counsel memo | Open |
| G5 | Transparency | | | Notices, explanations, and alternative or accommodation routes approved | Notice text | Open |
| G6 | Monitoring | | | Performance and fairness thresholds, owners, and a stop-use trigger set | Monitoring plan | Open |

## 15. Sign-off

<Sign-off block from ../../_shared/templates/approval-record.md, routed by the current residual rating, plus:>

| Item | Name and role | Date | Notes |
|---|---|---|---|
| Classification and roles confirmed | | | |
| Prohibition check confirmed | | | |
| Launch authorized | | | Only once launch blockers are Done with evidence |

## Appendix: ticket import

<Only when no ticketing tool is connected.>
