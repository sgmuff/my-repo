---
id: VR-YYYY-NNN
type: vendor-review
title: <Vendor name>: <services in scope>
vendor: <legal name of signing entity>
status: Draft
stage: Draft complete   # Screening complete | Draft complete | Ready for sign-off | Authorized to launch
depth: <Light | Standard | Deep>
version: 0.1
review_kind: <new | renewal | expansion | reassessment>
requesting_business_area: <business area>
system_owner: <team or person, if different>
prepared_by: Claude (privacy-governance suite), for <privacy lead>
date_prepared: YYYY-MM-DD
next_review: YYYY-MM-DD
roles: {gdpr: <processor (provisional) | ...>, us_state: <service provider | third party | ...>, ferpa: <n/a | school official subcontractor>, eu_ai_act: {vendor: <provider | n/a>, company: <deployer | n/a>}}
aiuc_1: {mode: vendor benchmark, certified: <yes | no | claimed, unverified>, product_in_scope: <...>, release: <...>, report_date: <...>}
recommendation: <Approve | Approve with conditions | Do not approve as proposed> (provisional)
residual_risk: {current: <rating>, target: <rating>, confirmed: false}
onboarding_authorized: false
references:
  - dpa-checklist.md (as of 2026-10-16), last verified 2026-10-16
tickets: []
---

# Vendor review: <Vendor name>

## Document control

| Field | Value |
|---|---|
| Review ID | |
| Status and stage | Draft · <stage> |
| Vendor (signing entity) | |
| Services, products, and features in scope | |
| Review kind and depth | <new / renewal / …> · <Light / Standard / Deep>, because … |
| Requesting business area | |
| System owner | |
| Proposed roles | Per operation (all Provisional) |
| Documents reviewed | <title, version or date, how obtained> |
| Related records | RoPA entries, DPIAs, AI impact assessments, earlier reviews |
| Reference files relied on | |

### Version history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | | | First draft |

## 1. Executive summary

> **Review status:** Draft, not approved. Depth: <depth>.
> **Recommendation:** <…> (Provisional; depends on F…).
> **Residual risk:** not yet confirmed. Current: **<rating>**. Target: **<rating>**, subject to verification of A….
> **Onboarding decision:** Not authorized by this draft. Don't sign, renew, or turn on the service for personal data until the approver named in §11 has recorded a decision and the blocking conditions are verified.
> **Follow-on assessments:** <…>.

<Short paragraphs, each opening with its conclusion: what the vendor does for the company, the findings that drive the recommendation (finding IDs), the conditions, and anything already processed before review.>

> **Decision needed:** <The approval decision and any legal determinations, with the approver for each, per approvals.md.>

## 2. Fact register

| # | Fact | Status | Evidence or source | Owner | Needed by | Blocks onboarding? |
|---|---|---|---|---|---|---|
| F1 | | Confirmed, Stated by requester, Stated by vendor, Unverified assumption, or TBC | | | | |

### 2a. Verification register

| # | Claim being checked | Why it matters | Source to check | Owner | Blocks onboarding? | Action |
|---|---|---|---|---|---|---|

## 3. Scope and data

| Service or feature | Purpose | Personal data | Data subjects | Sensitive categories | Proposed vendor role | Proposed company role |
|---|---|---|---|---|---|---|

## 4. DPA gap analysis

Ratings: **Present**, **Partial**, **Missing**, **Conflicts**. Clause references are to the documents listed in document control.

| # | Checklist item | What the contract says (clause) | Rating | Basis | Fix (contract, configuration, or compensating control) | Finding |
|---|---|---|---|---|---|---|
| 2.1 | Documented instructions | | | GDPR Art. 28(3)(a) | | G… |

<Include every checklist item in scope for the review depth. Group by checklist section.>

## 5. AI module

<Only when the vendor supplies AI. Checklist §6 items in the same table format, each with its AIUC-1 requirement. Then:>

### 5.1 AIUC-1 certification

| Field | Value |
|---|---|
| Certified? | Yes, No, or Claimed, not yet evidenced |
| Product in scope | |
| Release audited | |
| Report date and expiry | |
| Quarterly evaluations current? | |
| Exclusions in the Statement of Applicability | |
| Covers the product the company uses? | |

### 5.2 EU AI Act

<Proposed roles (Provisional), classification of the company's intended use by function, what the vendor must supply for deployer duties, and whether an AI impact assessment is recommended.>

## 6. Transfers

| From | To | Vendor entity | Mechanism | Verified? (source, date) | Fallback | TIA |
|---|---|---|---|---|---|---|

## 7. Security assurance

| Report | Date | Scope covers the service? | Exceptions noted | For the security team |
|---|---|---|---|---|

## 8. Findings

| ID | Finding | Status | Checklist items | Severity for individuals | Company-side (contract or commercial) | Owner |
|---|---|---|---|---|---|---|
| G1 | | Confirmed finding, Unverified concern, or Recommended control | | | <for Legal or Procurement, if any> | |

## 8a. Approval conditions (release gates)

The specific, verifiable conditions for approval. Each one names the evidence that closes it, such as an executed no-training clause, an export of the verified retention setting, an approved recording notice, a confirmed subprocessor scope, or a recorded decision on a disabled feature. Each links to its action.

| # | Condition | Evidence that closes it | Action | Status |
|---|---|---|---|---|
| C1 | | | A… | Open |

## 9. Risk register

<Register block from ../../_shared/templates/risk-register.md: risks to individuals, with three ratings and control statuses. A term the vendor hasn't signed is a planned control, not an implemented one.>

## 10. Action plan

<Action plan block from ../../_shared/templates/action-plan.md, including vendor requests, configuration changes, verify flags, objection deadlines, and the reassessment date (an action, not a calendar event).>

## 11. Sign-off

<Sign-off block from ../../_shared/templates/approval-record.md, routed by the current residual rating, plus:>

| Item | Name and role | Date | Notes |
|---|---|---|---|
| Roles confirmed | | | |
| Vendor request list approved to send | | | External communication |
| Legal or Procurement review of company-side findings | | | |
| Onboarding authorized | | | Only once blockers are Done with evidence |

## 12. Follow-on records

- RoPA entries to update: <links or TBC>
- DPIA screening recommended: <yes or no, why>
- AI impact assessment recommended: <yes or no, why>
- Next reassessment: <date> (action A…)

## Appendix: ticket import

<Only when no ticketing tool is connected.>
