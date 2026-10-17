---
id: AIS-NNNN
type: ai-system
title: <System or agent name>
source: <in-house | built on vendor model | vendor product | embedded feature in vendor product>
status: Draft
lifecycle: <idea | pilot | live | retired>
version: 0.1
requesting_business_area: <business area>
system_owner: <team or person>
prepared_by: Claude (privacy-governance suite), for <privacy lead>
date_prepared: YYYY-MM-DD
next_review: YYYY-MM-DD
tier: <0 Stop | 1 High | 2 Elevated | 3 Standard> (provisional)
eu_ai_act_category: <prohibited? | high-risk (Annex III point …) | transparency | minimal> (provisional)
eu_ai_act_role: <provider | deployer | both> (provisional)
autonomy: <L0 suggest | L1 act with approval | L2 act within limits | L3 act broadly>
decisions_about_people: <none | informs | makes or materially influences>
personal_data: <none | personal | sensitive, student, or children's>
aiuc_1_mode: <readiness | benchmark>
aiuc_1_capabilities: [Universal]
follow_ons: <ai-impact-assessment, dpia screening, vendor-review, AUP>
required_fields_tbc: <count>
related: {vendor_review: <VR-…>, ropa: <ROPA-…>, assessments: [<AIIA-…>, <DPIA-…>]}
references:
  - eu-ai-act.md (as amended by Reg. (EU) 2026/1744), last verified 2026-10-16
  - aiuc-1.md (Oct 15, 2026 release), last verified 2026-10-16
---

# AI system: <name>

## Summary

> **Proposed tier:** <tier> (Provisional), because <deciding factor and fact>.
> **EU AI Act:** <category> (Provisional). Role: <role> (Provisional).
> **Follow-ons required:** <list, with skills>.
> **Use decision:** Not authorized by this intake. <For Tier 0: "Stop. Don't use this function until the privacy lead and counsel have decided.">

<Two or three sentences: what it does, for whom, with what data, and how much it acts on its own.>

> **Decision needed:** The privacy lead confirms the tier and classification. The business owner confirms the facts.

## 1. What it does

| Field | Value | Source |
|---|---|---|
| Inputs | | |
| Outputs (with a sample) | | |
| What happens to the output | | |
| Users | | |
| People the outputs are about | | |
| Decisions it informs or makes | | |
| Tools and permissions (agents) | | |
| Underlying model and provider | | |
| Status and dates | | |

## 2. Data

| Data | Personal? Sensitive, biometric, student, or children's? | Where from | Retained by whom, how long |
|---|---|---|---|

## 3. EU AI Act classification

| Check | Result | Status | Basis |
|---|---|---|---|
| AI system (Art. 3(1)) | | | |
| Roles | | Provisional | Art. 3(3)–(4), Art. 25 |
| Prohibited practices (Art. 5), each checked | | | |
| High-risk (Art. 6, Annex III) | | | |
| Art. 6(3) derogation, if relied on | | | |
| Transparency (Art. 50), each paragraph | | | |
| GPAI underneath | | | Arts. 51–55 |

Other regimes: <GDPR Art. 22 and profiling; CCPA ADMT; Colorado SB 26-189; employment AI laws; FERPA or COPPA>

## 4. Tiering

| Factor | Level | Fact behind it |
|---|---|---|
| Use under the EU AI Act | | |
| Decisions about people | | |
| People affected | | |
| Data | | |
| Autonomy | | |
| Reach and reversibility | | |
| Source | | |

**Tier:** <highest level>.

## 5. AIUC-1

| Field | Value |
|---|---|
| Mode | Readiness (own agent) or benchmark (vendor's agent) |
| Capability tags | |
| Mandatory requirements that apply | |
| Certification (vendor) | <product in scope, release, report date, or none> |

## 6. Top risks

<Three to six risks from risk-method.md §2a, one line each, with who is affected. Full analysis goes in the impact assessment.>

## 7. Follow-ons

| Follow-on | Why | Skill | Status |
|---|---|---|---|
| AI impact assessment | | `ai-impact-assessment` | Recommended |
| DPIA screening | | `dpia` | |
| Vendor review | | `vendor-review` | |
| AUP coverage | | `notice-and-policy` | |

## 7a. Containment record (if any control was applied)

| Field | Value |
|---|---|
| Control | |
| Owner and approver | |
| Requested and applied (date, time) | |
| Evidence | |
| Output no longer generated, shown, exported, or used downstream? | |
| Remaining access paths | |
| Condition for re-enabling | |

## 8. Open questions

| # | Question | Needed for | Owner |
|---|---|---|---|

## 9. Sign-off

| Decision | Approver role | Name | Date | Decision |
|---|---|---|---|---|
| Facts confirmed | Business owner (<area>) | | | |
| Tier and classification confirmed | Privacy lead | | | |
