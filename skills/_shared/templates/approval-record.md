# Approval record

Two blocks: the sign-off table that goes at the end of each deliverable, and the row format for the approval log. Rules are in `approvals.md`. Delete these instructions when you use them.

---

## Sign-off (end of each deliverable)

| Decision | Approver role (per `approvals.md`) | Name | Date | Decision | Conditions or notes |
|---|---|---|---|---|---|
| Legal determinations in this document | Privacy lead | | | Confirmed, Changed, or Rejected | |
| Residual risk acceptance (**<rating>**) | <Privacy lead / Privacy lead and business owner / Executive risk approver> | | | Accepted, Accepted with conditions, or Not accepted | |
| Requesting business area acknowledgment | <Business area> contact | | | Acknowledged | |
| System owner acknowledgment (if different) | <System owner> | | | Acknowledged | |
| External communication, if any | Privacy lead | | | Approved to send, or Not approved | |

The skill fills in the role column and leaves the rest blank until a person records a decision.

---

## Approval log row

The log lives at `<output root>/approvals/approval-log.md`. If it doesn't exist, create it with this header:

```markdown
# Approval log

| Date | Document ID | Document | Decision type | Decision | Approver (name, role) | Channel | Recorded by | Conditions |
|---|---|---|---|---|---|---|---|---|
```

Then add one row per decision:

| Date | Document ID | Document | Decision type | Decision | Approver (name, role) | Channel | Recorded by | Conditions |
|---|---|---|---|---|---|---|---|---|
| 2026-10-20 | DPIA-2026-004 | [Support Copilot DPIA](../assessments/dpia/2026-10-16-support-copilot.md) | Residual risk acceptance (Medium) | Accepted with conditions | Jane Doe, Privacy Lead | Claude session | Claude, at Jane Doe's instruction | A1–A4 complete before launch |
