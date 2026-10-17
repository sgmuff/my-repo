# Leadership report test scenarios

## Should trigger

| # | Request |
|---|---|
| 1 | "Write the Q3 privacy update for the board." |
| 2 | "Give me a KRI dashboard for the audit committee." |
| 3 | "Summarize where the privacy and AI program stands for the exec team." |
| 4 | "How many DSRs did we miss the deadline on this quarter? It's for the CFO." |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Score our program maturity against NIST PF." | `program-assessment` |
| 2 | "Build the AIUC-1 audit evidence pack." | `controls-and-evidence` |
| 3 | "What does the new AI Act amendment mean for us?" | `regulatory-change` |

## What a good run looks like

- Runs `program_metrics.py` and uses its numbers, each traceable to a record.
- Compares with the previous report.
- Describes top risks in business terms, with record IDs.
- Never claims compliance, certification, or conformity, even when asked.
- Respects privilege on incidents and leaves out personal data.
- Lists decisions needed and data gaps.
- Saves the draft to `reports/` for the privacy lead's and counsel's review.
- Replies in about 150 words.

## Scenario runs

See `evals.json` for the prompts, fixtures in `files/`, and expected outputs.
