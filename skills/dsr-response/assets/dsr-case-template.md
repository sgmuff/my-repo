---
id: DSR-YYYY-NNN
type: dsr
status: Draft          # Draft | Awaiting verification | In progress | Forwarded | Responded | Closed
received: YYYY-MM-DD   # date the request reached the company
earliest_deadline: YYYY-MM-DD
extended_deadline:     # set only if an extension notice went out before earliest_deadline
internal_target:       # optional company target, earlier than the statutory deadline
responded: YYYY-MM-DD  # date the response went out; set when sent, for leadership metrics
closed: YYYY-MM-DD     # date the case closed
request_types: [access, deletion]
requester_type: <data subject | parent or guardian | authorized agent>
company_role: <controller | processor (forwarded) | school official (forwarded)> (provisional)
laws: [GDPR, CCPA]
verification: <not started | requested | verified by NAME on DATE | failed>
prepared_by: Claude (privacy-governance suite), for <privacy lead>
references:
  - dsr-matrix.md (as of 2026-10-16), last verified 2026-10-16
tickets: []
---

# Data subject request: DSR-YYYY-NNN

> **Earliest deadline: YYYY-MM-DD** (<which law, which step>). Next step: <send acknowledgment draft for approval>.

## 1. Request

| Field | Value |
|---|---|
| Received (date, time, channel) | |
| Requester (as identified) | <keep to what's needed> |
| Requester's words | "<quote>" |
| Request types | |
| Earlier requests from this person | <IDs, or none found> |

## 2. Role and applicable law

| Question | Answer | Status | Basis |
|---|---|---|---|
| Company role for this person's data | | Provisional | `dsr-matrix.md` §1 |
| GDPR, UK GDPR, or FADP applies? | | | Art. 3; residency; establishment |
| US state law applies? Which? | | | Residency; thresholds; exemptions |
| FERPA or COPPA applies? | | | |

## 3. Deadlines

Output of `gov deadlines`, with public holidays checked by hand. These are actions, not calendar events.

| Due | Step | Law | Statutory or internal target |
|---|---|---|---|
| | Acknowledge | | |
| | Respond | | Statutory |
| | Respond if extended (notice needed by the first deadline) | | Statutory |

## 4. Verification

| Item | Value |
|---|---|
| Method proposed | <account login, email confirmation, matching data points, signed declaration, agent permission> |
| Why it's proportionate | |
| Verified by, date, outcome | <filled in by a person> |

## 5. Where the data is

| System or activity (RoPA ID) | Data held | Search owner | Searched on | Result |
|---|---|---|---|---|

Processors that must act:

| Processor | Instruction (delete, correct, export) | Sent on | Confirmed on |
|---|---|---|---|

### 5a. Access response checklist (GDPR Art. 15)

| Item | Ready? | Source |
|---|---|---|
| Confirmation that data is processed | | |
| Copy of the personal data (with redactions recorded) | | |
| Purposes | | |
| Categories of data | | |
| Recipients, including in third countries | | |
| Retention period or criteria | | |
| Rights, and the right to complain | | |
| Source, if not collected from the person | | |
| Automated decision-making: logic, significance, consequences | | |
| Transfer safeguards | | |

## 6. Position for each request

| Request | Proposed action | Exception relied on (provision) | Status | Redactions |
|---|---|---|---|---|

> **Decision needed:** <any refusal, partial refusal, exception, fee, or extension, for the privacy lead (approvals.md)>

## 7. Messages

| Message | Draft location | Approved by | Sent on | Sent by |
|---|---|---|---|---|
| Acknowledgment | | | | |
| Verification request | | | | |
| Extension notice | | | | |
| Response | | | | |

## 8. Follow-ons

<Gaps found: systems missing from the RoPA, processors that couldn't delete, notice gaps.>

## 9. Closure

| Item | Value |
|---|---|
| Closed on | |
| Outcome summary | |
| Verification data deleted on | |
| Retain case record until | <closing date + 24 months> |
