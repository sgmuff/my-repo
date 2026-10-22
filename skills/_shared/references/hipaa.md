---
title: HIPAA
summary: HIPAA Privacy, Security, and Breach Notification Rules for covered entities and business associates
version_summary: Rules through the 2013 Omnibus Rule; 2025 Security Rule proposal noted
last_verified: '2026-10-18'
review_by: '2027-04-19'
review_interval: Every six months, or when HHS finalizes Security Rule changes
index_interval: Six months
source_quality: secondary
counsel_review:
  status: approved
  date: '2026-10-19'
  scope: Whole file
covers: HIPAA Privacy, Security, and Breach Notification Rules (45 CFR Parts 160 and 164), as they apply to a covered entity or business associate
version: The rules as amended through the 2013 Omnibus Rule; the January 2025 Security Rule proposal is noted, not applied
sources: ecfr.gov (45 CFR Parts 160, 164); HHS OCR guidance on risk analysis and on HIPAA and FERPA
last_verified_note: 2026-10-18, against secondary sources (law-firm, regulator-guide, and tracker summaries); primary texts not yet read line by line. Reviewed and approved by counsel on 2026-10-19.
volatile_points: §1 (Security Rule proposal status); §2 (business associate status depends on the contract and the service)
---

# HIPAA

## Contents

1. Status
2. When HIPAA applies to the company
3. The security risk analysis (45 CFR § 164.308(a)(1))
4. Related duties the analysis feeds
5. How HIPAA meets FERPA and state law

---

## 1. Status

HHS proposed a substantial update to the Security Rule on January 6, 2025 (RIN 0945-AA22), including making most "addressable" specifications required, an asset inventory and network map, and annual compliance audits. As of October 2026 it isn't final; the Unified Agenda targets July 2027, and provider groups have asked HHS to withdraw it. The current Security Rule applies until a final rule takes effect. *Volatile:* check the Federal Register before treating any proposed change as law.

## 2. When HIPAA applies to the company

HIPAA binds **covered entities** (health plans, health care clearinghouses, and providers that transmit health information electronically in standard transactions) and their **business associates**: anyone who creates, receives, maintains, or transmits protected health information (PHI) for a covered entity (45 CFR § 160.103). A business associate needs a business associate agreement (§ 164.504(e)) and is directly liable under the Security Rule.

Record, per activity: the covered entity served, the service, whether the company handles PHI, and the business associate agreement's ID. A company that handles health data for its own users, outside a covered entity, isn't under HIPAA for that data, though state health privacy laws may apply (`us-state-privacy.md`).

## 3. The security risk analysis (45 CFR § 164.308(a)(1))

Required, not addressable. The analysis must be "accurate and thorough" and cover all electronic PHI the company creates, receives, maintains, or transmits. HHS guidance expects it to:

1. Define the scope: every system and location holding ePHI
2. Collect data on where ePHI is stored, received, maintained, or transmitted
3. Identify threats and vulnerabilities
4. Assess current security measures
5. Determine the likelihood of each threat
6. Determine its potential impact
7. Determine the level of risk
8. Document the results
9. Review and update it periodically, and when operations or technology change

Risk management (§ 164.308(a)(1)(ii)(B)) then implements measures that reduce the risks to a reasonable and appropriate level. Keep documentation for six years (§ 164.316(b)(2)).

## 4. Related duties the analysis feeds

- **Breach notification** (§§ 164.400–414): a business associate notifies the covered entity without unreasonable delay, and no later than 60 days after discovery. Route incidents to `incident-assessment`.
- **Minimum necessary** (§ 164.502(b)) for uses and disclosures.
- **Subcontractors** that handle PHI need their own business associate agreements (§ 164.502(e)(1)(ii)).

## 5. How HIPAA meets FERPA and state law

Education records under FERPA are excluded from the definition of PHI (45 CFR § 160.103), so a school's health records are usually governed by FERPA, not HIPAA (HHS and Department of Education joint guidance, November 2008). At colleges, treatment records used only for treatment fall outside FERPA's education records (34 CFR § 99.3), and become education records once disclosed for other purposes. Check which law governs each data set before applying either. Where both a state law and HIPAA apply, the more protective state provision generally isn't preempted. *Verify* per state.
