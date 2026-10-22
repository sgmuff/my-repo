# Incident assessment test scenarios

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "A support agent emailed a CSV of 1,200 customers to the wrong customer an hour ago. Names, emails, last 4 of card. Mix of EU and US. What now?" | Misdirected disclosure; controller; GDPR and states |
| 2 | "We got hit by ransomware last night. The attackers say they took the student database. We host it for districts in New York and California." | Processor or school official; NY Ed Law 2-d 7 days; controllers notify |
| 3 | "Our helpdesk vendor says they had unauthorized access to tickets in September and just told us." | Vendor breach; awareness timing; controller duties |
| 4 | "An employee's laptop was stolen from their car. It had an unencrypted export of payroll data." | Lost device; SSNs; credit monitoring states |
| 5 | "Our support chatbot showed one customer's order history to another customer." | AI incident and personal data breach |
| 6 | "Do we have to notify anyone? Someone accessed an S3 bucket but we don't think they downloaded anything." | Access versus acquisition; states that cover access |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "A customer asked us to delete their data." | `dsr-response` |
| 2 | "Write our incident response plan." | A policy task (`notice-and-policy` or security) |
| 3 | "Review the breach notification clause in Acme's DPA." | `vendor-review` |
| 4 | "Which states have 30-day breach notification deadlines now?" | `regulatory-change` or a direct answer |

## What a good run looks like

- **Starts the clock first:** records the awareness time with zone and reasoning, runs `gov clock`, and leads with the earliest **working** deadline, stated with the awareness time it assumes. Sets internal milestones ahead of outer limits.
- Names an incident commander, runs technical containment in parallel with security, and never lets evidence preservation delay containment.
- Says "don't send unreviewed external notices," never "don't contact anyone yet."
- Keeps the US position "undetermined pending review" until fields, state counts (including unknown residence), definitions, and contracts are checked. Assesses Art. 34 separately. Leaves the EU authority route to counsel.
- Marks facts in drafts Verified, Estimated, Pending, or Planned, and keeps a decision log and delivery tracking.
- First reply: bring in counsel now (privilege), check insurance notice conditions, preserve evidence, don't speculate or contact anyone yet.
- Decides role first: a processor or school official notifies controllers or institutions (contract hours; NY 7 days), and doesn't notify individuals itself.
- Assesses GDPR (authority unless unlikely risk; individuals if high risk) with the EDPB factors, and each state separately (covered data, acquisition or access, safe harbor, risk-of-harm only where allowed).
- Builds a notification matrix with statutory and contractual deadlines, and flags sector laws for counsel.
- Drafts only the required notices, each "DRAFT: not sent," factual, no blame, meeting content rules (Art. 33(3), California format, Massachusetts restrictions).
- States the counsel-review blocker for the state reference.
- Saves under `incidents/YYYY/`, rebuilds the register, no calendar, reply about 150 words led by time.
