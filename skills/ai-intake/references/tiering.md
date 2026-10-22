# AI system tiering

The tier decides which follow-on work an AI system needs. It is the skill's Provisional proposal; the privacy lead confirms it (`approvals.md`). The tier is set by the **highest** factor that applies, not an average. Classify by documented function, not by product names or labels (`eu-ai-act.md`, §4).

## Tiers

| Tier | Name | When | Required follow-ons |
|---|---|---|---|
| **0** | **Stop** | Any factor could be an EU AI Act prohibited practice (Art. 5), applying since February 2, 2025 | Disable the function pending review, escalate to the privacy lead and counsel now, and preserve the records. Tier 0 is an **internal stop-use classification**, a precaution, not a legal finding that the practice is prohibited. Record the provisional legal question separately. DPIA screening and the vendor review still run for the data already processed and the rest of the system. |
| **1** | **High** | Any High factor below | AI impact assessment (`ai-impact-assessment`), with a FRIA check; DPIA screening; Deep vendor review if third-party; Art. 50 transparency check; AIUC-1 in the right mode; human oversight designed and tested before launch; quarterly testing plan |
| **2** | **Elevated** | Any Elevated factor, and no High factor | A targeted AI impact assessment (the sections the factors call for); DPIA screening if personal data is involved; Standard vendor review; Art. 50 transparency check |
| **3** | **Standard** | Only Standard factors | Register entry; acceptable use policy applies; Light vendor review if third-party |

## Factors

In the `ais` record, each factor's `level` is the column it falls in: `standard`, `elevated`, or `high`, or `stop` for a possible Art. 5 practice. Requirements are cumulative: a higher tier needs everything a lower one does.

| Factor | Standard | Elevated | High |
|---|---|---|---|
| **Use under the EU AI Act** | Minimal risk | Transparency duties (Art. 50): chatbots, synthetic content, emotion recognition or biometric categorization notices | Annex III use (by function), Art. 6(1) safety component, or an Art. 6(3) derogation that hasn't been documented |
| **Decisions about people** | None | Informs a decision that a person makes, with low stakes | Makes or materially influences decisions with legal or similarly significant effects: hiring, firing, task allocation, performance evaluation, grading, admission, placement, discipline, credit, insurance, housing, healthcare, access to essential services (GDPR Art. 22; CCPA ADMT; Colorado SB 26-189) |
| **People affected** | Employees using it as a tool | Customers or the public interacting with it | Children, students, patients, job applicants, employees monitored or scored by it, or other vulnerable groups as subjects of outputs or decisions |
| **Data** | No personal data beyond the user's own account details | Personal data or confidential business data in prompts, context, or retrieval | Special category, biometric, children's, or student data; customer content at scale |
| **Autonomy (agents)** | L0: suggests only; a person does everything | L1: takes actions only after a person approves each one; or read-only tool access to internal systems | L2–L3: acts on its own within limits or broadly; write, send, transact, or delete access; customer-facing actions without review |
| **Reach and reversibility** | Few uses, easily corrected | Many uses, correctable | High volume, or effects that are hard to reverse |
| **Source** | — | Third-party model or tool with unknown training or retention terms | Own model trained or fine-tuned on personal data |

**Record three things separately** for a system that raises a concern: the **immediate control** (for example, disable one feature), the **provisional legal finding** (for example, possibly within Art. 5(1)(f), pending evidence of function), and the **risk assessment** of the rest of the system (for example, whether the remaining features fall within Annex III point 4(b), judged by intended purpose and use). Don't let the first stand in for the others.

**Embedded agents in purchased tools count.** An AI feature switched on in an existing SaaS product (a CRM assistant, a meeting summarizer, a helpdesk triage bot) gets the same tiering as a new system. Its vendor review covers the AI module (`dpa-checklist.md`, §6).

## AIUC-1 mode and capability tags

- **Mode:** the company's own agent → **certification readiness**; a third party's agent → **vendor benchmark** (`aiuc-1.md`, §2).
- **Capability tags** decide which AIUC-1 requirements apply: Universal, External-facing (customers or the public use it), Automation (it takes actions through tools), Code-generation, Text-generation, Voice-generation, Image-generation. Record each tag that fits.

## Finding AI that nobody registered

Ask about these sources when building or refreshing the inventory:

- SaaS admin consoles and vendor release notes for newly switched-on AI features
- Expense reports and procurement records for AI subscriptions
- SSO and OAuth app grants to AI tools
- Browser extensions and desktop assistants
- Internal repositories calling model APIs
- Teams' own lists, gathered through the business area contacts in the company profile
