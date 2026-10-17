# Action plan block

Paste this section into any deliverable with follow-up work. Delete these instructions when you use it.

- Number actions `A1`, `A2`, and so on, and link each one to the risks, gaps, facts, or verify flags it addresses.
- Every action needs an owner and a due date. If the user didn't give them, propose a role (for example, "Eng lead, Support Platform") and a date tied to launch or review, and mark both *proposed*.
- Every verify flag becomes an action, with the source to check.
- **Sequence the dates.** An action is never due before the action it depends on. Every launch blocker and every legality-affecting verification is due before launch.
- **"Done" means verified.** An action closes when its evidence shows the safeguard operating as intended, not when a policy is drafted or a setting is proposed.
- Review dates and deadlines are actions here. Don't put them on a calendar (`connectors.md`).
- Fill in "Ticket" once the action is in Jira or ServiceNow. Leave it blank otherwise.

---

## Action plan

| ID | Action | Addresses | Depends on | Acceptance criterion | Owner | Due | Launch blocker? (Legal or Readiness) | Evidence link | Verified by | Ticket | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | | R1, F2 | — | | *(proposed)* | YYYY-MM-DD *(proposed)* | Yes, Legal | | | | Open |

Status values: Open, In progress, Done (only with evidence and a verifier), Won't do (with the reason and the approver who accepted the remaining risk).

State which actions are launch blockers and which aren't in a sentence below the table, so the count matches the table.

### Ticket import (appendix, only when no ticketing tool is connected)

```csv
Summary,Description,Due date,Labels
"[<doc ID> A1] <action>","Addresses R1. Acceptance: <criterion>. See <document path>",YYYY-MM-DD,privacy
```
