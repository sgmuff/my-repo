# Notice requirements checklist

What each kind of notice must say, by regime. Use it to compare a notice with the company's actual practice. Article-level detail is in `gdpr.md` (§4), `us-state-privacy.md` (§3), and `ferpa.md`. Items marked *verify* rest on summaries; check the text before relying on them in a published notice.

## 1. Privacy notice (website or app)

| Element | GDPR, UK, FADP | California (CCPA) | Other states | Practice source to check |
|---|---|---|---|---|
| Who the controller is; contact; DPO or representative | Arts. 13(1)(a)–(b), 14(1)(a)–(b), 27 | Contact for questions | Contact | Company profile |
| Categories of personal data | Art. 14(1)(d) | Categories collected in the past 12 months | Categories processed | RoPA §1.2 |
| Sources | Art. 14(2)(f) | Categories of sources | — | RoPA §3 |
| Purposes and lawful basis | Arts. 13(1)(c)–(d), 14(1)(c), 14(2)(b) | Business or commercial purposes | Purposes | RoPA §1.1 |
| Recipients or categories | Arts. 13(1)(e), 14(1)(e) | Categories of third parties disclosed to; sold or shared, and to whom | Categories shared with third parties; categories of third parties | RoPA §1.3; vendor reviews |
| Sale, sharing, targeted advertising | — | Whether sold or shared; "Do Not Sell or Share" link; Global Privacy Control | Disclosure and opt-out method | RoPA §4 |
| Sensitive data | Art. 9 conditions | Use of sensitive PI; "Limit" right where applicable | Consent or opt-out, by state | RoPA §1.2, §4 |
| Transfers outside the EEA, UK, or Switzerland | Arts. 13(1)(f), 14(1)(f) | — | — | RoPA §1.4 |
| Retention | Arts. 13(2)(a), 14(2)(a) | Retention period for each category (*verify*: Cal. Civ. Code § 1798.100(a)(3)) | — | RoPA §1.5 |
| Rights and how to exercise them, including appeals | Arts. 13(2)(b)–(d), 14(2)(c)–(e) | Each right, request methods (at least two for most businesses), verification process, authorized agents | Rights, how to exercise them, appeal process | `dsr-matrix.md` |
| Automated decisions and profiling | Arts. 13(2)(f), 14(2)(g) | ADMT pre-use notice from January 1, 2027 | Profiling opt-out | AI inventory |
| Children | Art. 8 | Minors' opt-in rules | Teen protections | — |
| Effective date and update history | Good practice | Date last updated (*verify*: at least every 12 months) | — | — |

## 2. Notice at collection

Where data is collected (a sign-up form, an in-product feature, a recording start), give the short notice the law requires at or before the moment of collection: the categories, the purposes, whether data is sold or shared, retention, and a link to the full notice (CCPA Regs. § 7012, *verify*). GDPR Art. 13 applies when data is obtained from the person. In-product AI features usually need a just-in-time notice.

## 3. AI-specific notices

- **Interacting with AI** (AI Act Art. 50(1); AIUC-1 E016): tell people they're dealing with an AI system, unless obvious. Check each chat or voice interface.
- **Synthetic content** (Art. 50(2), (4)): marking and disclosure.
- **High-risk decisions** (Art. 26(11); Art. 86): notice to people subject to decisions, and the right to an explanation.
- **Workers** (Art. 26(7)): notice before workplace use of high-risk AI.
- **US:** CCPA ADMT notices (from January 1, 2027); Colorado SB 26-189 disclosures (from January 1, 2027); NYC LL 144 candidate notices; Utah disclosure law (`us-state-privacy.md`, §9).

## 4. Other notices

- **Employee and applicant privacy notices:** GDPR Arts. 13 and 14 for EU and UK staff; CCPA notice at collection for California employees and applicants.
- **Financial incentive notice** (loyalty or discount programs tied to data): CCPA Regs. § 7016 (*verify*).
- **FERPA:** institutions publish the annual notification (34 CFR § 99.7). A school official vendor supports it, and must not describe uses the institution hasn't authorized.
- **COPPA:** an online notice and a direct notice to parents (16 CFR § 312.4), unless school authorization applies.

## 5. Comparing notice to practice

For each statement in the notice, find the practice record that supports it, and for each practice record, find the statement that covers it. Mismatches in either direction are findings:

- **Said but not done:** the notice promises something the practice doesn't deliver, such as "we never share data with advertisers" when a pixel does. This is the most serious kind, because it can be a deceptive practice (FTC Act § 5; state UDAP laws).
- **Done but not said:** practice the notice doesn't describe, such as a new AI feature, a new vendor category, or a new purpose.
- **Out of date:** retention periods, rights, contacts, or legal references that have changed.

Number each gap and give it **one primary kind** (the three above), noting a secondary kind where one practice causes two gaps (an ad tag can make a promise false and also be undisclosed).

### Facts behind each gap

Say what each gap rests on: a register entry reported by a business owner, or a technical check (tag manager export, network capture, configuration screenshot, contract). A register entry is "Stated by requester" until checked (`conventions.md`, §6). Ask for evidence with an owner and a date range: the current tag configuration plus its deployment history since the practice started, not only today's settings.

Check every surface where the notice appears (website, app, sign-up flow, app store listing). They often carry different versions.

### Questions to keep separate

Some findings bundle several legal questions. Keep them apart, each with its own status, so one answer doesn't stand in for another:

| Finding | Separate questions |
|---|---|
| Ad or analytics tags | Is the company covered (each threshold route, not only revenue; `us-state-privacy.md`)? Is the actual data flow a sale or sharing? Does it include children's or student data, which carry their own rules? A tag's presence alone doesn't answer any of these. |
| Children's data | Is the service directed to children, or does the company have actual knowledge? What does the parent notice say, how is consent verified, and how do withdrawal and deletion work? |
| AI and children's or student data | Separate inference, training or fine-tuning by the company, training by a vendor on the company's instructions, and vendor retention or own-purpose use. Ask what happens to data already used and to models already trained. |
| Call recording and transcription | The rules depend on the states involved, the parties, and the recording arrangement. One announcement isn't a universal fix; counsel approves a recording protocol (inbound and outbound, what happens if a caller declines, the vendor's use and retention). |
| School data (FERPA) | "School official" status depends on the school's direct control over use and maintenance of the records under the contract, not only on having a contract (`ferpa.md`). |
| International customers | The company's role for each data flow (controller or processor), whether it uses the data for its own purposes, and whether the customers' instructions cover the AI and support tools. |

Also ask what the company has already promised: school and customer contracts, earlier notices, parent consents. A change in practice may need a contract amendment, renewed consent, or notice to customers, and data collected under the old promise may need its own fix.

### Gap tracker

The review carries one row per gap:

| Gap | Kind | Evidence status | Legal status | Severity | Interim control | Decision needed (who) | Owner | Due | Closure evidence | Action status |
|---|---|---|---|---|---|---|---|---|---|---|

- **Evidence status:** confirmed, partly verified, or unverified.
- **Legal status:** likely noncompliant, possibly noncompliant, or for counsel. Provisional until counsel confirms.
- **Action status:** recommended, authorized, implemented, verified. A recommended pause is not a pause until the owner confirms it happened and someone checks it technically.

