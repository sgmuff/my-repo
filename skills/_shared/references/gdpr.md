# GDPR, UK GDPR, and Swiss FADP

| Field | Value |
|---|---|
| Covers | EU GDPR (Regulation (EU) 2016/679); UK GDPR and DPA 2018 as amended by the Data (Use and Access) Act 2025; Swiss Federal Act on Data Protection (revised FADP, in force September 1, 2023) |
| Version covered | EU GDPR as in force on 2026-10-16, with no amendments adopted. UK GDPR with DUAA amendments commenced in stages from June 19, 2025. FADP and its Ordinance (DPO) as in force since September 1, 2023. |
| Sources | EUR-Lex (eur-lex.europa.eu/eli/reg/2016/679/oj); legislation.gov.uk (DUAA 2025 and commencement regulations SI 2025/904, SI 2025/996, SI 2026/82); fedlex.admin.ch (FADP SR 235.1); EDPB guidelines |
| Last verified | 2026-10-16 |
| Verification scope | Status items (Omnibus procedure, DUAA commencement) checked against sources on 2026-10-16. Article content reflects the stable text of the three laws and was not re-read line by line. Quote from EUR-Lex, legislation.gov.uk, or fedlex rather than from this summary. |
| Review interval | Quarterly while the EU Digital Omnibus is pending and DUAA commencement continues; otherwise every six months |
| Volatile points | §1 (pending EU Digital Omnibus; DUAA commencement); §9 (breach deadlines if the Omnibus passes); §11 (EU-US DPF litigation) |

## Contents

1. Status and pending changes
1a. Territorial scope
2. Roles
3. Principles, lawful bases, and special categories
4. Transparency
5. Data subject rights and deadlines
6. Automated decision-making
7. Accountability, records, and DPOs
8. Processors and contracts
9. Personal data breaches
10. DPIAs and prior consultation
11. International transfers
12. Swiss FADP differences
13. Fines

---

## 1. Status and pending changes

**EU GDPR is unamended.** The Commission's Digital Omnibus proposal (procedure 2025/0360(COD), November 2025) would amend the GDPR. As of October 16, 2026 it was still in the European Parliament, with committee amendments recorded in July 2026. The EDPB and EDPS responded in Joint Opinion 2/2026. *Volatile.* Until it is adopted and applies, cite the current text. The main proposed changes are:

- A relative definition of personal data, tied to the means reasonably likely to be used by the specific controller
- Breach notification to the supervisory authority only for breaches likely to result in a **high** risk, within **96 hours**, through a single EU entry point
- EU-wide lists of processing that does and doesn't require a DPIA, plus a common DPIA template, prepared by the EDPB, replacing national lists
- A broader record-of-processing exemption (the threshold rises from 250 to 750 employees in the proposal)
- A new legitimate-interests route for processing personal data to develop and operate AI, and a limited exception for residual special category data in AI training
- Cookie and terminal-equipment rules moved partly into the GDPR

When a conclusion would change if the Omnibus passed, add a verify flag that says so.

**UK GDPR is amended by the Data (Use and Access) Act 2025 (DUAA),** commenced in stages. *Volatile.* Confirmed so far:

- **Royal Assent, June 19, 2025:** subject access requests need only a "reasonable and proportionate" search (UK GDPR Art. 15(1A)), treated as applying from January 1, 2024.
- **Commencement No. 1, August 20, 2025 (SI 2025/904):** governance changes and the first data protection provisions.
- **Commencement No. 3 (SI 2025/996):** legal professional privilege and national security exemptions; joint processing provisions from November 17, 2025.
- **Commencement No. 6 (SI 2026/82):** further provisions from February 5, 2026, and the duty for controllers to handle data protection complaints (DUAA s. 103) from June 19, 2026.

The main Part 5 amendments include recognized legitimate interests (UK GDPR Art. 6(1)(ea) and Annex 1), new automated decision-making rules (Arts. 22A–22D), "stop the clock" for clarifying requests, a revised international transfer test, and the renaming of the ICO as the Information Commission. Before citing one of these as in force, confirm its commencement on legislation.gov.uk and record the date checked.

**Swiss FADP** has been stable since September 1, 2023.

---

## 1a. Territorial scope

Never decide that the GDPR doesn't apply from where the data subjects live. Art. 3 has three routes, and each needs its own facts:

- **Establishment (Art. 3(1)):** the GDPR applies to processing in the context of the activities of an establishment of a controller or processor in the EU, **regardless of whether the processing takes place in the EU or whose data it is.** An EU subsidiary, office, or stable arrangement can bring US-only processing into scope if the processing is in the context of its activities.
- **Targeting (Art. 3(2)(a)):** a controller or processor not established in the EU is covered when it offers goods or services to data subjects in the EU.
- **Monitoring (Art. 3(2)(b)):** the same, when it monitors their behavior in the EU.

EDPB Guidelines 3/2018 on territorial scope explain each route.

**Scope and the lead supervisory authority are separate questions.** Art. 3 decides whether the GDPR applies. The lead authority under the one-stop shop (Art. 56) depends on the controller's main establishment and on whether the processing is cross-border (Art. 4(16), (23)). Having an EU office doesn't settle either one alone. UK GDPR Art. 3 and FADP Art. 3 (effects in Switzerland) follow similar logic.

Before recording "GDPR not applicable," confirm: the company's establishments and what each does; whether any of them is involved in the processing; and whether any data subjects are in the EU, UK, or Switzerland. Until confirmed, the conclusion is Provisional (`conventions.md`, §7), and the open fact goes in the fact register. If the GDPR doesn't apply, say which other regimes still do. Its absence doesn't mean there are no obligations.

---

## 2. Roles

| Role | Definition | Consequence |
|---|---|---|
| Controller | Determines the purposes and means of processing (Art. 4(7)) | Owns the lawful basis, transparency, rights, DPIA, and records |
| Joint controllers | Jointly determine purposes and means (Art. 26) | Need an arrangement allocating duties; the essence is made available to data subjects (Art. 26(2)) |
| Processor | Processes on behalf of the controller (Art. 4(8)) | Bound by an Art. 28 contract; its own records (Art. 30(2)) and security (Art. 32); assists the controller with DPIAs (Art. 28(3)(f)) |
| Sub-processor | Engaged by a processor | Needs the controller's authorization and flow-down terms (Art. 28(2), (4)) |

A processor that uses data for its own purposes, such as training its own models or analytics beyond the service, becomes a controller for that use (Art. 28(10)). Check for this in every vendor review.

**Roles follow the facts, not the contract.** A DPA that calls a vendor a processor is evidence, not a conclusion. Ask who decides the purposes and the essential means of each processing operation, and assign roles operation by operation. One party can be a processor for the service and a controller for something it decides on itself, such as model training or product analytics. When the company is a controller for a related operation, such as training its own model, that operation is a separate workstream, but it still belongs in the privacy analysis and may need its own assessment.

FADP uses the same split: controller (*Verantwortlicher*, FADP Art. 5(j)) and processor (*Auftragsbearbeiter*, Art. 5(k)).

---

## 3. Principles, lawful bases, and special categories

**Principles (Art. 5(1)):** (a) lawfulness, fairness, and transparency; (b) purpose limitation; (c) data minimization; (d) accuracy; (e) storage limitation; (f) integrity and confidentiality. The controller must be able to demonstrate compliance (Art. 5(2)).

**Lawful bases (Art. 6(1)):** (a) consent; (b) contract; (c) legal obligation; (d) vital interests; (e) public task; (f) legitimate interests, which needs a three-part test: purpose, necessity, and balancing. Further processing for a new purpose must be compatible (Art. 6(4)). UK only: (ea) recognized legitimate interests listed in UK GDPR Annex 1, which need no balancing test (*verify commencement*).

**Consent (Arts. 4(11), 7):** freely given, specific, informed, unambiguous, as easy to withdraw as to give, and demonstrable. Children's consent for information society services: 16 by default, lowered by some member states to as low as 13 (Art. 8(1)). The UK sets 13.

**Special category data (Art. 9(1)):** racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data for unique identification, health, sex life, or sexual orientation. Processing is prohibited unless an Art. 9(2) condition applies, such as (a) explicit consent, (b) employment and social security law, (f) legal claims, or (g) substantial public interest. Inferred special category data counts.

**Classify by what the data reveals, in context.** A field is special category data when it reveals one of the Art. 9(1) categories, directly or by clear inference, in the context of the processing (see CJEU C-184/20, *OT*, on indirect revelation). An IEP flag may reveal disability or health information. An English-learner status isn't Art. 9 data by default, although it can correlate with origin and deserves care. Record the reasoning for each such field. FERPA education records and GDPR special category data are different concepts; one doesn't imply the other.

**Biometric data needs precision.** A face image is not special category data just because it shows a face. It becomes biometric data under Art. 4(14) and Art. 9 when specific technical processing allows or confirms unique identification (Recital 51). Distinguish, and record which the system does:

- Capturing video or images for ordinary viewing
- Detecting that a face is present, or counting faces, without identifying anyone
- Comparing a live face to a reference image to verify identity (biometric; Art. 9)
- Creating or retaining face templates or embeddings (biometric; Art. 9)
- Using facial, gaze, or voice features to infer behavior, emotion, or intent (may be biometric, and engages AI Act Art. 5(1)(f) in workplaces and education)

The same precision applies to voice, keystroke dynamics, and gait.

**Criminal offense data (Art. 10):** only under official authority or where member state law authorizes it.

**Swiss sensitive data (FADP Art. 5(c))** is broader: it adds data on religious, philosophical, political, or trade union views or activities, intimate sphere, administrative and criminal proceedings and sanctions, and social assistance measures.

---

## 4. Transparency

Information must be concise, transparent, intelligible, easily accessible, and in clear and plain language (Art. 12(1)).

| Item | Collected from the person (Art. 13) | From another source (Art. 14) |
|---|---|---|
| Controller identity and contact; DPO contact | 13(1)(a)–(b) | 14(1)(a)–(b) |
| Purposes and lawful basis | 13(1)(c) | 14(1)(c) |
| Legitimate interests pursued, if relied on | 13(1)(d) | 14(2)(b) |
| Categories of personal data | — | 14(1)(d) |
| Recipients or categories of recipients | 13(1)(e) | 14(1)(e) |
| Third-country transfers and safeguards | 13(1)(f) | 14(1)(f) |
| Retention period or criteria | 13(2)(a) | 14(2)(a) |
| Rights, including withdrawal of consent and complaint to a supervisory authority | 13(2)(b)–(d) | 14(2)(c)–(e) |
| Whether providing the data is required, and the consequences of not providing it | 13(2)(e) | — |
| Source of the data | — | 14(2)(f) |
| Automated decision-making: existence, logic, significance, and consequences | 13(2)(f) | 14(2)(g) |

Timing under Art. 14(3): within a reasonable period and at the latest one month after obtaining the data, or at first communication or first disclosure if earlier.

FADP Art. 19 requires similar content, including each recipient country and the safeguard relied on.

---

## 5. Data subject rights and deadlines

| Right | EU GDPR | UK GDPR | FADP |
|---|---|---|---|
| Access | Art. 15 | Art. 15, with a "reasonable and proportionate" search (Art. 15(1A)) | Art. 25 |
| Rectification | Art. 16 | Art. 16 | Art. 32 |
| Erasure | Art. 17 | Art. 17 | Art. 32 |
| Restriction | Art. 18 | Art. 18 | Art. 32 |
| Portability | Art. 20 | Art. 20 | Art. 28 |
| Objection (absolute for direct marketing) | Art. 21, 21(3) | Art. 21 | Art. 30(2)(b) |
| Not subject to solely automated decisions | Art. 22 | Arts. 22A–22D (*verify commencement*) | Art. 21 (information and right to be heard) |

**Deadline:** one month from receipt, extendable by two further months where necessary given the complexity and number of requests, with the person told of the extension and the reasons within the first month (Art. 12(3)). The UK allows the clock to pause while the controller waits for information it reasonably needs, such as identity verification or clarification (*verify commencement*). FADP access: 30 days, extendable with notice (Data Protection Ordinance Art. 18).

**Identity:** where there is reasonable doubt, the controller may request information needed to confirm identity (Art. 12(6)). Don't collect more than needed.

**Manifestly unfounded or excessive requests:** may be refused or charged a reasonable fee; the controller bears the burden of proof (Art. 12(5)).

**Notifying recipients:** rectification, erasure, and restriction must be passed to each recipient unless impossible or disproportionate (Art. 19).

The `dsr-response` skill (Wave 2) will add a fuller matrix covering US states.

---

## 6. Automated decision-making

**EU GDPR Art. 22:** a person has the right not to be subject to a decision based solely on automated processing, including profiling, that produces legal or similarly significant effects, unless the decision is (a) necessary for a contract, (b) authorized by law, or (c) based on explicit consent. For (a) and (c), the controller must provide at least the right to obtain human intervention, to express a view, and to contest the decision (Art. 22(3)). Special category data may be used only with Art. 9(2)(a) or (g) and suitable safeguards (Art. 22(4)).

Human involvement must be meaningful. A person who rubber-stamps the output doesn't take the decision out of Art. 22.

**Run two separate analyses, and record both:**

1. **Is there profiling (Art. 4(4))?** Automated evaluation of personal aspects, such as a churn, risk, or engagement score about a person. Profiling brings transparency duties and the right to object (Art. 21), whether or not Art. 22 applies. First check that the score is about a natural person and not only a business account.
2. **Is there a decision under Art. 22?** Both conditions must hold: the decision is based **solely** on automated processing, and it produces **legal or similarly significant effects**. Test the effect against the real consequences. Closing a ticket that only leaves an agent's queue is different from one that lets a refund deadline lapse, ends a complaint, delays a security response, or cuts access to a service.

**Reversibility and notices are safeguards, not exemptions.** A closure notice and a "reply to reopen" option help, but they don't decide whether a decision is solely automated or significant. Analyze the conditions first, then record the safeguards and the evidence that they work. The CJEU read "decision" broadly in *SCHUFA* (C-634/21, December 7, 2023): an automated score that plays a determining role in a third party's decision can itself be an Art. 22 decision.

**UK GDPR Arts. 22A–22D (DUAA):** solely automated significant decisions are generally allowed with safeguards (information, representations, human intervention, and contest), except when based on special category data, which keeps tighter limits. *Verify commencement.*

**FADP Art. 21:** inform the person of an automated individual decision with legal or significant effects, and on request let them state their view and have a human review it.

---

## 7. Accountability, records, and DPOs

- **Responsibility of the controller (Art. 24)** and **data protection by design and by default (Art. 25).**
- **Records of processing (Art. 30).** A controller's record contains (Art. 30(1)):
  - (a) name and contact details of the controller, any joint controller, the representative, and the DPO
  - (b) purposes
  - (c) categories of data subjects and of personal data
  - (d) categories of recipients, including in third countries
  - (e) transfers to third countries, and for Art. 49(1) second-subparagraph transfers, the safeguards
  - (f) where possible, time limits for erasure
  - (g) where possible, a general description of the Art. 32(1) security measures

  A processor's record contains (Art. 30(2)): (a) name and contact details of the processor, each controller, representatives, and DPO; (b) categories of processing carried out for each controller; (c) transfers; (d) where possible, the security measures.

  **Exemption (Art. 30(5)):** fewer than 250 employees, unless the processing is likely to result in a risk, is not occasional, or includes Art. 9 or Art. 10 data. In practice almost no company qualifies, because routine processing is not occasional. *Volatile:* the Omnibus would raise the threshold.
- **FADP Art. 12:** controllers and processors keep a record of processing activities with similar content. Companies with fewer than 250 employees are exempt unless they process sensitive data on a large scale or carry out high-risk profiling (Ordinance Art. 24).
- **DPO (Art. 37):** mandatory where core activities involve regular and systematic monitoring of individuals on a large scale, or large-scale processing of Art. 9 or Art. 10 data, or for public bodies.
- **Representative (Art. 27):** needed by a controller or processor with no EU establishment that is subject to the GDPR under Art. 3(2).

---

## 8. Processors and contracts

**Choosing a processor (Art. 28(1)):** use only processors that give sufficient guarantees of appropriate technical and organizational measures.

**Sub-processors (Art. 28(2), (4)):** prior specific or general written authorization. Under general authorization, the processor tells the controller of intended changes and gives it the chance to object. The same data protection obligations flow down by contract, and the original processor remains fully liable.

**Mandatory contract terms (Art. 28(3)).** The contract sets out the subject matter, duration, nature and purpose of processing, type of personal data, categories of data subjects, and the controller's obligations and rights. It must require the processor to:

- (a) process only on documented instructions, including for transfers, unless law requires otherwise
- (b) ensure people authorized to process the data are bound by confidentiality
- (c) take all measures required by Art. 32
- (d) respect the conditions for engaging sub-processors
- (e) assist the controller in responding to data subject requests
- (f) assist the controller with Arts. 32 to 36: security, breach notification, DPIAs, and prior consultation
- (g) delete or return all personal data at the end of the services, at the controller's choice
- (h) make available all information needed to demonstrate compliance, and allow for and contribute to audits and inspections

The processor must also tell the controller immediately if an instruction infringes the law (Art. 28(3), final subparagraph). The contract must be in writing, which includes electronic form (Art. 28(9)). The Commission's SCCs for controller-processor contracts (Implementing Decision (EU) 2021/915) satisfy Art. 28.

**FADP Art. 9:** processing may be delegated by contract if the processor processes only as the controller could, and no legal or contractual secrecy duty forbids it. Sub-processing needs the controller's prior authorization.

The `vendor-review` skill (Wave 1) will turn this section into a DPA checklist.

---

## 9. Personal data breaches

**Definition (Art. 4(12)):** a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data.

| Duty | EU GDPR | UK GDPR | FADP |
|---|---|---|---|
| Notify the authority | Without undue delay and, where feasible, within 72 hours of becoming aware, unless unlikely to result in a risk (Art. 33(1)) | Same, to the Information Commission | As soon as possible, if likely to result in a high risk (Art. 24(1)) |
| Processor to controller | Without undue delay (Art. 33(2)) | Same | As soon as possible (Art. 24(3)) |
| Notify individuals | Without undue delay if likely to result in a high risk, unless an Art. 34(3) exception applies | Same | If needed to protect them, or if the FDPIC requires it (Art. 24(4)) |
| Document every breach | Yes (Art. 33(5)) | Yes | — |

**Content of the notice to the authority (Art. 33(3)):** (a) the nature of the breach, including categories and approximate numbers of data subjects and records; (b) the DPO or contact point; (c) likely consequences; (d) measures taken or proposed. Information may be provided in phases (Art. 33(4)).

**Guidance:** EDPB Guidelines 9/2022 on personal data breach notification, version 2.0 (March 28, 2023), and EDPB Guidelines 01/2021 on examples of breach notification.

*Volatile:* the Omnibus would change the authority threshold to high risk and the deadline to 96 hours. Until adopted, use 72 hours. The `incident-assessment` skill (Wave 3) will add the US state breach laws.

---

## 10. DPIAs and prior consultation

**DPIA (Art. 35):** required where processing is likely to result in a high risk, and always in the three Art. 35(3) cases. Content (Art. 35(7)): (a) a systematic description of the processing and purposes, including legitimate interests; (b) necessity and proportionality; (c) the risks to rights and freedoms; (d) the measures to address them. Seek the DPO's advice (Art. 35(2)) and, where appropriate, the views of data subjects (Art. 35(9)). Review when the risk changes (Art. 35(11)). The screening criteria are in `dpia/references/screening.md`.

**Prior consultation.** Flag it whenever **any** residual risk is still High after mitigation. Judge this on the current residual rating, the one based on verified controls (`risk-method.md`, §1). An unverified target rating of Medium doesn't rule out consultation. Write instead: "Prior consultation is not required if the target residual rating is achieved and verified. Revisit when A<n> closes."

In a processor assistance pack, the company doesn't decide whether the customer must consult. Say that the pack doesn't make that determination, and that each controller assesses its own residual risk, including its own safeguards, and decides on Art. 36 itself.

- **EU GDPR Art. 36:** consult the supervisory authority *before* processing starts. For cross-border processing, consult the lead supervisory authority. The authority has 8 weeks to give written advice, extendable by 6 weeks, and the clock pauses while it waits for information (Art. 36(2)). Under Art. 36(3), the submission includes: the responsibilities of the controllers and processors; the purposes and means; the measures and safeguards; the DPO's contact details; the DPIA; and any other information the authority requests. Some member states also require consultation or authorization for processing in the public interest (Art. 36(5)).
- **UK GDPR Art. 36:** consult the regulator before processing if high risk remains; 8 weeks, extendable by 6.
- **FADP Art. 23:** consult the FDPIC if high risk remains, unless the company consulted its data protection advisor (Art. 23(4)). The FDPIC has 2 months, extendable by 1.

When you flag consultation in a document:

1. Name the risks, by ID, that are still High.
2. List the additional mitigations that could reduce them, with your view on whether each is feasible. Consultation is slow, so the business usually prefers to reduce the risk first.
3. State that processing must not start until consultation is complete or the risk is brought down to Medium or lower.
4. Add an action to prepare the consultation package, owned by the DPO or privacy lead.

**FADP Art. 22:** a DPIA is required when processing may lead to a high risk to personality or fundamental rights, notably for extensive processing of sensitive data or systematic monitoring of extensive public areas.

---

## 11. International transfers

| Mechanism | EU | UK | Switzerland |
|---|---|---|---|
| Adequacy | Art. 45 decisions | UK adequacy regulations | Federal Council list (Ordinance Annex 1) |
| US framework | EU-US Data Privacy Framework, adequacy decision of July 10, 2023, for certified US organizations | UK Extension to the DPF ("data bridge"), from October 12, 2023 | Swiss-US DPF, from September 15, 2024 |
| Contract clauses | 2021 SCCs (Implementing Decision (EU) 2021/914): Module 1 C2C, 2 C2P, 3 P2P, 4 P2C | IDTA, or the UK Addendum to the EU SCCs | EU SCCs with Swiss adaptations |
| Corporate rules | BCRs (Art. 47) | UK BCRs | BCRs approved by the FDPIC |
| Derogations | Art. 49, for occasional transfers only | Art. 49 | FADP Art. 17 |

**Transfer impact assessment:** required in practice for SCCs and BCRs, following *Schrems II* (CJEU C-311/18) and EDPB Recommendations 01/2020. Record the assessment and any supplementary measures.

**Remote access counts as a transfer.** Support staff in a third country who can view EU data trigger Chapter V.

*Volatile:* the General Court dismissed the challenge to the EU-US DPF in *Latombe v Commission* (T-553/23, September 3, 2025). An appeal to the Court of Justice was reported. Check its status before advising that the DPF is stable, and keep SCCs as a fallback in vendor contracts.

---

## 12. Swiss FADP differences

- Applies only to natural persons' data (legal persons are no longer covered).
- Sanctions are criminal fines of up to CHF 250,000 on **responsible individuals**, not the company, for intentional breaches of specific duties (FADP Arts. 60–66).
- Breach notification threshold is high risk only, with no fixed hour count (Art. 24).
- No legitimate-interests list. Processing is lawful unless it unlawfully violates personality (Art. 30), and justification is needed only then (Art. 31).
- Privacy by design and default (Art. 7) and a duty to inform (Art. 19) apply as in the GDPR.

## 13. Fines

EU and UK GDPR: up to €20 million or 4% of worldwide annual turnover, whichever is higher, for breaches of principles, lawful bases, rights, and transfers (Art. 83(5)); up to €10 million or 2% for breaches of controller and processor duties, including Arts. 25 to 39 (Art. 83(4)). UK: £17.5 million or 4%, and £8.7 million or 2%.
