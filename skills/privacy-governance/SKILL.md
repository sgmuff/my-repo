---
name: privacy-governance
description: Triage privacy and AI governance requests that span several workflows, or that don't say which one they need, and plan the order to run them in. For example, a new AI tool that will touch customer or student data, a product launch with new vendors and data uses, an acquisition or new market, "where do I start," or "what do we need to do before we can use X." Produces a short triage plan that names the facts that decide the path, the skills to run in order, and the human decisions along the way. Use it when a request mixes vendor, assessment, records, AI, or policy work, or when it's unclear which privacy workflow applies. Skip it when the request clearly matches one skill, such as "review this DPA" (vendor-review), "do we need a DPIA for X" (dpia), or "add this to the RoPA" (ropa), and go straight to that skill.
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.9+, PyYAML, jsonschema, and Jinja2.
---

# Privacy and AI governance triage

This skill is the front door for requests that don't fit one workflow. It gathers the facts that decide the path, `gov route` turns them into a plan and a decision register, and the skill adds the legal issues the routing table can't see. Then it hands off. It produces no compliance deliverable of its own.

**`gov route` decides the steps; you spot the issues.** The routing table (`gov/rules/routing.yaml`) holds the steps, their order, and the legal checks the privacy lead approved, so the same facts always give the same plan. Don't reorder, add, drop, or reword its steps: two people asking the same question must get the same plan, and the plan must be auditable. The table can't foresee every issue, though. Your judgment goes in a separate, labeled section below it (step 4), never into the table.

Requests that clearly match one skill go straight to that skill. **Time-critical requests don't wait for triage:** a suspected breach goes straight to `incident-assessment`, and a data subject request with a running deadline goes straight to `dsr-response`.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | Always: roles, intake rounds, and determination status apply to triage too |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | Always, for the regimes in scope and the business areas |
| `gov/rules/routing.yaml` | For the facts it asks about, and why a step or check appears |

## Workflow

### 1. Check the tool and restate the request

Run `gov --version`. If it fails, stop and tell the user to run `skills/install.sh`. Don't build a plan by hand.

Restate the request as what will happen to personal data: what is bought, built, shared, or changed; for whom; and with what data.

### 2. Set the facts you can infer

The facts are the keys under `facts:` in `routing.yaml`. Set each one the request or its documents settle, including what the request plainly implies: sales contacting scored prospects is `direct_marketing: yes`, and an analytics SDK is `tracking_tech: yes`. Leave the rest `TBC`. Don't turn a hint into a fact: a US vendor makes `cross_border_access` worth asking about, not yes. Never set `lawful_basis` unless someone already proposed one: choosing it is a decision for the controller, not an intake answer.

### 3. Run the router

```bash
gov route - --format markdown <<'EOF'
processing_started: no
vendor_involved: yes
ai_involved: yes
children_or_students: yes
new_processing: yes
EOF
```

Use only the keys `routing.yaml` defines. `gov` rejects anything else; fix the facts and rerun. Then run the same facts with `--format questions` to get the open facts ranked by how much each would settle.

### 4. Reply

Keep the reply to one screen plus the plan:

1. **Triage plan: <request in a few words>**, and one line on what you understood.
2. **Facts:** the ones you set, marked given or inferred.
3. `gov`'s output, unchanged.
4. **Issues for counsel the plan doesn't cover:** legal issues specific to this request that no step or check in the plan names, such as a sector rule, a contract limit, or a litigation trend. Each gets one line and an owner, and counsel decides whether it blocks launch. Five at most. Name the issue and why it may apply; don't decide it or state uncertain law as fact. Write "None beyond the plan" if there are none.
   If the request names a launch date, add one line after the issues: the required decisions that must close before that date, in the order to start them.
5. **Questions:** one list. First, ask for the PRD, ticket, or a short description if you don't have one. Then ask three questions at most, each an open fact from `--format questions`, worded with that fact's question. Pick the facts that matter most for this request, not only the top of the ranking: `tracking_tech` or `session_replay` for analytics, `biometrics` or `school_context` for a tool that records students, `scraped_data` for data from LinkedIn. If a fact you need isn't in the table, say so under issues instead.
6. Offer to start the steps marked **Now**. Several can run in parallel.

### 5. Hand off

When the user agrees, follow each step's `SKILL.md` from the beginning, and carry the facts forward so the user isn't asked twice. When answers come back, rerun `gov route` with the new facts; the plan changes only through the table. A step marked "no skill yet" goes to its owner, and launch waits until its result is recorded.

## Rules

- Triage makes no legal determinations. "This likely needs a DPIA" goes to `dpia` for screening, not into the plan as a conclusion.
- Don't do a missing skill's work ad hoc in triage.
- Never create calendar events. Deadlines go in the plan and in the action plans of the skills that run.
