---
title: Data subject request matrix
summary: Data subject request rights, deadlines, verification, exceptions
version_summary: As of 2026-10-16
last_verified: '2026-10-16'
review_by: '2027-01-16'
review_interval: Quarterly
index_interval: Quarterly
source_quality: primary
counsel_review:
  status: not-recorded
covers: Rights, deadlines, verification, exceptions, and response content for data subject and consumer requests under EU GDPR, UK GDPR, Swiss FADP, US comprehensive state privacy laws, FERPA, and COPPA
version: As of 2026-10-16
sources: '`gdpr.md`, `us-state-privacy.md`, `ferpa.md`; CCPA Regs. 11 CCR §§ 7020–7028, 7060–7063, 7101; EDPB Guidelines 01/2022 on the right of access (v2.0, March 28, 2023); secondary summaries of state deadlines (Osano, ComplyFine, Byte Back, retrieved 2026-10-16)'
verification_scope: CCPA timelines and state response and appeal windows checked against secondary sources. Appeal windows, Iowa's 90-day period, and free-request limits rest on secondary sources and carry verify flags. Read the statute before quoting a deadline to a requester.
volatile_points: §3 (state appeal windows; laws effective 2027–2028); UK "stop the clock" commencement
---

# Data subject request matrix

The `dsr-response` skill uses this file to decide which law applies, when the response is due, how to verify identity, and what the response must contain.

## Contents

1. Which law applies
2. Request types
3. Deadlines
4. Identity verification and agents
5. Exceptions and refusals
6. Response content
7. Fees, records, and metrics

---

## 1. Which law applies

Work out the company's role first, because it decides who answers.

| Company role for the data | What to do |
|---|---|
| **Controller or business** | The company responds, under each law that applies to the requester |
| **Processor or service provider** | Don't answer the substance. Forward the request to the customer (the controller) promptly, as the DPA requires, tell the requester it was forwarded where the DPA allows, and help the customer respond (GDPR Art. 28(3)(e); state processor duties). |
| **FERPA school official** | Requests from parents or eligible students go through the institution. Forward them, and help the institution meet its 45-day deadline. |

Then decide which laws apply to **this requester**:

- **GDPR, UK GDPR, FADP:** apply if the company's processing of this person's data falls within their territorial scope (`gdpr.md`, §1a). The requester's location helps, but doesn't decide it alone.
- **US states:** apply if the requester is a resident of a state whose law applies to the company (thresholds) and the data isn't exempt (`us-state-privacy.md`, §2 and §10). Employee, applicant, and B2B data are excluded in most states but covered in California. Check the state's exemption wording.
- **FERPA, COPPA:** see `ferpa.md`.
- **Several at once:** apply the strictest deadline and the broadest content that any applicable law requires, unless they conflict. Record each law's position. A response under one law doesn't automatically satisfy another: CCPA response content, look-back, and prohibited disclosures differ from Art. 15.
- **Residency is a legal concept.** Where the person is when they write doesn't decide it. Keep state-law applicability Open until residency, the company's thresholds, and any exemptions are checked.

If residency is unknown, ask, but don't hold up the acknowledgment. Where the answer could change the deadline, use the shortest plausible deadline until it's resolved.

---

## 2. Request types

| Request | GDPR, UK, FADP | US states | FERPA, COPPA |
|---|---|---|---|
| Access, confirmation, copy | Art. 15; FADP Art. 25 | Right to know, confirm, access, copy (all states). California: categories and specific pieces (Cal. Civ. Code §§ 1798.100, 1798.110) | FERPA inspect and review (34 CFR § 99.10); COPPA parental review (16 CFR § 312.6) |
| Deletion | Art. 17 | Right to delete (all states; Cal. Civ. Code § 1798.105) | COPPA parental deletion (§ 312.6) |
| Correction | Art. 16 | Right to correct (most states; Cal. Civ. Code § 1798.106) | FERPA amendment (§§ 99.20–99.22) |
| Portability | Art. 20 | Portable copy (most states) | — |
| Restriction | Art. 18 | — | — |
| Objection | Art. 21 (absolute for direct marketing) | — | — |
| Opt-out of sale, sharing, targeted advertising | Art. 21(2) for direct marketing | All states; California "Do Not Sell or Share" (§ 1798.120); universal opt-out signals | — |
| Opt-out of profiling for significant decisions | Art. 22 | Most states; California ADMT opt-out from Jan 1, 2027 | — |
| Limit use of sensitive data | — | California (§ 1798.121) | — |
| List of third parties | — | Oregon, Minnesota, and others (*verify per state*) | — |
| Question a profiling result | Art. 22(3) | Minnesota | — |
| Appeal of a refusal | Complaint to the supervisory authority | Appeal to the controller, then the attorney general (most states) | Complaint to SPPO |

---

## 3. Deadlines

Count from the date the request is received, not the date it's verified, unless the law says otherwise. Verifying identity doesn't pause the GDPR clock (the UK "stop the clock" provision is the exception, once commenced).

**Statutory deadlines and internal targets are different things.** Record both, and label them. An acknowledgment target of a few days is good practice, but under the GDPR it isn't a statutory deadline. Under the CCPA, the 10-business-day acknowledgment is. An extension is lawful only where complexity or volume makes it necessary. Lacking a DSR process or a RoPA doesn't justify one.

| Law | Acknowledge | Respond | Extension | Appeal |
|---|---|---|---|---|
| EU GDPR | — (good practice: promptly) | **One month** (Art. 12(3)) | Up to two further months for complex or numerous requests, notified within the first month with reasons | — |
| UK GDPR | — | One month | As GDPR. The clock may pause while waiting for information reasonably needed, such as identity or clarification (*verify commencement*) | — |
| Swiss FADP | — | **30 days** (Ordinance Art. 18) | Extendable with notice and reasons | — |
| California CCPA | **10 business days** (CCPA Regs. § 7021) | **45 calendar days** | One 45-day extension with notice and reasons | — |
| California opt-out of sale or sharing; limit sensitive data | — | **As soon as feasible, no later than 15 business days** (CCPA Regs. §§ 7026, 7027) | — | — |
| Most other states (Virginia model) | — | **45 days** | One 45-day extension with notice and reasons | **45 or 60 days** to decide the appeal, depending on the state. Virginia: 60 days. Colorado: 45 days, extendable by 60. Minnesota: 45 days, extendable by 60. (*verify per state*) |
| Iowa | — | **90 days** (*verify*) | 45 days (*verify*) | — |
| FERPA | — | **45 days** (34 CFR § 99.10(b)) | — | Hearing on amendment requests (§ 99.21) |

**Counting one month (GDPR):** the period ends on the same date in the following month. If that date doesn't exist (for example, January 31 to February), it ends on the last day of that month. If it ends on a weekend or public holiday, it moves to the next working day (EDPB Guidelines 01/2022, section on timing; *verify* the paragraph before citing it). Use `dsr-response/gov deadlines`, and check public holidays by hand.

> **Verify:** State appeal windows and Iowa's response period come from secondary sources. Check the statute for the requester's state before stating a deadline in a reply.

---

## 4. Identity verification and agents

Verify enough to protect the person, and no more.

- **GDPR:** authenticate through the existing account channel where it gives enough assurance. Where reasonable doubts remain, ask only for the information needed to resolve them (Art. 12(6)). Don't ask for unnecessary ID documents, and never by default. EDPB Guidelines 01/2022 treat a routine request for a copy of an ID card as disproportionate where other means work.
- **California** (CCPA Regs. §§ 7060–7062): use a reasonable method proportionate to the sensitivity of the data and the risk of harm. For categories of personal information, a **reasonable degree of certainty** (match at least two data points). For specific pieces, a **reasonably high degree of certainty** (match at least three data points, plus a signed declaration under penalty of perjury). Deletion: as for categories or pieces, depending on the data. Account holders can be verified through the account. Don't require someone to create an account.
- **Opt-outs** of sale, sharing, or targeted advertising generally **don't need identity verification**. Ask only for what's needed to apply the opt-out.
- **Authorized agents:** California (§ 7063), Colorado, Connecticut, and others allow an agent to submit requests. Ask for the person's signed permission, and you may verify the person directly.
- **Parents and guardians:** COPPA and FERPA requests come from parents, or from eligible students under FERPA. Verify the relationship proportionately.
- **Don't collect new data for verification beyond what's needed.** Delete data collected only for verification once the request is closed (CCPA Regs. § 7060(d)).

If verification fails, tell the person why and what they can do. For California, a deletion request that can't be verified is treated as an opt-out of sale or sharing where applicable (§ 7062(d); *verify*).

---

## 5. Exceptions and refusals

Refusing all or part of a request is a legal determination: record the provision, and route it to the privacy lead (`approvals.md`).

- **GDPR:** manifestly unfounded or excessive requests (Art. 12(5); the controller bears the burden); rights and freedoms of others (Art. 15(4)), such as redacting third parties in a copy; erasure exceptions (Art. 17(3)): legal obligation, legal claims, freedom of expression, public interest, archiving and research; restriction instead of erasure where accuracy is contested (Art. 18). Member state law restrictions (Art. 23), such as legal privilege.
- **UK:** the "reasonable and proportionate search" standard for access requests (UK GDPR Art. 15(1A)); legal professional privilege exemption.
- **California deletion exceptions** (Cal. Civ. Code § 1798.105(d)): complete the transaction, security, debugging, free speech, legal obligation, internal uses reasonably aligned with expectations, and others. Trade secrets aren't a reason to refuse access entirely.
- **Most states:** similar exceptions, plus pseudonymous data held separately with controls, and fraud prevention and security.
- **FERPA:** some records are excluded from "education records" (`ferpa.md`, §2).
- **Legal holds:** data under a litigation hold isn't deleted. Restrict it, and tell the person what you can.

Every refusal tells the person why, what they can do, and how to appeal or complain (GDPR Art. 12(4); state appeal duties).

---

## 6. Response content

**GDPR access (Art. 15):** confirmation; a copy of the personal data; and (a) purposes, (b) categories, (c) recipients, (d) retention period or criteria, (e) the rights to rectify, erase, restrict, and object, (f) the right to complain, (g) the source if not from the person, and (h) automated decision-making, including meaningful information about the logic, significance, and consequences. Transfer safeguards where data went to a third country (Art. 15(2)). The first copy is free.

**California request to know:** categories of personal information collected; categories of sources; business or commercial purposes; categories of third parties disclosed to; categories sold or shared and to whom; and specific pieces, as requested. The look-back covers data collected on or after January 1, 2022, unless that proves impossible or involves disproportionate effort (Cal. Civ. Code § 1798.130(a)(2)(B)). Never disclose Social Security, driver's license, or other government ID numbers, financial account numbers, health insurance or medical ID numbers, account passwords, security questions and answers, or unique biometric data in a response. Confirm that the business holds them instead (CCPA Regs. § 7024(d)).

**Other states:** confirmation, access to the personal data, and a portable copy where technically feasible.

**Deletion:** confirm what was deleted and where, including processors, which the company must direct to delete. Say what was kept, and under which exception.

**Correction:** say what changed, or why not.

**Notifying recipients (Art. 19):** tell each recipient to whom the data was actually disclosed about a rectification, erasure, or restriction, unless that proves impossible or involves disproportionate effort. Tell the person who they are, if asked. Identify them from the disclosure records, not by notifying every vendor by default.

---

## 7. Fees, records, and metrics

- **Fees:** free in nearly all cases. GDPR allows a reasonable fee for further copies or for manifestly unfounded or excessive requests (Arts. 12(5), 15(3)). Most states allow free requests up to twice a year (*verify per state*).
- **Records:** California requires records of requests and responses for at least 24 months (CCPA Regs. § 7101). Keep the same for every request, and keep only what's needed to show compliance.
- **Suppression after deletion:** keeping a minimal identifier (such as a hashed email) so a deleted person isn't re-added to marketing lists needs its own justification and retention period. Record both.
- **Metrics:** California businesses handling the personal information of 10 million or more consumers publish annual request metrics (CCPA Regs. § 7102).
