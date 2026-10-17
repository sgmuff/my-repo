# Notice and policy test scenarios

## Should trigger

| # | Request |
|---|---|
| 1 | "Review our privacy notice against what we actually do." |
| 2 | "Does our notice cover the new call recording?" |
| 3 | "Write an AI acceptable use policy for employees." |
| 4 | "We need an acceptable use policy for customers of our AI agent, for AIUC-1." |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "A parent wants a copy of their child's data." | `dsr-response` |
| 2 | "Add the call recording activity to our RoPA." | `ropa` |
| 3 | "Draft the breach notice letter to affected customers." | `incident-assessment` |

## What a good run looks like

- Gathers the notice and the records of practice (RoPA, AI inventory, vendor reviews) before comparing.
- Compares in both directions: said but not done, done but not said, and out of date.
- Turns unknown practices into questions, not invented wording.
- Separates notice fixes from practice problems, and routes practice problems to the right skill.
- For AI acceptable use policies, picks the employee or product policy and drafts from facts, leaving unknowns TBC.
- Saves drafts to `policies/` and routes for approval; never publishes.
- Replies in about 150 words.

## Scenario runs

See `evals.json` for the prompts, fixtures in `files/`, and expected outputs.
