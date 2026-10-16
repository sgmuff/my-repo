# DPA and vendor contract checklist

| Field | Value |
|---|---|
| Covers | The contract terms a vendor review checks: GDPR Art. 28, UK GDPR, Swiss FADP, US state processor and service provider terms, FERPA and state student privacy terms, international transfers, and AI-specific terms, benchmarked to AIUC-1 |
| Version covered | Built from `gdpr.md`, `us-state-privacy.md`, `ferpa.md`, `eu-ai-act.md`, and `aiuc-1.md` as verified 2026-10-16; AIUC-1 certification facts from standard.aiuc-1.com (FAQ and certification pages, retrieved 2026-10-16) |
| Last verified | 2026-10-16 |
| Review interval | Quarterly, alongside the files it draws on |
| Volatile points | §6 (AI terms track AIUC-1's quarterly releases); §4 (state laws enacted in 2026) |

This is a checklist, not a contract template. For each item, the vendor review records what the contract says, with the clause reference, and rates it **Present**, **Partial**, **Missing**, **Conflicts** (the contract says the opposite, or a later term overrides it), or **Not provided** (the document that would answer it hasn't been supplied; ask for it in Round 1). Rate the documents actually provided. A trust center summary or a sales answer isn't a contract term.

Commercial terms such as liability caps, indemnities, and pricing belong to Legal and Procurement. The checklist flags them where they affect data protection, and leaves the negotiation to them.

## Contents

1. Scope and roles
2. GDPR Art. 28 core terms
3. Subprocessors, transfers, and location
4. US state processor and service provider terms
5. Student data terms
6. AI terms
7. Security, breach, audit, and deletion
8. Red flags
9. Other laws to flag for counsel

---

## 1. Scope and roles

| # | Check | Basis |
|---|---|---|
| 1.1 | The contract describes the subject matter, duration, nature and purpose of processing, types of personal data, and categories of data subjects | GDPR Art. 28(3) |
| 1.2 | The roles the contract assigns match the facts for each operation. Look for vendor rights to use data for its own purposes (analytics, product improvement, model training, benchmarking, marketing). Such a right makes the vendor a controller for that use. | GDPR Arts. 4(7)–(8), 28(10); `gdpr.md` §2 |
| 1.3 | Which document wins when the DPA, MSA, order form, AI terms, and online terms conflict. If the vendor can change online terms: whether changes need notice, whether the company can object or terminate, whether the order form overrides them, and whether a material reduction in data protection gives a remedy. Ask for an order-form term blocking material reductions without notice and a right to exit. | Contract construction |
| 1.4 | Which vendor entity signs, and whether it matches the entity on the DPF listing and the security reports | Transfers; assurance |

## 2. GDPR Art. 28 core terms

| # | Check | Basis |
|---|---|---|
| 2.1 | Processes only on the company's documented instructions, including for transfers, unless law requires otherwise, and tells the company of that legal requirement first | Art. 28(3)(a) |
| 2.2 | People authorized to process the data are bound by confidentiality | Art. 28(3)(b) |
| 2.3 | Takes all measures required by Art. 32, described specifically enough to assess (an annex of technical and organizational measures) | Art. 28(3)(c) |
| 2.4 | Respects the conditions for engaging subprocessors (§3) | Art. 28(3)(d) |
| 2.5 | Assists with data subject requests, with a response time | Art. 28(3)(e) |
| 2.6 | Assists with security, breach notification, DPIAs, and prior consultation | Art. 28(3)(f) |
| 2.7 | Deletes or returns all personal data at the end of the services, at the company's choice, and deletes existing copies unless law requires storage | Art. 28(3)(g) |
| 2.8 | Makes available all information needed to demonstrate compliance, and allows and contributes to audits and inspections | Art. 28(3)(h) |
| 2.9 | Tells the company immediately if an instruction infringes data protection law | Art. 28(3), final subparagraph |
| 2.10 | In writing, including electronic form | Art. 28(9) |
| 2.11 | UK and Swiss equivalents covered where those data subjects are in scope | UK GDPR Art. 28; FADP Art. 9 |

## 3. Subprocessors, transfers, and location

| # | Check | Basis |
|---|---|---|
| 3.1 | Subprocessors need prior specific or general written authorization; under general authorization, advance notice of changes and a real right to object (with a remedy, such as termination without penalty) | Art. 28(2) |
| 3.2 | Same data protection obligations flow down to subprocessors, and the vendor stays fully liable | Art. 28(4) |
| 3.3 | A current subprocessor list, with each subprocessor's service, data, and location. For AI vendors, the model providers and hosting regions are named. | Art. 28(2); AIUC-1 E006, E011 |
| 3.4 | Processing and storage locations, and remote access locations (support, engineering), stated | Chapter V; AIUC-1 E011 |
| 3.5 | Transfer mechanism for each restricted transfer: an active DPF certification for the right entity, covering the UK Extension and Swiss-US DPF where relevant (check dataprivacyframework.gov); or SCCs with the correct module; plus the UK Addendum or IDTA and Swiss adaptations | Arts. 44–46; `gdpr.md` §11 |
| 3.6 | SCCs incorporated as a fallback if the DPF is invalidated (*Volatile*: DPF litigation) | `gdpr.md` §11 |
| 3.7 | A transfer impact assessment or vendor-supplied transfer information for SCC transfers, and commitments on government access requests (notice where lawful, challenge, minimization) | *Schrems II*; EDPB Recommendations 01/2020 |

## 4. US state processor and service provider terms

| # | Check | Basis |
|---|---|---|
| 4.1 | Virginia-model terms: instructions; nature, purpose, type of data, and duration; confidentiality; deletion or return; information to show compliance; assessments or an annual independent assessment; subcontractor flow-down with notice and a chance to object; help with consumer requests, security, breach notice, and assessments | `us-state-privacy.md` §4 |
| 4.2 | California service provider or contractor terms: no selling or sharing; use limited to the specified business purposes; no use outside the direct business relationship; no combining with other data except as the regulations allow; CCPA compliance and the same level of protection; the company's right to take reasonable steps to stop unauthorized use; notice if the vendor can't comply; contractor certification | Cal. Civ. Code §§ 1798.100(d), 1798.140(ag), (j); CCPA Regs. § 7051 |
| 4.3 | Without the terms in 4.2, the vendor is a "third party," and disclosure may be a sale or share. Record this as a finding. | Cal. Civ. Code § 1798.140 |
| 4.4 | Sensitive data and minors: no use beyond the service; honors opt-outs passed on by the company | `us-state-privacy.md` §3 |

## 5. Student data terms

Use when the vendor will receive education records or student data. Details are in `ferpa.md`, §7 and §11.

| # | Check | Basis |
|---|---|---|
| 5.1 | The FERPA exception is named, and the terms support each of its conditions as facts: an institutional function, the institution's direct control, use and redisclosure limits | 34 CFR §§ 99.31(a)(1)(i)(B), 99.33 |
| 5.2 | No use for advertising, profiling, or product development unrelated to the service, and no model training on student data, unless the institution authorizes it specifically | `ferpa.md` §4; SOPIPA |
| 5.3 | The state student privacy law terms for each customer's state, such as New York's data security and privacy plan, Parents' Bill of Rights, and **7-day** breach notice (8 NYCRR 121.10(a)); Illinois SOPPA's data privacy agreement; California Ed. Code § 49073.1 contract terms | `ferpa.md` §11 |
| 5.4 | COPPA: if users under 13 are involved, data collected on school authorization is used only for the school's purpose | `ferpa.md` §10 |
| 5.5 | De-identified data: whether the vendor may keep or use it, and a ban on re-identification | 34 CFR § 99.31(b) |

## 6. AI terms

Use when the vendor provides an AI system, model, or agent, including AI features embedded in a product the company already buys. Benchmark against AIUC-1 (`aiuc-1.md`) in **vendor benchmark** mode.

| # | Check | Basis |
|---|---|---|
| 6.1 | **Training and improvement:** separate (a) training or fine-tuning foundation models, (b) improving or evaluating the vendor's own models or features, and (c) retention for abuse monitoring or operations. For each: the default, opt-in or opt-out, whose models are covered, the exceptions, and whether the commitment is in the contract or only in a policy that can change. A plan tier is not a control; get written terms. Ask whether training has already happened on the company's data, since turning a setting off now doesn't establish past use. | AIUC-1 A001; GDPR Art. 28(10) |
| 6.2 | **Retention:** what is kept (prompts, outputs, files, embeddings, logs), for how long, and why, including abuse-monitoring and safety logs; whether zero-retention options exist and are switched on | AIUC-1 A001, E005; GDPR Art. 5(1)(e) |
| 6.3 | **Outputs:** ownership of outputs, usage rights, and deletion; IP infringement protection for outputs | AIUC-1 A002, A007 |
| 6.3a | **Scores and inferences about people** (sentiment, engagement, risk, performance): the technical definition, the input modalities (text, voice, video, biometrics), the intended purpose, sample outputs, and how the company will use them, especially to evaluate employees. Disable pending assessment if the function could be emotion recognition from biometric data (AI Act Art. 5(1)(f)) or employee evaluation (Annex III point 4(b)). | AIUC-1 C003, E017; `eu-ai-act.md` §4–5 |
| 6.4 | **Isolation:** no exposure of the company's data to other customers; limits on what an agent can access, based on task, user role, and context | AIUC-1 A003, A005, A006 |
| 6.5 | **Agent actions:** for agents that act, what tools and permissions they have, how actions beyond scope are blocked, and who is liable for an unauthorized action | AIUC-1 B006, D003 |
| 6.6 | **Model changes:** notice of material model or provider changes, and the right to object or exit | AIUC-1 E004, E006 |
| 6.7 | **Incident duties:** notice of AI failures that harm the company or its users (security breaches, harmful outputs, damaging hallucinations), with timelines | AIUC-1 E001–E003 |
| 6.8 | **Logging:** activity logs available to the company for investigation, retained long enough for its duties (AI Act deployers keep logs at least 6 months) | AIUC-1 E015; AI Act Art. 26(6) |
| 6.9 | **Transparency:** disclosure that users are interacting with AI where needed; model cards or system documentation; for high-risk systems, the provider's instructions for use | AIUC-1 E016, E017; AI Act Arts. 13, 50 |
| 6.10 | **AI Act roles:** who is provider and who is deployer; whether the company's use or configuration could make it a provider (Art. 25); what information the vendor supplies for the company's deployer duties | `eu-ai-act.md` §3, §7 |
| 6.11 | **AIUC-1 certification:** whether the vendor holds a certificate, and, from the certificate and audit report (AIUC publishes no public registry; ask the vendor for them): the **product** in scope (certification usually covers specific agents), the **release** audited, the **report date**, expiry (valid 12 months), whether the quarterly evaluations are current, and the exclusions in the Statement of Applicability. A certificate is strong evidence, not a warranty. | `aiuc-1.md` §3; AIUC-1 FAQ |
| 6.12 | **Without certification:** the vendor's answers on the AIUC-1 mandatory requirements that apply to its capabilities, with evidence, starting with A001–A006, B001, B006, C001, D003, E001, E004, E006, E015, and E016 | `aiuc-1.md` §4 |

## 7. Security, breach, audit, and deletion

| # | Check | Basis |
|---|---|---|
| 7.1 | Security assurance: SOC 2 Type II or ISO 27001 report, its period, the systems and subprocessors in scope, any bridge letter, the exceptions noted, and their remediation status. A report that doesn't cover the service in use doesn't count, and a report is evidence about specified controls, not a guarantee. | Art. 28(1); Art. 32 |
| 7.2 | Breach notice to the company without undue delay, with a stated maximum (commonly 24 to 72 hours) that leaves the company time to meet its own 72-hour GDPR deadline and any shorter contractual or state deadlines, such as New York's 7 days for student data | Arts. 33(2), 28(3)(f); 8 NYCRR 121.10(a) |
| 7.3 | Content and cooperation in breach notices: what happened, data and people affected, measures taken, and a contact | Art. 33(3) |
| 7.4 | Audit rights: reports, questionnaires, and on-site audits for cause, without unreasonable cost or notice barriers | Art. 28(3)(h) |
| 7.5 | Deletion at the end of the contract and on request, covering backups (with a timeline), subprocessors, derived data, embeddings, and fine-tuned models; certification of deletion on request | Art. 28(3)(g) |
| 7.6 | Data subject request support, including from subprocessors and model providers | Art. 28(3)(e) |

## 8. Red flags

Raise each of these as a finding, even when the rest of the contract is strong:

- The vendor may use customer data, inputs, or outputs to train or improve its models or services, by default or through a policy it can change
- The vendor may change its online terms, DPA, or subprocessor list without notice or a right to object
- The vendor may create, keep, or use "aggregated," "de-identified," or "anonymized" data with no definition, standard, or ban on re-identification. Ownership of aggregated data doesn't by itself make the vendor a controller: ask whether the output is genuinely anonymous statistics or still pseudonymous, and assess the vendor's role for creating it
- The DPA covers only some of the services or entities actually used
- Breach notice has no deadline, or a long one
- Deletion excludes backups indefinitely, or excludes derived data and models
- The vendor's liability for data protection breaches is capped below a level Legal is comfortable with, or excluded (flag for Legal)
- The vendor disclaims any processor role while processing on the company's behalf
- An AI feature was turned on in an existing product without a contract update

---

## 9. Other laws to flag for counsel

The reference files don't cover these laws, but vendor reviews run into them often. When the facts point to one, raise it as a verify flag for Legal, with the fact that triggered it. Don't state a conclusion.

| Trigger in the facts | Law to flag |
|---|---|
| The vendor records calls, meetings, or chats | US call-recording consent laws, including all-party consent states such as California (Cal. Penal Code § 632); notice to EU and UK participants |
| Session replay, chat widgets, or pixels capture what users type or view | State wiretap claims, such as California's CIPA (Cal. Penal Code § 631) |
| Voiceprints, face geometry, or other biometric identifiers | Illinois BIPA; Texas CUBI; Washington biometric law |
| Health information outside HIPAA, including inferred health | Washington My Health My Data Act and similar consumer health data laws (Nevada, Connecticut) |
| Protected health information from covered entities | HIPAA business associate terms down the subprocessor chain. HIPAA is outside this suite's scope, so route to counsel. |
| Background checks or consumer reports | FCRA disclosure, authorization, and adverse action duties; state and city fair-chance laws |
