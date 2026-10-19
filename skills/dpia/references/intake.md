# Intake checklist

Fill in each field from the brief first, and record each fact in the fact register with its status (`../../_shared/conventions.md`, §6). Then ask about the gaps in two rounds:

- **[R1] Round 1, blockers:** facts that could change the screening outcome, a legal determination, or whether the activity can launch. Send these first, alone, in one short numbered message. Usually under 15 questions: pick the R1 items that are actually open, not all of them.
- **[R2] Round 2, completion:** everything else. Send it with the draft.

Items marked **Evidence** ask for a document, not just an answer. Record what was provided. Mark anything the user can't answer as `TBC`, and say whether it blocks launch.

## A. Overview

1. [R2] Name of the activity, and the project or ticket reference
2. [R2] Type: new feature, change to an existing feature, new vendor, or internal processing (HR, security, marketing)
3. [R2] **Requesting business area**, and the **system owner** if different. Both appear in document control and approval routing. Use the business area list in the company profile.
4. [R2] Technical owner
5. [R1] Planned launch date, and whether the processing has already started, including pilots and tests on real data. If it has: what was captured, whose data, whether any sensitive field was exposed, where the data went (including any model-training pipeline), and whether deletion or access limits are needed now. A future launch gate doesn't address data already collected; see SKILL.md, step 1.
6. [R1] For each processing operation, who decides its purposes and essential means. The answers drive the proposed roles under GDPR, US state law, and FERPA (SKILL.md, step 1). Ask about operations the company may decide on for itself, such as model training or product analytics. **Evidence:** the customer contract or DPA.

## B. Purpose and context

7. [R1] Each purpose, stated specifically. Write "Generate meeting summaries for meeting participants," not "Improve the product."
8. [R1] For each score, flag, or prediction: is it about a natural person, a business account, or both, and how is the distinction implemented? What exactly does it change, and who can act on it?
9. [R1] For each automated outcome (closing, routing, flagging, recommending): what are the real consequences for the person? Can it affect a deadline, a refund, a complaint, an exam result, placement, a disciplinary step, or access to a service?
10. [R2] Expected benefit to the individual, the customer, and the company. US benefit-risk statements need this.
11. [R2] Whether individuals would reasonably expect this processing, given their relationship with the company
12. [R1] Any secondary uses: analytics, product improvement, model training, staff performance evaluation, or marketing. Each one is a separate purpose. Keep product improvement apart from model training, since their contractual permissions often differ.
13. [R1] The proposed lawful basis for each purpose, and, where special category data may be processed, the Art. 9 condition relied on. A legitimate interests assessment doesn't supply an Art. 9 condition.
14. [R1] What evidence already exists for the proposed safeguards: test results, vendor security reports, retention configuration, access-control reviews, accuracy data, or an existing legitimate interests assessment. **Evidence:** whatever exists.

## C. Data subjects

15. [R2] Categories, such as customer end users, customer admins, prospects, employees, contractors, or third parties captured in content (bystanders on camera, people named in tickets)
16. [R2] Approximate number of people and geographic spread (EEA, UK, Switzerland, US states, other). Estimates are fine; don't hold up the core analysis for exact counts. List the states where affected people live separately from the states whose applicability thresholds the company meets.
17. [R1] **Territorial scope:** the company's establishments (EU, UK, Swiss subsidiaries, offices, or staff), and whether any of them is involved in this processing. The GDPR can apply on establishment alone (`gdpr.md`, §1a).
18. [R1] **Children:** is the service directed at, or likely to be used by, anyone under 18? Ask for facts, not conclusions: does the company collect date of birth, age, or grade; do customers identify users under 13 when provisioning accounts; and what age information can the company and its vendors see? Whether that amounts to actual knowledge under COPPA is a legal determination for later. Ages vary by law: GDPR Art. 8 sets 13 to 16 by member state, COPPA covers under 13, and several US states protect minors under 16 or 18.
19. [R2] Other vulnerable groups, such as employees, patients, students with disabilities, or people in financial difficulty
20. [R1] **Students:** does the activity use education records or PII from education records? If so, under which FERPA exception, in which states are the customers, and does each institution authorize each use, including analytics and model training? **Evidence:** the district or university agreement (`../../_shared/references/ferpa.md`).

## D. Personal data

21. [R2] Data elements, listed as specifically as possible
22. [R1] **Special category data (Art. 9):** racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data used for identification, health, sex life, or sexual orientation. Inferred special category data counts, such as health inferred from content.
23. [R1] **Biometrics, precisely** (`gdpr.md`, §3): does the system only capture images, detect faces or objects, verify identity against a reference, create or keep templates or embeddings, or infer behavior, emotion, or intent from face, gaze, or voice? **Evidence:** technical documentation of inputs and outputs.
24. [R2] **Criminal offense data (Art. 10)**
25. [R2] **US "sensitive" data**, which is broader in many states. Keep it distinct from GDPR special category data:
    - Precise geolocation
    - Account login credentials and payment card data
    - Government ID numbers
    - Financial account details
    - Contents of mail, email, or texts (California)
    - Neural data (California, Colorado, and others)
    - Citizenship or immigration status
    - Data from a known child
    - Transgender or nonbinary status (some states)
26. [R1] Whether the processing includes free-text content, recordings, or files that may carry unpredictable personal data, and whether attachments and files are actually sent onward (for example, to a model or vendor) or only stored
27. [R2] Inferences or derived data produced, such as scores, profiles, summaries, or embeddings

## E. Sources

28. [R2] Collected directly from the individual, from the customer, observed through telemetry or cookies, or from a third party. For a third party, name it and say how it is lawful to receive the data.
29. [R2] Whether individuals are aware of the collection when it happens

## F. Recipients, processors, and subprocessors

30. [R2] Internal teams with access, and on what basis (role-based access, least privilege)
31. [R1] Each processor or subprocessor: name, service, data shared, and location. **Evidence:** the DPA, the retention and training configuration, the subprocessor list, and the latest SOC 2 or ISO report date.
32. [R1] Whether any vendor uses the data for its own purposes, such as model training, analytics, or ads. That vendor may be a controller for that use. **Evidence:** the vendor's terms on data use.
33. [R2] Other third-party recipients, such as customers' integrations, partners, or authorities
34. [R1] Whether the data is sold or shared for cross-context behavioral advertising, as US state laws define those terms

## G. International transfers

35. [R2] Each transfer: from, to, recipient, and data
36. [R2] Mechanism for each, verified for each entity and destination. **Evidence:** the DPF listing (with its scope: EU, UK Extension, Swiss), the SCC module, or the IDTA.
    - **EU:** an adequacy decision, the EU-US DPF (check that the recipient is certified and active), the 2021 SCCs (record the module: 1 C2C, 2 C2P, 3 P2P, 4 P2C), BCRs, or an Art. 49 derogation (occasional transfers only)
    - **UK:** adequacy regulations, the UK Extension to the DPF, the IDTA, or the UK Addendum
    - **Switzerland:** an adequacy listing, the Swiss-US DPF, or SCCs with Swiss adaptations
37. [R2] A transfer impact assessment on file for SCC or BCR transfers, and any supplementary measures. If none exists, recommend the `tia` skill.
38. [R2] Remote access from third countries, such as support staff. Remote access counts as a transfer.

## H. Retention and deletion

39. [R2] Retention period for each data category, the purpose that justifies it, and the trigger that starts it. A vendor default isn't a justification.
40. [R2] How deletion happens: automatic or manual, and whether it reaches backups, logs, analytics copies, vendor copies, derived datasets, and trained models
41. [R2] Legal holds and any statutory retention

## I. Security

Cite the baseline in the company profile, and record only what is specific to this activity. **Evidence:** configuration exports or test results for each control a risk rating depends on.

42. [R2] Encryption in transit and at rest, and key management
43. [R2] Access controls, authentication, and how privileged access is managed
44. [R2] Logging and monitoring, plus the incident response path
45. [R1] Pseudonymization, masking, redaction, or aggregation, and how each one is tested (including edge cases such as drafts, deleted text, and metadata in URLs)
46. [R2] Environment separation, such as whether production data is used in testing

## J. Automated decisions and AI

47. [R1] Whether any decision about a person is made solely by automated means, what it affects (see item 9), and what human review happens before it takes effect
48. [R1] For human review: what the reviewer sees (the original evidence or only the flag), what training they get, and whether they must record an independent reason before acting
49. [R1] Remedies: how a person challenges an outcome, sees the evidence, gets a timely human review before any adverse finding, and uses an alternative process without penalty, including people with disabilities, assistive technology, or poor connectivity. Whether people are told what is captured, why, who sees it, and for how long.
50. [R1] Models: built in-house or supplied by a third party, and whether the company develops the AI system or switches on a vendor's feature (this decides the AI Act role; `eu-ai-act.md`, §3). Is customer data used to train or fine-tune any model, including the vendor's? Can the customer opt out?
51. [R2] Performance: accuracy, calibration, false positive and false negative rates, and how they vary across languages and relevant groups, with sample sizes and test conditions. For any confidence threshold, why it was chosen and how it performs on a representative test set. Minimum performance required before launch, and the rollback process if performance drops. **Evidence:** test results. (Round 1 for assistance packs and any system whose outputs can lead to adverse decisions.)
52. [R2] How errors are caught, corrected, and fed back

## K. Consultation

53. [R2] Whether the DPO or counsel has given advice yet (Art. 35(2)). Record it separately from the controller's decision.
54. [R2] Whether data subjects or their representatives have been consulted, or will be, such as through user research, student or parent groups, or a works council. Art. 35(9) asks for their views "where appropriate"; it isn't mandatory in every case. Record what was done, what is planned, or why it wasn't appropriate.
55. [R2] Security, legal, and engineering contributors, with their roles. Several laws require reviewers' names and titles; `us-state-privacy.md` lists which.
56. [R2] Who advises, who accepts residual risk, and who authorizes launch. Don't assume they are the same person (`approvals.md`).
