# Program assessment rating guide

How to choose the Target Profile, rate the Current Profile, set the Implementation Tier, and rank the gaps. The framework's structure is in `nist-privacy-framework.md`, §2. The same method works for the NIST AI RMF and the ISO/IEC 42001 checklist.

## 1. Target Profile: which outcomes the program needs

For each subcategory, decide whether it belongs in the Target Profile and record **why**. Use these drivers, in order:

1. **Law:** a regime in scope requires it. The category map in `nist-privacy-framework.md`, §3 shows which laws each category serves. A subcategory driven by law is in the Target Profile unless the law doesn't apply to the company, which is a Provisional determination.
2. **Risk:** the company's registers show risks it would treat (DPIAs, AI impact assessments, incidents, vendor reviews).
3. **Commitments:** contracts, certifications pursued (AIUC-1, ISO/IEC 42001), customer expectations, and the company's own policies.
4. **Benefit:** good practice the company chooses to adopt.

A subcategory can be left out, with its reason. Not every outcome fits every organization, but an exclusion must rest on scope or relevance. It must never remove an inconvenient gap from the assessment.

**Applicability analysis is complete or it's Open.** For each law that drives the Target Profile, check every alternative threshold and scope rule: for example, TIPA's revenue floor together with either 175,000 consumers or 25,000 consumers with more than 50% of revenue from sales, and its exclusions; and GDPR territorial scope by establishment, targeting, and monitoring, not establishment alone (`gdpr.md`, §1a). Record what was checked. Tennessee's affirmative defense requires a program that "reasonably conforms" to the framework, so record the reasoning for each exclusion (`us-state-privacy.md`, §2).

## 2. Current Profile: what the evidence shows today

Rate each Target Profile subcategory on this scale. **The rating follows the evidence, not the policy.**

| Rating | Meaning | Evidence needed |
|---|---|---|
| **Achieved** | The outcome is met across the scope, and operating | Current operating evidence (records, test results), not only policies |
| **Largely achieved** | Met for most of the scope, or operating with minor exceptions | Operating evidence for the main systems; known exceptions listed |
| **Partly achieved** | Designed, but operating only in places, or with significant gaps | Policy or design evidence; partial operating evidence |
| **Not achieved** | Not in place, or no evidence it operates | — |
| **Not assessed** | No information yet | Record what's needed |

Give each rating a status (`conventions.md`, §7). A rating built on interviews alone is Provisional.

**Unseen reports cap the rating.** A report or certificate nobody has reviewed (a SOC 2 report, an ISO certificate, a vendor attestation) supports at most **Partly achieved**. Once reviewed, map it explicitly: the subcategory, the matching criterion or control, whether the audited system, process, and period cover the outcome, any exceptions or complementary user entity controls, and what privacy-specific evidence is still needed. A security report rarely shows a privacy outcome on its own.

**Missing evidence isn't proof of absence.** Use Not assessed when the status is unknown, and Not achieved only when the evidence shows the outcome isn't met.

**Record for each rating:** the evidence IDs, each item's owner, the date obtained and the period covered, the assessor's rationale, known limitations, and the reviewer. Link the evidence by ID: controls (`CTL`), evidence (`EV`), registers (`ROPA`, `AIS`), and assessments (`DPIA`, `VR`, `AIIA`, `INC`, `DSR`).

**Read the program's own records first.** The suite's registers are evidence: a current RoPA with few TBC fields supports ID.IM-P; DSR case files with deadlines met support CT.PO-P3; vendor reviews support ID.DE-P; DPIAs support ID.RA-P. Gaps in those records are findings too.

## 3. Implementation Tier

The Tier describes the organization's privacy risk management as a whole, on four attributes. Rate each attribute 1 to 4, with evidence:

| Attribute | 1 Partial | 2 Risk Informed | 3 Repeatable | 4 Adaptive |
|---|---|---|---|---|
| **Privacy risk management process** | Ad hoc, reactive | Approved by management but not organization-wide policy | Formal, approved policy, updated regularly | Adapts from lessons learned and predictive indicators |
| **Integrated privacy risk management program** | Limited awareness of privacy risk | Awareness, but not consistent across the organization | Organization-wide approach, consistently applied | Part of the culture; informs decisions throughout |
| **Data processing ecosystem relationships** | Little understanding of its role or of ecosystem risks | Understands its role, but doesn't act on ecosystem risk consistently | Understands its role and manages ecosystem risk under policy | Manages ecosystem risk actively and shares information |
| **Workforce** | Few people with privacy responsibilities; little training | Some trained staff; awareness uneven | Trained workforce with clear roles | Workforce adapts practices as risks and roles change |

The overall Tier is a judgment, not an average. Say which attribute holds it back. **Tiers describe the organization's privacy risk management as a whole.** Don't assign Tiers to individual functions or categories (not "Protect-P is Tier 3"), and don't derive the Tier from subcategory counts. Report category results as Current Profile ratings, and document the Tier reasoning separately. *Verify* the attribute wording against NIST CSWP 01162020, §3.2 before quoting it externally. Record the framework version checked, the date, and the source, so a later reader knows whether 1.1 had been finalized (`nist-privacy-framework.md`, §1).

## 4. Gaps and priority

A gap is a Target Profile subcategory not rated Achieved. Rank each one:

| Factor | High | Medium | Low |
|---|---|---|---|
| **Legal exposure** | A law in scope requires it now, or a deadline applies | Required soon, or by a law with uncertain application | Good practice only |
| **Risk to individuals** | Linked to High residual risks in the registers | Linked to Medium risks | No linked risk |
| **Dependency** | Other gaps can't close until this one does | Some dependents | None |
| **Effort** | Small (quick win) | Moderate | Large |

**Priority:** legal exposure and risk first, then dependency, then effort, so that quick wins come forward among gaps of equal weight. Record the reasoning in a line for each gap.

## 4a. Findings, not verdicts

A rating says how well an outcome is met. It isn't a finding that the company broke the law. Where the notes suggest a possible violation (late DSRs, a notice that omits a use, a launch without assessment), write a **finding pending evidence**: what was observed, what would confirm or dismiss it, and the check to run. For example, check each request against its own deadline and any lawful extension, rather than inferring from an average. Investigation, and containment where needed, is the roadmap's first phase.

## 5. Roadmap

Make the first 30 days an **investigation and containment** phase for any finding pending evidence. Then group the ranked gaps into quarters, respecting dependencies. For each item: the gap, the action, the owner, the quarter, the acceptance criterion, the evidence that will show it's closed, and the expected rating change. Separate **Legal** items (required by a law in force) from **Readiness** items (`conventions.md`, §7).

## 6. AI RMF and ISO/IEC 42001 variants

- **NIST AI RMF:** same method, with the 72 subcategories (`make_checklist.py ai-rmf profile`). The AI RMF has no Tiers of its own. Report maturity by function (GOVERN, MAP, MEASURE, MANAGE) using the Current Profile ratings.
- **ISO/IEC 42001:** a gap assessment against clauses 4 to 10 and Annex A (`make_checklist.py iso-42001 profile`). Clauses 4 to 10 are mandatory for certification. Annex A controls are selected through risk treatment, with exclusions justified in a Statement of Applicability. The checklist is a public paraphrase, so final conformity judgments need the licensed standard (`iso-42001.md`).
