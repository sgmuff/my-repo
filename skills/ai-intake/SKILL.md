---
name: ai-intake
description: Take in a new or existing AI use case, AI system, model, or agent, including agents and AI features embedded in tools the company already buys, record it in the AI inventory, and propose a risk tier against the EU AI Act categories and AIUC-1 that decides which follow-on reviews it needs. Captures what the system does, who it affects, what data it touches, how autonomous it is, and what decisions it informs. Use it whenever someone wants to start using, build, buy, pilot, or switch on AI, asks "can we use AI for X," needs an AI inventory or an AI register built or refreshed, finds shadow AI, or asks whether a use is high-risk or prohibited under the EU AI Act, even if they don't say "intake." Not for the full assessment of fairness, oversight, and reliability (ai-impact-assessment), reviewing an AI vendor's contract (vendor-review), writing the AI acceptable use policy (notice-and-policy), or AI Act provider files and deployer duty checks (ai-act-provider, ai-act-deployer).
---

# AI intake and inventory

This skill is the front door for AI. It records each AI system or agent in the inventory, proposes a tier, and names the follow-on work the tier requires. It's deliberately quicker than an impact assessment: the goal is to know what AI the company uses, and which uses need closer review, before anyone relies on them.

The skill proposes the tier and the classification. The privacy lead confirms them (`approvals.md`). A Tier 0 or Tier 1 proposal goes to the privacy lead at once.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start, for the regimes in scope and the business areas |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 6 |
| [`references/tiering.md`](references/tiering.md) | Step 4: tiers, factors, AIUC-1 mode and capability tags, finding unregistered AI |
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Step 3: definition, roles, prohibited practices, Annex III |
| [`../_shared/references/aiuc-1.md`](../_shared/references/aiuc-1.md) | Step 4: mode and applicable requirements |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) | Step 4: the AI risk catalog (§2a) |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | §9, state AI and ADMT laws |
| [`assets/ai-system-template.md`](assets/ai-system-template.md) | Step 5 |
| [`../_shared/scripts/build_register_index.py`](../_shared/scripts/build_register_index.py) | Step 5, to rebuild the inventory index |

## Workflow

### 1. Load context and check the inventory

Read `conventions.md` and `company-profile.md`. Read `<output root>/registers/ai-inventory/index.md` if it exists, and look for an entry for the same system or use. One system used for two different purposes gets one entry, with each use tiered separately; the entry's tier is the highest.

If the AI is already in use, including a pilot or a feature switched on by default, record that, and ask what it has already processed. Containment comes before planning (`conventions.md`, §6).

### 2. Describe the system by what it does

Capture the facts in one short Round 1 message (usually under 10 questions), with documents requested where they exist (product documentation, the vendor's AI terms, an architecture note):

- **Function:** what goes in, what comes out, and what happens to the output. Ask for sample inputs and outputs.
- **Use:** who uses it, for what decision or task, and whether its outputs feed a decision about a person
- **People affected:** users, and anyone the outputs are about
- **Data:** what personal, sensitive, student, or confidential data it sees, including through retrieval or connected tools
- **Autonomy:** suggest only, act with approval, or act on its own; which tools and permissions it has
- **Source:** built in-house, built on a vendor model, or a vendor's product or embedded feature
- **Status:** idea, pilot, live; dates

A label is not a function. "Productivity assistant," "insights," or "engagement score" tells you nothing until you know the inputs, outputs, and use.

### 3. Classify under the EU AI Act

Using `eu-ai-act.md`, and marking each point Provisional:

1. **Is it an AI system** (Art. 3(1))? Record why, briefly.
2. **Roles:** provider, deployer, or both, from the facts (§3). Building on a vendor model doesn't by itself make the company a provider.
3. **Prohibited practices** (Art. 5): check every one against the documented function, now. Prohibitions already apply.
4. **High-risk** (Art. 6, Annex III): check each Annex III area against the intended purpose. If relying on the Art. 6(3) derogation, record the condition and why the system doesn't profile people.
5. **Transparency** (Art. 50): each paragraph separately.
6. **GPAI:** note whether a general-purpose model sits underneath, and who provides it.

Also note other regimes the use touches: GDPR Art. 22 and profiling, California ADMT, Colorado SB 26-189, employment AI laws (`us-state-privacy.md`, §9), and FERPA or COPPA for student data.

### 4. Propose the tier

Apply `references/tiering.md`. For each factor, record the level and the fact behind it. The tier is the highest level that applies. Then:

- Set the **AIUC-1 mode** (readiness or benchmark) and the **capability tags**, and list the mandatory requirements that apply.
- Name the top risks from the AI risk catalog (`risk-method.md`, §2a), briefly. Full analysis belongs to the impact assessment.
- List the **follow-ons** the tier requires, with the skill for each: `ai-impact-assessment`, `dpia` screening, `vendor-review`, and AUP coverage. Recommend them; don't run them.

A Tier 0 result is a stop: say so first, plainly, with the provision and the function that raises it, and add a `Decision needed` block for the privacy lead and counsel. Phrase the legal point conditionally ("may fall within Art. 5(1)(f) if it infers employees' emotions from biometric data"), not as a settled classification. Tier 0 is an internal precaution.

**Containment needs a record.** For any immediate control, record the owner and approver, when it was requested and applied, the evidence (a configuration screenshot), confirmation that the output is no longer generated, shown, exported, or used downstream (exports, reports, and integrations included), any remaining access paths, and the condition for re-enabling it.

**Ask the vendor what a score actually measures:** the construct, every input (text, acoustic features, pauses, rate, pitch), whether it infers emotion, sentiment, personality, or competence, the method and documentation, sample outputs, whether results vary by language, accent, disability, or call conditions, and whether the feature can be disabled on its own.

**For employee-facing tools, keep three workstreams apart:** employee monitoring (purposes, works council co-determination agreements, such as under BetrVG § 87(1) no. 6 in Germany, including for later material changes), the other people on the calls or in the content (notices, lawful bases, recording rules), and biometrics (identification or verification versus analysis of vocal features).

### 5. Write the inventory entry and rebuild the index

Fill in `assets/ai-system-template.md`. Save it to `<output root>/registers/ai-inventory/<system-slug>.md`, ID `AIS-NNNN`. Then run `python3 ../_shared/scripts/build_register_index.py <output root>/registers/ai-inventory ai-system` from this skill's folder.

### 6. Route and hand back

Route per `approvals.md`: the privacy lead confirms the tier and the classification; the business owner confirms the facts. Tier 0 and Tier 1 go to the privacy lead immediately, not in a batch.

Reply in about 150 words: the entry path and ID, the proposed tier (Provisional) and the deciding factor, any stop, the follow-ons, and the decisions needed.

## Building or refreshing the whole inventory

When asked to build the inventory, or find AI nobody registered, use the discovery sources in `references/tiering.md`. Propose the list of systems first, and get it confirmed. Then draft the entries, send one consolidated question list grouped by system, and rebuild the index once at the end. In the reply, report coverage: systems found, tiered, and still unconfirmed, and any Tier 0 or Tier 1.

Each entry has a review date: 12 months for Tier 3, 6 months for Tiers 1 and 2, and on any material change (new data, new use, new autonomy, model change). Review dates are actions, never calendar events.
