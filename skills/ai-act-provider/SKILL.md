---
name: ai-act-provider
description: Answer what the EU AI Act requires of a company as the provider of an AI system it builds or sells under its own name, and record it as a provider file - whether the system is high-risk under Art. 6, the documented Art. 6(3)-(4) assessment when an Annex III system is claimed not to be, and the high-risk provider obligations, from risk management to conformity assessment and post-market monitoring, with their status and evidence. Use it whenever someone asks whether their own AI product is high-risk, what they need before placing it on the EU market, how to get ready for conformity assessment or CE marking, or `gov required` or triage lists provider readiness, even if they don't say "AI Act." Not for deciding whether a use is AI or tiering it (ai-intake), using someone else's AI system (ai-act-deployer), fairness and impact reviews or FRIAs (ai-impact-assessment), or general-purpose AI model duties alone (eu-ai-act-gpai.md via ai-intake).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# AI Act provider files

This skill answers what the AI Act requires of a provider for one AI system, and records the answer as a provider file a market surveillance authority or notified body can read. The record is one YAML file, rendered to Markdown in a fixed format.

**Answer first, then record.** The legal analysis is yours, as full and as careful as you would give without this skill. The record captures it; it doesn't shape it. Never write or edit the `.md` file; `gov` writes it.

**The file proposes; the privacy or AI governance lead decides.** Give a provisional view on every answer. Never present a system as not high-risk, or as ready, before the facts that decide it are known; the provider's signatory signs the declaration of conformity, not this file.

## Files

| File | Read it when |
|---|---|
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Step 2: timeline (section 2), roles (3), risk categories and Art. 6 (4), Annex III (5), provider obligations (6), transparency (8) |
| [`../_shared/references/eu-ai-act-gpai.md`](../_shared/references/eu-ai-act-gpai.md) | Step 2, if the system is or includes a general-purpose AI model |
| [`../_shared/conventions.md`](../_shared/conventions.md) | Step 3 |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 5 |

## Workflow

### 1. Check the tool and the role

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. If the company uses another company's system under that company's name, it's a deployer: use `ai-act-deployer`. If the system isn't yet in the AI inventory, say `ai-intake` should record it.

### 2. Answer the question

Answer the request as a careful AI Act lawyer would, before you open any template: the system's intended purpose; whether it's high-risk through Annex I or Annex III; if Annex III, whether an Art. 6(3) condition applies, remembering that profiling natural persons always makes it high-risk; any Art. 5 prohibition; which provider obligations follow, what's in place, and what's missing; Art. 50 transparency where people interact with it or see generated content; the data protection overlap; when each obligation applies; and your provisional view with the facts that would change it. Then read the reference sections listed above and add anything your answer missed; don't cut what it already covers. Mark each point you can't check against a source, especially dates, as one to verify.

### 3. Record it

Run `gov new aip --slug <short-slug> --title "<system name>" --date <today>`, and set `kind`: `high-risk`, or `non-high-risk` for an Annex III system documented as not high-risk under Art. 6(3)-(4). Set `context` to every tag in `gov/rules/issues.yaml` that fits the facts.

Fill in the record from your answer. Put its reasoning in `analysis`, condensed to 400 words. Fill in `classification`, `application_date`, and one row per obligation with its status, the evidence or what's missing, and an owner; mark an obligation `not-applicable` only with the reason as evidence. Each call stays Provisional. If a point doesn't fit a field, it goes in `analysis`; the record never changes your conclusion. Add a verify flag for each point to verify.

### 4. Validate and render

Before validating: mark an action `block_reason: law` only when a provision requires that action before the system is placed on the market or used, and cite it in `scope` (`gov validate` rejects a law block without one). Gathering facts, verifying a point, or getting counsel's view is `risk` or `policy`. Run `gov validate`, fix errors, and resolve findings by changing the record. For each issue it raises, record in `issues` how your answer deals with it: `addressed` with the conclusion, `not-applicable` with why, or `open` with what's needed. If `gov` raises an issue your answer missed, deal with it in the answer too. Don't add a `finding_responses` entry yourself; only a person decides a finding doesn't apply. Validation checks structure and consistency, not legal correctness. Run `gov render`.

### 5. Reply

The privacy or AI governance lead decides the classification and readiness (`approvals.md`). Send the answer from step 2, as you amended it, to the requester: in plain English, as long as the answer needs and no longer. Say what has to happen before launch in ordinary words, grouped as legal requirements, risks, and internal policy, and ask the questions, five at most, that would change the answer. Give a date only when the request, a contract, or the law sets it. Keep the record out of the reply: no record or action IDs, field names, or counts of findings and flags, apart from one closing line naming the record and its path.
