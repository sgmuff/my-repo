# AI impact assessment test scenarios

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "Run the AI impact assessment on TalentRank before we launch it in January. Validation summary attached." | Full AIIA for Annex III employment use |
| 2 | "Our university customers want FRIA input for the proctoring tool." | FRIA input pack (provider) |
| 3 | "Is our essay grader fair across English learners? We have test results." | Fairness section with evidence |
| 4 | "Do a pre-launch AI review of the refund agent." | AIIA for an autonomous agent |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Can we use Copilot for code?" | `ai-intake` |
| 2 | "Does the churn model need a DPIA?" | `dpia` |
| 3 | "Review Hirewise's contract." | `vendor-review` |

## What a good run looks like

- Starts from the inventory entry (or runs intake first) and confirms scope, roles, and classification as Provisional.
- Asks a short Round 1 with an "Evidence requested" group.
- Assesses each section in scope against evidence, labels findings Confirmed, Unverified, or Recommended, and cites AIUC-1 (with release), AI Act, NIST AI RMF, and ISO/IEC 42001.
- Treats automatic de-prioritization and nominal human review as oversight gaps, with remedies.
- Rates three ratings with reach, reversibility, and autonomy, and names who is affected.
- States the launch gate, decides FRIA (deployer, case by case) or input pack (provider), and keeps the AIIA separate from the DPIA.
- Puts AIUC-1 quarterly testing in the action plan for readiness mode. No calendar.
- Replies in about 150 words.
