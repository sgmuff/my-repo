---
id: INC-YYYY-NNN
type: incident
title: <short neutral description>
status: Open          # Open | Notifications in progress | Monitoring | Closed
aware_at: YYYY-MM-DDTHH:MM <zone>
earliest_deadline: YYYY-MM-DD HH:MM <zone>
personal_data_breach: <yes | no | TBC> (provisional)
company_role: <controller | processor | school official | mixed> (provisional)
individuals_affected: <number or TBC>
regimes: [GDPR, CA, NY]
notified: []          # recipients notified, with dates
prepared_by: Claude (privacy-governance suite), for <privacy lead>, at the direction of counsel <name>
privilege: <marking directed by counsel, or "none directed">
breach_reference_reviewed_by_counsel: <yes, by NAME on DATE | no>
references:
  - us-breach-notification.md (as of 2026-10-16; draft reference), last verified 2026-10-16
  - gdpr.md, last verified 2026-10-16
---

# Incident record: INC-YYYY-NNN

> **Earliest deadline: YYYY-MM-DD HH:MM <zone>** (<recipient and basis>).
> **Next decision:** <for example, "Counsel and privacy lead: notify the lead supervisory authority?">
> <If the breach law reference hasn't been reviewed by counsel:> **Blocker:** The state breach law reference hasn't had its counsel review. Every state conclusion below needs counsel's confirmation before notices go out.

## 1. Timeline

| Time (with zone) | Event | Source |
|---|---|---|
| | Incident began (if known) | |
| | Detected | |
| | Company became aware (the clock starts here; reasoning: …; confirmed or assumed?) | |
| | Reported internally | |
| | Counsel engaged | |
| | Insurer notified | |

## 2. Facts

| # | Fact | Status | Source | Learned at |
|---|---|---|---|---|
| F1 | | Confirmed, Stated by …, Unverified assumption, or TBC | | |

### 2a. Verification register

| # | Claim being checked | Why it matters | Source to check | Owner | Blocks a notice? |
|---|---|---|---|---|---|

## 3. Data and people

| Data element | Encrypted (key safe?) | Acquired or accessed | People affected | By jurisdiction |
|---|---|---|---|---|

## 4. Role

| Data set | Company role | Who notifies whom | Basis |
|---|---|---|---|

## 5. Assessment

### 5.1 GDPR, UK GDPR, FADP

| Question | Answer | Status | Basis |
|---|---|---|---|
| Personal data breach? | | | Art. 4(12) |
| Awareness time and reasoning | | | EDPB Guidelines 9/2022 |
| Authority notice (unless unlikely to result in a risk) | | | Art. 33(1) |
| Individuals (likely high risk; exceptions) | | | Art. 34 |

Risk factors (`references/risk-factors.md`): <each factor, one line>

### 5.2 US states

| State | Covered data? | Breach under statute? | Safe harbor? | Risk-of-harm allowed and supports no notice? | Duty | Status |
|---|---|---|---|---|---|---|

### 5.3 Student data, AI, and sector laws

<FERPA and institution contracts; AI Act Art. 73 and AIUC-1 failure plans; federal and sector laws flagged for counsel.>

## 6. Notification matrix

Clock output from `gov clock`, plus contractual deadlines. Deadlines are actions, not calendar events.

| Recipient | Regime or contract | Required? (status) | Deadline (statutory or contractual) | Content rules | Method or form | Draft | Approved by | Sent on, by |
|---|---|---|---|---|---|---|---|---|

> **Decision needed:** <each notify or don't-notify decision, for counsel and the privacy lead>

## 6a. Decision log

| Time (zone) | Decision | Decided by | Evidence relied on | Rationale |
|---|---|---|---|---|

## 6b. Delivery tracking

| Recipient | Sent at | Method | Sent to | Delivery confirmed? |
|---|---|---|---|---|

## 6c. Technical containment (owned by security)

| Measure | Status (done and verified, done unverified, in progress) | Evidence | Remaining access paths |
|---|---|---|---|

## 7. Actions

<Action plan block from ../../_shared/templates/action-plan.md, with Legal or Readiness labels.>

## 8. Documentation (GDPR Art. 33(5))

<The facts, effects, and remedial action, recorded whether or not the breach was notified.>

## 9. Closure and lessons learned

| Item | Value |
|---|---|
| Closed on | |
| Root cause (from security) | |
| Follow-ons | DPIA rescreen, vendor reassessment, RoPA updates, notice changes, AIUC-1 failure-plan updates |
