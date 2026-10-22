---
name: ai-intake
description: Take in a new or existing AI use case, AI system, model, or agent, including agents and AI features embedded in tools the company already buys, record it in the AI inventory as a gov record, and propose a risk tier against the EU AI Act categories and AIUC-1 that decides which follow-on reviews it needs. Captures what the system does, who it affects, what data it touches, how autonomous it is, and what decisions it informs. Use it whenever someone wants to start using, build, buy, pilot, or switch on AI, asks "can we use AI for X," needs an AI inventory or an AI register built or refreshed, finds shadow AI, or asks whether a use is high-risk or prohibited under the EU AI Act, even if they don't say "intake." Not for the full assessment of fairness, oversight, and reliability (ai-impact-assessment), reviewing an AI vendor's contract (vendor-review), writing the AI acceptable use policy (notice-and-policy), or AI Act provider files and deployer duty checks (ai-act-provider, ai-act-deployer).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# AI intake and inventory

This skill is the front door for AI. It records each AI system or agent as an `ais` record in the inventory, proposes a tier, and names the follow-ons the tier requires. It's quicker than an impact assessment: the goal is to know what AI the company uses, and which uses need closer review, before anyone relies on them. Never write or edit a record's `.md` file; `gov` writes it.

The skill proposes the tier and the classification; the privacy lead confirms them (`approvals.md`). A Tier 0 or Tier 1 proposal goes to the privacy lead at once.

## Files

| File | Read it when |
|---|---|
| [`references/tiering.md`](references/tiering.md) | Step 3: tiers, factors, follow-ons, AIUC-1 mode and tags, finding unregistered AI |
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Step 3: definition, roles, prohibited practices, Annex III, Art. 50 |
| [`../_shared/references/aiuc-1.md`](../_shared/references/aiuc-1.md) | Step 3: mode and capability tags |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) | Step 3: the AI risk catalog (§2a) |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Step 3: Art. 22 and profiling (§6), biometric data (§3) |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | Step 3: CPPA risk assessments, which come before processing starts (§6), and state AI and ADMT laws (§9) |
| [`../_shared/references/dpa-checklist.md`](../_shared/references/dpa-checklist.md) | Step 3, for a vendor's AI: what to ask about its model, training, and retention (§6) |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 5 |

## Workflow

### 1. Check the tool and the inventory

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. Read `compliance/registers/ai-inventory/index.md` if it exists, and look for an entry for the same system. One system used for two purposes gets one entry, with each use tiered in `tiering` and `analysis`; the entry's tier is the highest.

If the AI is already in use, including a pilot or a feature switched on by default, ask what it has already processed. Containment comes before planning.

### 2. Get the facts

Ask in one Round 1 message (`conventions.md`, §6): inputs, outputs (with samples), what happens to the output, users, the people the outputs are about, data (including through retrieval and tools), autonomy and permissions, source, and lifecycle. Ask for product documentation and the vendor's AI terms where they exist. A label is not a function: "productivity assistant" or "engagement score" says nothing until you know the inputs, outputs, and use.

### 3. Answer the intake

Answer it fully, then check it against `tiering.md` and `eu-ai-act.md` and add what you missed. Points answers often miss:

- **Check every Art. 5 practice against the documented function now**; prohibitions already apply. A possible prohibited practice makes the system Tier 0, an internal stop: say so first, phrase the legal point conditionally ("may fall within Art. 5(1)(f) if it infers employees' emotions from biometric data"), and keep the immediate control, the provisional legal question, and the assessment of the rest of the system apart.
- **Building on a vendor model doesn't by itself make the company a provider.** Rebranding or substantially modifying a high-risk system can (Art. 25).
- **Relying on the Art. 6(3) derogation** needs the condition and why the system doesn't profile people; an undocumented derogation is a High factor.
- **Ask the vendor what a score measures:** the construct, every input (text, acoustic features, pauses, pitch), whether it infers emotion, sentiment, personality, or competence, whether results vary by language, accent, disability, or call conditions, and whether the feature can be disabled on its own.
- **For employee-facing tools, keep three workstreams apart:** employee monitoring (including works council co-determination, such as BetrVG § 87(1) no. 6), the other people in the calls or content, and biometrics (identification or verification versus analysis of vocal features).
- **Other regimes:** GDPR Art. 22 and profiling, California ADMT, Colorado, employment AI laws (`us-state-privacy.md`, §9), FERPA or COPPA.

### 4. Record it

Run `gov new ais --slug <system> --title "<system name>" --date <today>` and fill in the record from your answer: each tiering factor with its level and the fact behind it, the tier and AI Act calls (Provisional), the AIUC-1 mode and tags, three to six top risks, and the follow-ons with `status: recommended`; recommend them, don't run them. Record each containment control as `requested` until someone applies it, with an action to apply it; once applied, record the evidence and whether the output is stopped downstream, including exports, reports, and integrations. Record a split classification by function: `prohibited` for a possible Art. 5 practice, `category` for the rest of the system, and `art50` for transparency duties, which apply whatever the category. Link each verify flag to its action. Points that don't fit a field go in `analysis` (400 words at most). When a follow-on starts, set its `record` to the new record's ID.

### 5. Validate, render, and reply

Run `gov validate`, fix errors, and resolve findings by changing the record; a finding that names a real gap stays open with an action. Don't add a `finding_responses` entry yourself. Run `gov render`, which rebuilds the inventory index.

Reply in plain English: any stop first, with the containment to apply now; then the proposed tier (Provisional) and the deciding factor, what has to happen before use, the follow-ons, and the Round 1 questions. Tier 0 and Tier 1 go to the privacy lead now, not in a batch; if the company profile names no privacy lead, say the decision is theirs by role and ask who holds it, rather than saying it was sent. Close with one line naming the record and its path.

## Building or refreshing the whole inventory

Use the discovery sources in `tiering.md`. Propose the list of systems first and get it confirmed, then create one record per system, send one consolidated question list grouped by system, and run `gov render` once at the end. Report coverage: systems found, tiered, and still unconfirmed, and any Tier 0 or Tier 1.

Review entries every 6 months for Tiers 1 and 2, every 12 months for Tier 3, and on any material change (new data, use, autonomy, or model). `gov schedule` lists the dates; they're actions, never calendar events.
