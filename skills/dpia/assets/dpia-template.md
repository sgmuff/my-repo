---
id: DPIA-YYYY-NNN
type: dpia            # or dpia-assistance-pack (see references/assistance-pack.md)
title: <Activity name>
status: Draft
stage: Draft complete   # Screening complete | Draft complete | Ready for sign-off | Authorized to launch
version: 0.1
requesting_business_area: <business area>
system_owner: <team or person, if different>
prepared_by: Claude (privacy-governance suite), for <privacy lead>
date_prepared: YYYY-MM-DD
next_review: YYYY-MM-DD
roles: {gdpr: <proposed role> (provisional), us_state: <...>, ferpa: <n/a | school official | ...>, eu_ai_act: <n/a | provider | deployer> (provisional)}
regimes: [GDPR, UK GDPR, FADP, EU AI Act, FERPA, COPPA, CA, CO, ...]
residual_risk: {current: <rating>, target: <rating>, confirmed: false}
launch_authorized: false
references:
  - <file> (<version covered>), last verified YYYY-MM-DD
tickets: []
---

<For an assistance pack going to a customer, the first body line is: DRAFT: not sent>

# Data protection impact assessment: <Activity name>

## Document control

| Field | Value |
|---|---|
| DPIA ID | |
| Status | Draft |
| Activity, ticket, or PRD | |
| Requesting business area | |
| System owner | |
| Technical owner | |
| Proposed roles | Per operation: GDPR … · US states … · FERPA … · EU AI Act … (all Provisional until confirmed in §11) |
| Planned start of processing | |
| Related records | RoPA entry, vendor reviews, AI impact assessment or FRIA, TIA, LIA, previous DPIA (link each one) |
| Reference files relied on | <file, version covered, last verified>. Note any file overdue, or due for review before launch. |

### Version history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | | | First draft |

## 1. Executive summary

> **DPIA status:** Draft, not approved. Stage: <stage>.
> **Screening:** <Warranted | Recommended | Not indicated> (<Provisional | Confirmed>; depends on F…).
> **Residual risk:** not yet confirmed. Current: **<rating>** (<verified controls, or "none verified">). Target: **<rating>**, subject to verification of A….
> **Prior consultation:** <e.g., "Not required if the target is achieved and verified; revisit when A… closes." (Provisional)>
> **Launch decision:** Not authorized by this draft. Production processing must not begin until the approver named in §11 has reviewed the completed assessment, confirmed the legal determinations and roles, verified the launch-blocking actions with evidence, and recorded the residual-risk decision.
> **Other regimes:** <each with its status, e.g., "CA CPPA risk assessment: Open (F4)">.

<Then, in short paragraphs that open with their conclusion:
- What the processing is and why the company is doing it (2–3 sentences)
- The facts that drive the screening and risk conclusions, and which are unverified
- The top conditions for going ahead (action IDs)
- Separate approval for any secondary purpose, such as model training

Define the legal terms on first use here.>

> **Decision needed:** <The determinations and the risk acceptance this document asks for, and the approver for each, per approvals.md.>

## 2. Fact register

| # | Fact | Status | Evidence or source | Owner | Needed by | Blocks launch? | Effect if unresolved |
|---|---|---|---|---|---|---|---|
| F1 | | Confirmed, Stated by requester, Unverified assumption, or TBC | | | | | |

### 2a. Verification register

| # | Claim being checked | Why it matters | Source to check | Owner | Blocks launch? | Action |
|---|---|---|---|---|---|---|
| V1 | | | | *(proposed)* | | A… |

A flagged point is something to check, not a confirmed defect.

## 3. Screening

<Screening table from references/screening.md §6, starting with territorial scope, each row with supporting facts and status. Then the outcome paragraph, written as a judgment about likely high risk.>

## 4. Description of the processing (Art. 35(7)(a))

### 4.1 Nature, scope, context, and purposes

<One row per processing operation, with its purpose and the proposed role for each party.>

### 4.2 Data subjects

| Category | Approx. number | Regions | Vulnerable? | Children (under 13?) or students? |
|---|---|---|---|---|

### 4.3 Personal data inventory

| Data element | Category | Special category, biometric (which kind), criminal, US-sensitive, or education record? | Source | Purpose | Retention and justification | Needed? (see §6.2) |
|---|---|---|---|---|---|---|

### 4.4 Data flow

<Short numbered flow from collection to deletion. Add a Mermaid diagram if it helps.>

### 4.5 Recipients, processors, and subprocessors

| Recipient | Proposed role, per operation | Service | Data | Location | DPA (evidence) | Assurance | Own-purpose use? | Vendor review |
|---|---|---|---|---|---|---|---|---|

### 4.6 International transfers

| From | To | Recipient | Mechanism (verified for this entity and destination?) | TIA on file | Supplementary measures |
|---|---|---|---|---|---|

### 4.7 Retention and deletion

### 4.8 Security measures

<Point to the standard baseline in the company profile. List the controls specific to this activity, each marked implemented and evidenced, implemented but unverified, planned, or absent.>

## 5. Consultation

| Party | Date | Input (advice, not decision) | How it was addressed |
|---|---|---|---|
| DPO or counsel (Art. 35(2)) | | | |
| Data subjects or their representatives (Art. 35(9)) | | | |
| Requesting business area | | | |
| Security | | | |
| Processors | | | |

## 6. Necessity and proportionality (Art. 35(7)(b))

<For an assistance pack, mark 6.1, 6.3, and 6.8 "Controller to complete," and list the facts the controller will need.>

### 6.1 Lawful basis
<Per purpose: the Art. 6 basis, plus an Art. 9 condition where needed. Each secondary purpose separately.>

### 6.2 Data minimization
### 6.3 Purpose limitation and compatibility
### 6.4 Transparency
### 6.5 Data subject rights
### 6.6 Profiling and automated decisions
<Two analyses, recorded separately (gdpr.md §6): (1) Is there profiling under Art. 4(4)? (2) Is there an Art. 22 decision: solely automated, with legal or similarly significant effects, tested against real consequences? Then the safeguards and their evidence.>
### 6.7 Retention
### 6.8 Assessment

| Principle | Assessment | Status | Citation | Gap and linked action |
|---|---|---|---|---|
| Lawfulness | Adequate, Gap, or Not met | Provisional, Confirmed, or Open | Art. 6 | |
| Minimization | | | Art. 5(1)(c) | |
| Purpose limitation | | | Arts. 5(1)(b), 6(4) | |
| Transparency | | | Arts. 13–14 | |
| Rights | | | Arts. 15–22 | |
| Accuracy | | | Art. 5(1)(d) | |
| Storage limitation | | | Art. 5(1)(e) | |
| Transfers | | | Arts. 44–49 | |

## 7. Risk register (Art. 35(7)(c)–(d))

<Register block from ../../_shared/templates/risk-register.md, with inherent, current residual, and target residual ratings. For an assistance pack, split the target into vendor residual and deployment residual.>

## 8. Prior consultation

<Judge on the current residual rating (gdpr.md §10).

If no current rating is High: "No current residual risk is rated High. Prior consultation under GDPR Art. 36 (or UK GDPR Art. 36 or FADP Art. 23) is not required on current facts." (Provisional.)

If a High drops only in the target: "Prior consultation is not required if the target residual rating is achieved and verified. Revisit when A… closes." (Provisional.)

If a current or target rating is High:

> **Blocker:** Prior consultation may be required. R<n> remains High. Processing must not start until the consultation is complete, or the risk is brought down to Medium or lower and verified.

For an assistance pack: "This pack doesn't determine whether a controller must consult. Each controller decides after its own assessment.">

## 9. Other regimes

<For each regime: does the law apply to the company, and does this activity trigger an obligation, with the provision and status. Use the crosswalk in ../../_shared/references/us-state-privacy.md §5.>

### 9.1 Benefit-risk weighing
### 9.2 Regime-specific content (US states)
### 9.3 Student data: FERPA, COPPA, and state student privacy laws (if applicable)
<Exception relied on and the facts showing its conditions are met; use and redisclosure limits; users under 13 and the consent basis; state student privacy law duties per customer state; each institution's authorization for each use.>
### 9.4 EU AI Act (if applicable)
<Role (Provisional), classification by documented function, any Art. 5 prohibition analysis, each Art. 50 paragraph, and a link to the separate AI impact assessment or FRIA.>

## 10. Action plan

<Action plan block from ../../_shared/templates/action-plan.md: dependencies, acceptance criteria, evidence, and dates sequenced so that every launch blocker and legality-affecting verification is due before launch. Include one action per verify flag. Review dates are actions, not calendar events.>

## 11. Sign-off

<Sign-off block from ../../_shared/templates/approval-record.md, routed by the current residual rating, plus these DPIA-specific rows:>

| Item | Name and role | Date | Notes |
|---|---|---|---|
| Roles confirmed | | | Changes from the proposed roles |
| DPO or counsel advice provided | | | |
| Summary of advice | | | |
| Advice accepted or overruled | | | If overruled, give the reasons |
| Consultation responses reviewed by | | | If the decision departs from data subjects' views, give the reasons |
| CA executive attestation (if applicable) | | | |
| Launch authorized | | | Only once the launch blockers are Done with evidence |
| Kept under review by | | | |

## 12. Review

- **Next scheduled review:** <the strictest applicable cadence>, recorded as an action in §10
- **Triggers for an early review:**
  - A new data category, purpose, vendor, or region
  - A model change
  - An incident
  - A regulatory change, including a new release of a framework cited above
  - Under California rules, any material change (update within 45 days)
  - Closure of the actions a target rating depends on (re-rate the current residual)

## Appendix: ticket import

<Only when no ticketing tool is connected: the CSV block from the action plan template.>
