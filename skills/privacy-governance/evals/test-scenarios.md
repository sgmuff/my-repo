# Triage test scenarios

The router should catch requests that span workflows or name none, and stay quiet when one skill clearly fits. The trigger lists are also in `trigger-evals.json`.

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "We're buying an AI note-taker that records student tutoring sessions. What do we need to do?" | Vendor review, AI intake, DPIA, and RoPA, in order |
| 2 | "Legal says we need to look at the new analytics thing before it ships. Where do I start?" | No workflow named |
| 3 | "We're launching in Germany next quarter with a new payments partner and a chatbot. What's our privacy to-do list?" | New market, vendor, and AI together |
| 4 | "We acquired a small edtech company. What privacy work do we need to do on their systems?" | Program-level triage across records, vendors, and assessments |
| 5 | "Marketing wants to start using an AI tool to score leads from LinkedIn data. Is that OK?" | AI intake, vendor review, DPIA screening, and notice |

## Should not trigger (one skill clearly fits)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Review this DPA against Article 28." | `vendor-review` |
| 2 | "Do we need a DPIA for the churn model?" | `dpia` |
| 3 | "Add the webinar signup flow to the RoPA." | `ropa` |
| 4 | "What's GDPR Article 28(3)(h)?" | A direct answer; no workflow |

## What a good run looks like

- Restates the request as activities on personal data.
- Asks only the deciding facts (usually under eight), proposing answers it can infer.
- Puts time-critical items first (running breach clocks, DSR deadlines, objection windows), and is candid when the skill for them isn't built yet.
- Produces a one-screen plan: steps in dependency order, why, what each depends on, and the human decision after each.
- Recommends only installed skills; names planned ones as not yet available, with an interim step.
- Doesn't make legal determinations in the plan, and states that nothing in it authorizes processing.
- Offers to start step 1, and carries the facts forward when it does.
