# Program assessment test scenarios

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "Do a NIST Privacy Framework assessment of our program from these notes. Where are we and what should we do first?" | Full profile, Tier, roadmap |
| 2 | "Does our program reasonably conform to the NIST PF for Tennessee's defense?" | Tennessee affirmative defense |
| 3 | "We want an ISO 42001 gap assessment before deciding whether to certify." | ISO variant |
| 4 | "Annual privacy program review is due. Compare to last year's." | Repeat assessment |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Map our MFA control to the frameworks." | `controls-and-evidence` |
| 2 | "Write the board's quarterly privacy update." | `leadership-report` |
| 3 | "Do we need a DPIA for the churn model?" | `dpia` |

## What a good run looks like

- Gathers evidence from the suite's registers and records first, then asks a short Round 1 for what they don't show.
- Generates the profile with `make_checklist.py nist-pf profile`, so all 100 subcategories appear.
- Sets the Target Profile by law, risk, commitments, and benefit, with reasons for exclusions.
- Rates the Current Profile on evidence, not policy, marking interview-only ratings Provisional and rating lower where evidence is thin.
- Rates the four Tier attributes, and names the one holding the Tier back.
- Ranks gaps on legal exposure, risk, dependency, and effort, and builds a quarterly roadmap with Legal and Readiness labels.
- Doesn't claim Tennessee conformity. Treats it as a determination for counsel.
- Replies in about 150 words.
