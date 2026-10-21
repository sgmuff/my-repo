---
name: ai-act-deployer
description: Answer what the EU AI Act requires of a company using someone else's high-risk AI system, and record it as a deployer check - whether the company has become the provider under Art. 25 by rebranding, substantially modifying, or repurposing the system, its Art. 26 duties, from human oversight and logs to telling workers and the people affected, AI literacy, Art. 50 transparency, the Art. 86 right to an explanation, and whether it owes a fundamental rights impact assessment under Art. 27. Use it whenever someone wants to use or keep using a vendor's AI system for hiring, credit, insurance, education, or another Annex III use, asks what deployers must do under the AI Act, or `gov required` or triage lists deployer duties, even without saying "deployer." Not for deciding whether a use is AI or tiering it (ai-intake), systems the company builds or sells under its own name (ai-act-provider), writing the FRIA itself or a fairness review (ai-impact-assessment), or the vendor's contract (vendor-review).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# AI Act deployer checks

This skill answers what the AI Act requires of a deployer of one high-risk AI system, and records the answer as a deployer check a market surveillance authority can read. The record is one YAML file, rendered to Markdown in a fixed format.

**Answer first, then record.** The legal analysis is yours, as full and as careful as you would give without this skill. The record captures it; it doesn't shape it. Never write or edit the `.md` file; `gov` writes it.

**The check proposes; the privacy or AI governance lead decides.** Give a provisional view on every answer, and never present the deployer as ready, or a FRIA as not owed, before the facts that decide it are known.

## Files

| File | Read it when |
|---|---|
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Step 2: timeline (section 2), roles and Art. 25 (3), Annex III (5), deployer duties and the FRIA (7), transparency (8) |
| [`../_shared/conventions.md`](../_shared/conventions.md) | Step 3 |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 5 |

## Workflow

### 1. Check the tool and the role

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. If the company builds or sells the system under its own name, it's a provider: use `ai-act-provider`. If the system isn't high-risk, say so with the reason; most deployer duties then don't apply, though Arts. 4 and 50 may.

### 2. Answer the question

Answer the request as a careful AI Act lawyer would, before you open any template: whether the system is high-risk and why; whether the company has become the provider under Art. 25; each deployer duty, what's in place, and what's missing; whether the company owes a FRIA, given its legal status and the Annex III point; the workplace, DPIA, and explanation duties where they apply; when the duties apply; and your provisional view with the facts that would change it. Then read the reference sections listed above and add anything your answer missed; don't cut what it already covers. Mark each point you can't check against a source, especially dates, as one to verify.

### 3. Record it

Run `gov new aid --slug <short-slug> --title "<system and use>" --date <today>`. Set `context` to every tag in `gov/rules/issues.yaml` that fits the facts, such as `employees` or `public-body`.

Fill in the record from your answer. Put its reasoning in `analysis`, condensed to 400 words. Fill in `provider`, `provider_role_check`, `fria`, `application_date`, and one row per duty with its status, the evidence or what's missing, and an owner; mark a duty `not-applicable` only with the reason as evidence. If any Art. 25 answer is yes, set the decision to `becomes-provider` and say a provider file is needed. Each call stays Provisional. If a point doesn't fit a field, it goes in `analysis`; the record never changes your conclusion. Add a verify flag for each point to verify.

### 4. Validate and render

Before validating: mark an action `block_reason: law` only when a provision requires that action before the system is placed on the market or used, and cite it in `scope` (`gov validate` rejects a law block without one). Gathering facts, verifying a point, or getting counsel's view is `risk` or `policy`. Run `gov validate`, fix errors, and resolve findings by changing the record. For each issue it raises, record in `issues` how your answer deals with it: `addressed` with the conclusion, `not-applicable` with why, or `open` with what's needed. If `gov` raises an issue your answer missed, deal with it in the answer too. Don't add a `finding_responses` entry yourself; only a person decides a finding doesn't apply. Validation checks structure and consistency, not legal correctness. Run `gov render`.

### 5. Reply

The privacy or AI governance lead decides whether the company is ready to use the system (`approvals.md`). Send the answer from step 2, as you amended it, to the requester: in plain English, as long as the answer needs and no longer. Say what has to happen before launch in ordinary words, grouped as legal requirements, risks, and internal policy, and ask the questions, five at most, that would change the answer. Give a date only when the request, a contract, or the law sets it. Keep the record out of the reply: no record or action IDs, field names, or counts of findings and flags, apart from one closing line naming the record and its path. If a FRIA is owed, say so first; `ai-impact-assessment` writes it.
