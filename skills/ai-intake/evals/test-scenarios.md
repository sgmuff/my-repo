# AI intake test scenarios

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "Sales turned on the AI call coach in our CRM last month. It scores reps on talk ratio and 'confidence.' Do we need to do anything?" | Embedded AI feature already live; employee evaluation; possible emotion inference |
| 2 | "Can we use ChatGPT Enterprise for drafting customer support replies?" | New AI use |
| 3 | "We want to build an agent that can issue refunds up to $200 on its own." | Own agent with transact permissions |
| 4 | "Build our AI inventory. Here's the list of tools from the expense report." | Inventory build |
| 5 | "Is our essay feedback tool high-risk under the EU AI Act?" | Classification question |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Run a full bias and human oversight assessment on TalentRank before launch." | `ai-impact-assessment` |
| 2 | "Review OpenAI's enterprise terms." | `vendor-review` |
| 3 | "Write our AI acceptable use policy." | `notice-and-policy` |
| 4 | "Does the churn model need a DPIA?" | `dpia` |

## What a good run looks like

- Records function by inputs, outputs, and use, and asks for samples; doesn't accept labels.
- Records that a live feature needs containment first.
- Classifies under the AI Act by function, checks every Art. 5 practice now, marks roles Provisional.
- Proposes a tier from the highest factor, with the fact behind each factor; Tier 0 is a stop said first.
- Sets the AIUC-1 mode and capability tags; lists follow-ons with skills, without running them.
- Saves under `registers/ai-inventory/` and rebuilds the index with the shared script.
- Replies in about 150 words.
