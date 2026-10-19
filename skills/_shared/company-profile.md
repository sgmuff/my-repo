# Company profile

Every skill in the suite reads this file at the start of a run. Fill it in once, replacing each `TODO`, and the skills will stop asking for these details. When a skill finds a `TODO` that matters to the current run, it asks for the value and offers to save it here.

This file holds facts that stay stable between runs. It deliberately leaves out the company's role (controller, processor, provider, deployer). Roles change from one activity to the next, so each skill proposes a role for each run and asks you to confirm it. See `conventions.md`, section 5.

## Organization

- Legal entity name: TODO
- Short name used in documents: TODO
- Sector, and any sector rules that apply (for example, education, which brings in FERPA): TODO
- EU establishment, if any (this decides the lead supervisory authority under the one-stop shop): TODO
- Lead supervisory authority: TODO
- EU Article 27 representative, if there is no EU establishment: TODO
- UK representative or establishment: TODO
- Swiss representative, if any: TODO

## People

- Privacy lead, who prepares and approves privacy and AI governance work: TODO
- DPO (name and contact), if appointed: TODO
- Legal counsel, for escalations: TODO
- Security contact, for control questions: TODO
- Executive who accepts High residual risk and signs the California CPPA attestation: TODO

The approval rules that use these people are in `approvals.md`.

## Business areas

List the business areas that request reviews or own systems, with a default contact for each. Every deliverable records the requesting business area and the system owner, so a short list here saves a question on each run.

| Business area | Default contact (name, role) |
|---|---|
| TODO | TODO |

## Regimes in scope

Delete any that don't apply.

- EU GDPR
- UK GDPR and the Data Protection Act 2018, as amended by the Data (Use and Access) Act 2025
- Swiss FADP
- FERPA (education records), when the activity touches student data
- US comprehensive state privacy laws: list the states where the company meets the applicability thresholds, and review this list each year. Default: all states in `references/us-state-privacy.md`, §2. TODO
- EU AI Act
- AIUC-1
- NIST Privacy Framework (organizing framework for the privacy program)
- NIST AI RMF and ISO/IEC 42001 (AI governance mappings)

Conditional regimes (confirmed 2026-10-18). Their reference files exist, checked on 2026-10-18 against secondary sources only, so the catalog entries apply; have counsel review each file before relying on it:

- EU AI Act general-purpose AI model duties (Art. 53, 55): the company trains or markets general-purpose models
- GLBA Safeguards Rule (16 CFR Part 314): the company serves financial institutions, including colleges in federal student aid
- HIPAA Security Rule (45 CFR Part 164): the company is a covered entity or business associate
- NIS2 Directive, as transposed: the company is an essential or important entity
- Quebec Law 25: the company processes personal information of people in Quebec

## Defaults

- Output root folder for deliverables: `compliance/` (relative to the repository root). The folder layout is in `conventions.md`, section 8.
- Risk matrix: 3x3, defined in `references/risk-method.md`.
- Standard security baseline, so deliverables can cite it instead of restating it (for example, SOC 2 Type II report date, ISO 27001 certificate, encryption at rest and in transit, SSO and MFA, links to policies): TODO
- Standard transfer mechanisms in use (for example, EU SCCs Module 2 or 3, UK Addendum, EU-US DPF certification): TODO
- Standard DPA or data processing terms the company offers or requires, with a link: TODO

## Connected systems

Leave a line blank if the company doesn't use that system. `connectors.md` explains how each one is used.

- Ticketing for action items: Jira, ServiceNow, or none. TODO
  - Jira project key for privacy and AI governance actions: TODO
  - ServiceNow table or module for actions or risks (for example, `sn_grc_issue`, or an incident or task table): TODO
- Document source for system documentation, vendor contracts, and PRDs (for example, Google Drive, Confluence, SharePoint, or this repository): TODO
- Publishing target for approved assessments: none for now. Confluence is planned. Storage moves to Azure Blob Storage later.
