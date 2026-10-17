# Controls and evidence test scenarios

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "Sales wants AIUC-1 certification for Ava by Q2. Here's the agent description and our SOC 2 controls. Where are we?" | AIUC-1 readiness |
| 2 | "Which frameworks does our Okta MFA control satisfy?" | Map a control |
| 3 | "An enterprise customer's questionnaire asks for evidence of access reviews and encryption. What do we send?" | Questionnaire evidence pack |
| 4 | "Build our control library from the SOC 2 report and our policies." | Library build |
| 5 | "What tests and reviews are due this quarter?" | Schedule |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "How mature is our privacy program against NIST PF?" | `program-assessment` |
| 2 | "Review the model provider's DPA." | `vendor-review` |
| 3 | "Is Ava high-risk under the EU AI Act?" | `ai-intake` |
| 4 | "Write our AI acceptable use policy." | `notice-and-policy` |

## What a good run looks like

- Records controls as specific practices with owners, frequency, and scope, mapped to CCO objectives and so to frameworks.
- Judges evidence for operation, period, and scope. A SOC 2 test covers its period only, and a policy shows design.
- Generates the Statement of Applicability with `make_checklist.py aiuc-1 soa`, excluding mandatory requirements only by missing capability, with a justification.
- Labels coverage Covered, Partly covered, Not covered, or Not applicable (Provisional).
- Finds the third-party testing gap (A009, B001, C010, D004, E018) and schedules it as controls with next_test dates, never calendar events.
- Doesn't claim certification or conformity. Readiness only.
- Rebuilds the control index and `schedule.md`.
- Replies in about 150 words.
