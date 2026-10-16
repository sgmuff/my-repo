# NIST Privacy Framework

| Field | Value |
|---|---|
| Covers | NIST Privacy Framework: A Tool for Improving Privacy through Enterprise Risk Management, Version 1.0 (NIST CSWP 01162020) |
| Version covered | 1.0 (January 16, 2020), the current final version. Version 1.1 exists only as an Initial Public Draft (April 14, 2025). |
| Sources | nist.gov/privacy-framework; nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01162020.pdf (Core text in §4 extracted from this PDF on 2026-10-16) |
| Last verified | 2026-10-16 |
| Review interval | Quarterly until 1.1 is final, then annually |
| Volatile points | §1 (1.1 finalization changes the Core's structure and IDs) |

The privacy workflows are organized around this framework's five functions. Each deliverable tags its findings with Core subcategory IDs, so a program assessment can roll up evidence from DPIAs, vendor reviews, and RoPA entries without redoing them.

## Contents

1. Status and the 1.1 draft
2. How the framework works: Core, Profiles, Tiers
3. Map: categories to laws and to the suite's skills
4. The Core (all 100 subcategories)

---

## 1. Status and the 1.1 draft

Version 1.0 is the current final framework. NIST released Privacy Framework 1.1 as an Initial Public Draft on April 14, 2025, with comments closing June 13, 2025, and said it planned a final version later that year. As of October 16, 2026, NIST's Privacy Framework page still presents 1.1 as a draft.

The draft aligns the Core with the Cybersecurity Framework 2.0, revises the Govern-P and Protect-P functions, renumbers subcategories, and adds guidance on AI and privacy risk. *Volatile:* when 1.1 is final, update this file, map old IDs to new ones, and re-tag open assessments. Until then, cite 1.0 IDs.

Tennessee's privacy law gives an affirmative defense to a controller whose privacy program reasonably conforms to the NIST Privacy Framework (`us-state-privacy.md`, §2). That makes the program assessment worth doing carefully.

---

## 2. How the framework works: Core, Profiles, Tiers

**Core.** Five functions (Identify-P, Govern-P, Control-P, Communicate-P, Protect-P), 18 categories, and 100 subcategories. Subcategories are outcomes, not controls. An outcome can be met by many different controls.

**Profiles.** A Profile is the set of subcategories the organization selects as priorities.

- The **Current Profile** records which outcomes the organization achieves today.
- The **Target Profile** records the outcomes it needs to achieve, given its laws, risks, and mission.
- The gap between them, ranked by risk, becomes the roadmap.

An organization may leave subcategories out of a Target Profile when they don't apply, with a recorded reason. Not every subcategory is required.

**Implementation Tiers.** A Tier describes how mature the organization's privacy risk management is overall, not per subcategory:

| Tier | Name | Summary |
|---|---|---|
| 1 | Partial | Privacy risk management is ad hoc and reactive. Limited awareness of privacy risk at the organizational level. |
| 2 | Risk Informed | Management approves risk practices, but they may not be organization-wide policy. Awareness exists but isn't consistent. |
| 3 | Repeatable | Risk practices are approved and expressed as policy, updated regularly, and applied consistently. |
| 4 | Adaptive | Practices adapt from lessons learned and predictive indicators. Privacy risk is part of the organizational culture. |

The `program-assessment` skill (Wave 4) builds Current and Target Profiles and the roadmap.

---

## 3. Map: categories to laws and to the suite's skills

This map is the suite's own and is not part of NIST's framework. It ties each category to the legal provisions it helps satisfy, and to the skill that produces evidence for it. Use it to tag findings and to plan program assessments. Provision-level detail is in `gdpr.md`, `us-state-privacy.md`, and `ferpa.md`.

| Category | GDPR, UK GDPR, FADP | US state laws | FERPA | Skills producing evidence |
|---|---|---|---|---|
| ID.IM-P Inventory and Mapping | Art. 30; FADP Art. 12 | Minnesota data inventory; CCPA Regs. risk assessment operational elements | § 99.32 disclosure records | `ropa`, `ai-intake` |
| ID.BE-P Business Environment | Arts. 4(7)–(8), 26, 28 (roles) | Controller and processor roles | School official status, § 99.31(a)(1)(i)(B) | Every skill (role step) |
| ID.RA-P Risk Assessment | Art. 35; FADP Art. 22 | State data protection assessments; CCPA Regs. §§ 7150–7157 | — | `dpia`, `ai-impact-assessment` |
| ID.DE-P Data Processing Ecosystem | Arts. 28, 44–49; FADP Arts. 9, 16–17 | Processor and service provider contracts | School official and studies agreements, §§ 99.31, 99.33, 99.35 | `vendor-review` |
| GV.PO-P Governance Policies | Arts. 5(2), 24, 37–39 | Privacy program duties; Tennessee NIST defense | Annual notification, § 99.7 | `program-assessment`, `notice-and-policy` |
| GV.RM-P Risk Management Strategy | Arts. 24, 32(2) | Risk-based assessment duties | — | `approvals.md`, `risk-method.md` |
| GV.AT-P Awareness and Training | Arts. 32(4), 39(1)(b) | — | Reasonable methods, § 99.31(a)(1)(ii) | `program-assessment` |
| GV.MT-P Monitoring and Review | Art. 35(11); UK DUAA complaints duty | Assessment review cadences | Complaints, § 99.63 | `program-assessment`, `regulatory-change` |
| CT.PO-P Data Processing Policies | Arts. 6–7, 12–22, 25 | Consent for sensitive data; opt-outs; appeals | Consent, § 99.30 | `dsr-response`, `notice-and-policy` |
| CT.DM-P Data Processing Management | Arts. 5(1)(e), 15–20 | Access, correction, deletion, portability | Inspect and amend, §§ 99.10, 99.20 | `dsr-response`, `dpia` |
| CT.DP-P Disassociated Processing | Arts. 25, 32(1)(a), 89 | De-identified data definitions | De-identification, § 99.31(b) | `dpia` (mitigations) |
| CM.PO-P Communication Policies | Art. 12 | Privacy notice duties | Annual notification, § 99.7 | `notice-and-policy` |
| CM.AW-P Data Processing Awareness | Arts. 13–14, 19, 33–34 | Notices; breach notification laws | § 99.32 | `notice-and-policy`, `incident-assessment` |
| PR.PO-P Data Protection Policies | Arts. 25, 32 | Reasonable security; CCPA cybersecurity audits | — | `vendor-review`, `controls-and-evidence` |
| PR.AC-P Identity, Authentication, Access | Art. 32(1)(b), 32(4) | Reasonable security | § 99.31(a)(1)(ii) | `vendor-review`, `controls-and-evidence` |
| PR.DS-P Data Security | Art. 32(1)(a)–(c) | Reasonable security; breach law encryption safe harbors | — | `vendor-review`, `incident-assessment` |
| PR.MA-P Maintenance | Art. 32 | Reasonable security | — | `controls-and-evidence` |
| PR.PT-P Protective Technology | Art. 32(1)(b)–(c) | Reasonable security | — | `controls-and-evidence` |

---

## 4. The Core

The text below is NIST's, copied from Version 1.0 word for word (only curly apostrophes were straightened), including its "systems/products/services" shorthand.

### Identify-P (ID-P)

Develop the organizational understanding to manage privacy risk for individuals arising from data processing.

#### Inventory and Mapping (ID.IM-P)

Data processing by systems, products, or services is understood and informs the management of privacy risk.

| Subcategory | Outcome |
|---|---|
| ID.IM-P1 | Systems/products/services that process data are inventoried. |
| ID.IM-P2 | Owners or operators (e.g., the organization or third parties such as service providers, partners, customers, and developers) and their roles with respect to the systems/products/services and components (e.g., internal or external) that process data are inventoried. |
| ID.IM-P3 | Categories of individuals (e.g., customers, employees or prospective employees, consumers) whose data are being processed are inventoried. |
| ID.IM-P4 | Data actions of the systems/products/services are inventoried. |
| ID.IM-P5 | The purposes for the data actions are inventoried. |
| ID.IM-P6 | Data elements within the data actions are inventoried. |
| ID.IM-P7 | The data processing environment is identified (e.g., geographic location, internal, cloud, third parties). |
| ID.IM-P8 | Data processing is mapped, illustrating the data actions and associated data elements for systems/products/services, including components; roles of the component owners/operators; and interactions of individuals or third parties with the systems/products/services. |

#### Business Environment (ID.BE-P)

The organization's mission, objectives, stakeholders, and activities are understood and prioritized; this information is used to inform privacy roles, responsibilities, and risk management decisions.

| Subcategory | Outcome |
|---|---|
| ID.BE-P1 | The organization's role(s) in the data processing ecosystem are identified and communicated. |
| ID.BE-P2 | Priorities for organizational mission, objectives, and activities are established and communicated. |
| ID.BE-P3 | Systems/products/services that support organizational priorities are identified and key requirements communicated. |

#### Risk Assessment (ID.RA-P)

The organization understands the privacy risks to individuals and how such privacy risks may create follow-on impacts on organizational operations, including mission, functions, other risk management priorities (e.g., compliance, financial), reputation, workforce, and culture.

| Subcategory | Outcome |
|---|---|
| ID.RA-P1 | Contextual factors related to the systems/products/services and the data actions are identified (e.g., individuals' demographics and privacy interests or perceptions, data sensitivity and/or types, visibility of data processing to individuals and third parties). |
| ID.RA-P2 | Data analytic inputs and outputs are identified and evaluated for bias. |
| ID.RA-P3 | Potential problematic data actions and associated problems are identified. |
| ID.RA-P4 | Problematic data actions, likelihoods, and impacts are used to determine and prioritize risk. |
| ID.RA-P5 | Risk responses are identified, prioritized, and implemented. |

#### Data Processing Ecosystem Risk Management (ID.DE-P)

The organization's priorities, constraints, risk tolerance, and assumptions are established and used to support risk decisions associated with managing privacy risk and third parties within the data processing ecosystem. The organization has established and implemented the processes to identify, assess, and manage privacy risks within the data processing ecosystem.

| Subcategory | Outcome |
|---|---|
| ID.DE-P1 | Data processing ecosystem risk management policies, processes, and procedures are identified, established, assessed, managed, and agreed to by organizational stakeholders. |
| ID.DE-P2 | Data processing ecosystem parties (e.g., service providers, customers, partners, product manufacturers, application developers) are identified, prioritized, and assessed using a privacy risk assessment process. |
| ID.DE-P3 | Contracts with data processing ecosystem parties are used to implement appropriate measures designed to meet the objectives of an organization's privacy program. |
| ID.DE-P4 | Interoperability frameworks or similar multi-party approaches are used to manage data processing ecosystem privacy risks. |
| ID.DE-P5 | Data processing ecosystem parties are routinely assessed using audits, test results, or other forms of evaluations to confirm they are meeting their contractual, interoperability framework, or other obligations. |

### Govern-P (GV-P)

Develop and implement the organizational governance structure to enable an ongoing understanding of the organization's risk management priorities that are informed by privacy risk.

#### Governance Policies, Processes, and Procedures (GV.PO-P)

The policies, processes, and procedures to manage and monitor the organization's regulatory, legal, risk, environmental, and operational requirements are understood and inform the management of privacy risk.

| Subcategory | Outcome |
|---|---|
| GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data processing such as data uses or retention periods, individuals' prerogatives with respect to data processing) are established and communicated. |
| GV.PO-P2 | Processes to instill organizational privacy values within system/product/service development and operations are established and in place. |
| GV.PO-P3 | Roles and responsibilities for the workforce are established with respect to privacy. |
| GV.PO-P4 | Privacy roles and responsibilities are coordinated and aligned with third-party stakeholders (e.g., service providers, customers, partners). |
| GV.PO-P5 | Legal, regulatory, and contractual requirements regarding privacy are understood and managed. |
| GV.PO-P6 | Governance and risk management policies, processes, and procedures address privacy risks. |

#### Risk Management Strategy (GV.RM-P)

The organization's priorities, constraints, risk tolerances, and assumptions are established and used to support operational risk decisions.

| Subcategory | Outcome |
|---|---|
| GV.RM-P1 | Risk management processes are established, managed, and agreed to by organizational stakeholders. |
| GV.RM-P2 | Organizational risk tolerance is determined and clearly expressed. |
| GV.RM-P3 | The organization's determination of risk tolerance is informed by its role(s) in the data processing ecosystem. |

#### Awareness and Training (GV.AT-P)

The organization's workforce and third parties engaged in data processing are provided privacy awareness education and are trained to perform their privacy-related duties and responsibilities consistent with related policies, processes, procedures, and agreements and organizational privacy values.

| Subcategory | Outcome |
|---|---|
| GV.AT-P1 | The workforce is informed and trained on its roles and responsibilities. |
| GV.AT-P2 | Senior executives understand their roles and responsibilities. |
| GV.AT-P3 | Privacy personnel understand their roles and responsibilities. |
| GV.AT-P4 | Third parties (e.g., service providers, customers, partners) understand their roles and responsibilities. |

#### Monitoring and Review (GV.MT-P)

The policies, processes, and procedures for ongoing review of the organization's privacy posture are understood and inform the management of privacy risk.

| Subcategory | Outcome |
|---|---|
| GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors, including the organization's business environment (e.g., introduction of new technologies), governance (e.g., legal obligations, risk tolerance), data processing, and systems/products/services change. |
| GV.MT-P2 | Privacy values, policies, and training are reviewed and any updates are communicated. |
| GV.MT-P3 | Policies, processes, and procedures for assessing compliance with legal requirements and privacy policies are established and in place. |
| GV.MT-P4 | Policies, processes, and procedures for communicating progress on managing privacy risks are established and in place. |
| GV.MT-P5 | Policies, processes, and procedures are established and in place to receive, analyze, and respond to problematic data actions disclosed to the organization from internal and external sources (e.g., internal discovery, privacy researchers, professional events). |
| GV.MT-P6 | Policies, processes, and procedures incorporate lessons learned from problematic data actions. |
| GV.MT-P7 | Policies, processes, and procedures for receiving, tracking, and responding to complaints, concerns, and questions from individuals about organizational privacy practices are established and in place. |

### Control-P (CT-P)

Develop and implement appropriate activities to enable organizations or individuals to manage data with sufficient granularity to manage privacy risks.

#### Data Processing Policies, Processes, and Procedures (CT.PO-P)

Policies, processes, and procedures are maintained and used to manage data processing (e.g., purpose, scope, roles and responsibilities in the data processing ecosystem, and management commitment) consistent with the organization's risk strategy to protect individuals' privacy.

| Subcategory | Outcome |
|---|---|
| CT.PO-P1 | Policies, processes, and procedures for authorizing data processing (e.g., organizational decisions, individual consent), revoking authorizations, and maintaining authorizations are established and in place. |
| CT.PO-P2 | Policies, processes, and procedures for enabling data review, transfer, sharing or disclosure, alteration, and deletion are established and in place (e.g., to maintain data quality, manage data retention). |
| CT.PO-P3 | Policies, processes, and procedures for enabling individuals' data processing preferences and requests are established and in place. |
| CT.PO-P4 | A data life cycle to manage data is aligned and implemented with the system development life cycle to manage systems. |

#### Data Processing Management (CT.DM-P)

Data are managed consistent with the organization's risk strategy to protect individuals' privacy, increase manageability, and enable the implementation of privacy principles (e.g., individual participation, data quality, data minimization).

| Subcategory | Outcome |
|---|---|
| CT.DM-P1 | Data elements can be accessed for review. |
| CT.DM-P2 | Data elements can be accessed for transmission or disclosure. |
| CT.DM-P3 | Data elements can be accessed for alteration. |
| CT.DM-P4 | Data elements can be accessed for deletion. |
| CT.DM-P5 | Data are destroyed according to policy. |
| CT.DM-P6 | Data are transmitted using standardized formats. |
| CT.DM-P7 | Mechanisms for transmitting processing permissions and related data values with data elements are established and in place. |
| CT.DM-P8 | Audit/log records are determined, documented, implemented, and reviewed in accordance with policy and incorporating the principle of data minimization. |
| CT.DM-P9 | Technical measures implemented to manage data processing are tested and assessed. |
| CT.DM-P10 | Stakeholder privacy preferences are included in algorithmic design objectives and outputs are evaluated against these preferences. |

#### Disassociated Processing (CT.DP-P)

Data processing solutions increase disassociability consistent with the organization's risk strategy to protect individuals' privacy and enable implementation of privacy principles (e.g., data minimization).

| Subcategory | Outcome |
|---|---|
| CT.DP-P1 | Data are processed to limit observability and linkability (e.g., data actions take place on local devices, privacy-preserving cryptography). |
| CT.DP-P2 | Data are processed to limit the identification of individuals (e.g., de-identification privacy techniques, tokenization). |
| CT.DP-P3 | Data are processed to limit the formulation of inferences about individuals' behavior or activities (e.g., data processing is decentralized, distributed architectures). |
| CT.DP-P4 | System or device configurations permit selective collection or disclosure of data elements. |
| CT.DP-P5 | Attribute references are substituted for attribute values. |

### Communicate-P (CM-P)

Develop and implement appropriate activities to enable organizations and individuals to have a reliable understanding and engage in a dialogue about how data are processed and associated privacy risks.

#### Communication Policies, Processes, and Procedures (CM.PO-P)

Policies, processes, and procedures are maintained and used to increase transparency of the organization's data processing practices (e.g., purpose, scope, roles and responsibilities in the data processing ecosystem, and management commitment) and associated privacy risks.

| Subcategory | Outcome |
|---|---|
| CM.PO-P1 | Transparency policies, processes, and procedures for communicating data processing purposes, practices, and associated privacy risks are established and in place. |
| CM.PO-P2 | Roles and responsibilities (e.g., public relations) for communicating data processing purposes, practices, and associated privacy risks are established. |

#### Data Processing Awareness (CM.AW-P)

Individuals and organizations have reliable knowledge about data processing practices and associated privacy risks, and effective mechanisms are used and maintained to increase predictability consistent with the organization's risk strategy to protect individuals' privacy.

| Subcategory | Outcome |
|---|---|
| CM.AW-P1 | Mechanisms (e.g., notices, internal or public reports) for communicating data processing purposes, practices, associated privacy risks, and options for enabling individuals' data processing preferences and requests are established and in place. |
| CM.AW-P2 | Mechanisms for obtaining feedback from individuals (e.g., surveys or focus groups) about data processing and associated privacy risks are established and in place. |
| CM.AW-P3 | System/product/service design enables data processing visibility. |
| CM.AW-P4 | Records of data disclosures and sharing are maintained and can be accessed for review or transmission/disclosure. |
| CM.AW-P5 | Data corrections or deletions can be communicated to individuals or organizations (e.g., data sources) in the data processing ecosystem. |
| CM.AW-P6 | Data provenance and lineage are maintained and can be accessed for review or transmission/disclosure. |
| CM.AW-P7 | Impacted individuals and organizations are notified about a privacy breach or event. |
| CM.AW-P8 | Individuals are provided with mitigation mechanisms (e.g., credit monitoring, consent withdrawal, data alteration or deletion) to address impacts of problematic data actions. |

### Protect-P (PR-P)

Develop and implement appropriate data processing safeguards.

#### Data Protection Policies, Processes, and Procedures (PR.PO-P)

Security and privacy policies (e.g., purpose, scope, roles and responsibilities in the data processing ecosystem, and management commitment), processes, and procedures are maintained and used to manage the protection of data.

| Subcategory | Outcome |
|---|---|
| PR.PO-P1 | A baseline configuration of information technology is created and maintained incorporating security principles (e.g., concept of least functionality). |
| PR.PO-P2 | Configuration change control processes are established and in place. |
| PR.PO-P3 | Backups of information are conducted, maintained, and tested. |
| PR.PO-P4 | Policy and regulations regarding the physical operating environment for organizational assets are met. |
| PR.PO-P5 | Protection processes are improved. |
| PR.PO-P6 | Effectiveness of protection technologies is shared. |
| PR.PO-P7 | Response plans (Incident Response and Business Continuity) and recovery plans (Incident Recovery and Disaster Recovery) are established, in place, and managed. |
| PR.PO-P8 | Response and recovery plans are tested. |
| PR.PO-P9 | Privacy procedures are included in human resources practices (e.g., deprovisioning, personnel screening). |
| PR.PO-P10 | A vulnerability management plan is developed and implemented. |

#### Identity Management, Authentication, and Access Control (PR.AC-P)

Access to data and devices is limited to authorized individuals, processes, and devices, and is managed consistent with the assessed risk of unauthorized access.

| Subcategory | Outcome |
|---|---|
| PR.AC-P1 | Identities and credentials are issued, managed, verified, revoked, and audited for authorized individuals, processes, and devices. |
| PR.AC-P2 | Physical access to data and devices is managed. |
| PR.AC-P3 | Remote access is managed. |
| PR.AC-P4 | Access permissions and authorizations are managed, incorporating the principles of least privilege and separation of duties. |
| PR.AC-P5 | Network integrity is protected (e.g., network segregation, network segmentation). |
| PR.AC-P6 | Individuals and devices are proofed and bound to credentials, and authenticated commensurate with the risk of the transaction (e.g., individuals' security and privacy risks and other organizational risks). |

#### Data Security (PR.DS-P)

Data are managed consistent with the organization's risk strategy to protect individuals' privacy and maintain data confidentiality, integrity, and availability.

| Subcategory | Outcome |
|---|---|
| PR.DS-P1 | Data-at-rest are protected. |
| PR.DS-P2 | Data-in-transit are protected. |
| PR.DS-P3 | Systems/products/services and associated data are formally managed throughout removal, transfers, and disposition. |
| PR.DS-P4 | Adequate capacity to ensure availability is maintained. |
| PR.DS-P5 | Protections against data leaks are implemented. |
| PR.DS-P6 | Integrity checking mechanisms are used to verify software, firmware, and information integrity. |
| PR.DS-P7 | The development and testing environment(s) are separate from the production environment. |
| PR.DS-P8 | Integrity checking mechanisms are used to verify hardware integrity. |

#### Maintenance (PR.MA-P)

System maintenance and repairs are performed consistent with policies, processes, and procedures.

| Subcategory | Outcome |
|---|---|
| PR.MA-P1 | Maintenance and repair of organizational assets are performed and logged, with approved and controlled tools. |
| PR.MA-P2 | Remote maintenance of organizational assets is approved, logged, and performed in a manner that prevents unauthorized access. |

#### Protective Technology (PR.PT-P)

Technical security solutions are managed to ensure the security and resilience of systems/products/services and associated data, consistent with related policies, processes, procedures, and agreements.

| Subcategory | Outcome |
|---|---|
| PR.PT-P1 | Removable media is protected and its use restricted according to policy. |
| PR.PT-P2 | The principle of least functionality is incorporated by configuring systems to provide only essential capabilities. |
| PR.PT-P3 | Communications and control networks are protected. |
| PR.PT-P4 | Mechanisms (e.g., failsafe, load balancing, hot swap) are implemented to achieve resilience requirements in normal and adverse situations. |
