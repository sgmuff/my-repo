# Processor assistance packs

Use this when the company is the processor and a customer is the controller who owns the DPIA (GDPR Art. 28(3)(f)), or when the company is a FERPA school official helping an institution. The pack is an **evidence package**, not a finished DPIA. Customers use it to complete their own assessment. They shouldn't be led to think it has already been done for them.

## What the pack supplies, and what it leaves to the customer

| The company supplies | The customer decides |
|---|---|
| Verified facts about the system: what it collects, infers, retains, and where | Necessity and proportionality for its own use |
| The evidence behind those facts: test results, configurations, certifications, contract terms | Its lawful basis, and any Art. 9 condition |
| The company's safeguards, with their status (verified or planned) | The consequences in its own setting, such as exam policies, appeals, and alternatives |
| Known limitations, failure modes, and performance across groups | Its residual risk, after its own safeguards |
| Instructions for use, and the safeguards the customer must configure or operate | Whether Art. 36 prior consultation is needed |
| Input to the customer's FRIA where the AI Act applies | Its FRIA, if it is an Art. 27 deployer |

Say this plainly at the top of the pack. The company's own risk assessment doesn't substitute for the customer's.

## How the pack differs from an internal DPIA

- **Metadata:** `type: dpia-assistance-pack`. The audience is external, so the line "DRAFT: not sent" comes first in the body, after the metadata block (`conventions.md`, §7).
- **Two versions.** Keep the internal working version, with internal owners, TBCs, internal actions, and the fact register, in the repository. The customer-facing version is a separate file, `…-customer.md`. Produce it only after the privacy lead approves release. It drops internal owners and internal-only actions, and turns open facts into stated limitations ("not yet tested across lighting conditions"), never into silent omissions.
- **Necessity, lawful basis, and consultation sections** are marked "Controller to complete," with the facts the controller will need.
- **Risk ratings are split** into vendor residual (after the company's verified controls) and deployment residual (the customer's to assess; `risk-method.md`, §1). Don't assume a customer will put a safeguard in place that the company can't enforce.
- **Prior consultation:** state that the pack doesn't determine it, and that each controller decides on Art. 36 after its own assessment. Don't write that consultation is "not triggered."
- **Responsibilities table:** separate company-owned controls from customer-owned deployment safeguards, such as human review, alternatives, accommodations, and appeals.
- **Escalation for missing deployment safeguards.** Where the company's risk analysis depends on customer safeguards (independent human review, alternatives and accommodations, appeals), say so, and say what the company does if a customer can't put them in place: configuration limits, contract terms, or declining the deployment. Whether each customer owes a FRIA is that customer's determination (`eu-ai-act.md`, §7).
- **Round 1 includes performance evidence.** Customers will rely on the pack's performance claims, so ask for accuracy, false positive, and subgroup test results in Round 1, not Round 2.
- **Where it goes:** reserve an ID with `gov next-id PA --year <YYYY>` and save the pack as `compliance/assessments/dpia/assistance-packs/PA-YYYY-NNN-<slug>.md`, from `assets/dpia-template.md` with `type: dpia-assistance-pack`. It's Markdown, and `gov` doesn't manage that folder; don't put it beside the `dpia` records, where `gov validate` rejects Markdown with no record.
- **A live service:** if customers already use it, raise what applies now as immediate actions in the pack, ahead of the release gate: any possible Art. 5 prohibition, and any use of customer data for the company's own purposes, such as model training (which makes the company a controller for that use).
- **The company's own risk:** the vendor residual rating is the company's, and `approvals.md` routes it like any residual risk. The release gate below is a separate approval (counsel, 2026-10-22).
- **Release gate:** the customer-facing version needs the privacy lead's approval and a defined minimum evidence set: the facts in the pack confirmed, any possible prohibition resolved, and the key performance claims tested. Release is an external communication (`approvals.md`).

## Related controller processing

If the company is a controller for a related operation, such as training the model the service uses, the pack says so. It names what the customer needs to know: dataset provenance, whether training uses customer data, and whether the trained model can retain personal information. The company assesses that operation separately.

## AI systems in the pack

Where the company is the AI Act provider of a high-risk system, add an action to plan the full set of provider obligations (`eu-ai-act.md`, §6), not only the instructions for use. Base classification and any prohibition analysis on documented function, not on labels (`eu-ai-act.md`, §4).
