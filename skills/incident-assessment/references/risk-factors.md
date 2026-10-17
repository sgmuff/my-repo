# Breach risk assessment factors

How to assess whether a breach must be notified, and to whom. The GDPR's thresholds are about **risk to individuals**. US state laws are about whether the data is **covered** and, where the state allows it, whether misuse is **reasonably likely**. The two analyses differ, so record both.

## GDPR, UK GDPR, FADP

The questions, in order:

1. **Is it a personal data breach?** A breach of security leading to accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data (GDPR Art. 4(12)). This includes availability breaches, such as ransomware encryption without exfiltration, and confidentiality breaches.
2. **When did the company become aware?** When it has a reasonable degree of certainty that a security incident has occurred that compromised personal data (EDPB Guidelines 9/2022). A short initial investigation to establish that is allowed. Record the timestamp and the reasoning, because the 72-hour clock runs from it. A processor's knowledge reaches the controller when the processor tells it, so the controller's clock starts then (*verify* against current EDPB guidance).
3. **Notify the authority?** Required unless the breach is **unlikely to result in a risk** to individuals (Art. 33(1)). Where it's unclear, notify. Phased notification is allowed (Art. 33(4)).
4. **Notify individuals?** Required if the breach is **likely to result in a high risk** (Art. 34(1)), unless an exception applies: the data was unintelligible (encrypted with an uncompromised key), subsequent measures removed the high risk, or individual notice would involve disproportionate effort (then a public communication) (Art. 34(3)).

**Factors** (EDPB Guidelines 9/2022 and 01/2021):

| Factor | Raises risk | Lowers risk |
|---|---|---|
| Type of breach | Confidentiality (exfiltration, disclosure); integrity changes that people rely on | Brief availability loss with backups |
| Nature and sensitivity | Special category, criminal, financial, credentials, ID numbers, location, children's or student data, communications content | Business contact data only |
| Volume | Many records or many data types per person | A few fields |
| Ease of identification | Directly identifying data | Pseudonymized data with the key secure |
| Severity of consequences | Identity theft, fraud, discrimination, physical harm, distress, reputational damage | Inconvenience |
| Special characteristics | Children, vulnerable people, employees in disputes | — |
| Number of people | Many | One or a few |
| Recipient | Unknown or malicious actor; data published | A trusted recipient who confirms deletion (for example, a misdirected email to a known business partner) |
| Mitigation | — | Encryption with the key safe; recall or confirmed deletion; credentials reset before use |

Write the assessment so a supervisory authority could read it: the facts, each factor, the conclusion (Provisional), and who decided. Art. 33(5) requires documenting **every** breach, notified or not.

## US states

For each state where affected people live:

1. **Is the data covered** by that state's definition (`us-breach-notification.md`, §1)? Name the elements.
2. **Was it a breach** under that statute: acquisition, or also access?
3. **Does a safe harbor apply?** Encryption with the key uncompromised; redaction.
4. **Does the state allow a risk-of-harm analysis, and does it support no notice?** Only where the state allows one, and only on a documented, reasonable investigation. Note when the determination must be in writing, kept, or sent to the AG.
5. **Who notifies?** Owner or licensee notifies people. A maintainer notifies the owner.
6. **Deadlines, regulators, credit bureaus, content, and method:** from §2 and §3, with `scripts/incident_clock.py` for the dates.

## Before concluding

- **Check the actual exposed data**, not a description of it: open the file, table, or bucket listing (or have security do it) and list the columns or fields. A conclusion that no state law is triggered depends on it.
- **The authority route is a legal determination for counsel.** Whether the one-stop shop applies depends on the controller's main establishment and the processing activity (EDPB guidance on the lead supervisory authority). Without it, the route depends on the affected countries and each authority's competence. In Germany, competence for private bodies sits with the state (Land) authorities. Don't assume a destination from where affected people live, and record counsel's written conclusion.

## Ransomware

- Report to law enforcement (in the US, the FBI or CISA) as counsel advises.
- Make no contact with the attackers and no payment except as coordinated by counsel and the incident responders, with the insurer involved. A ransom decision weighs sanctions (US Treasury OFAC advisories), law enforcement coordination, insurance terms, contractual duties, operational need, and the consequences of paying. A sanctions screen alone isn't enough.
- Treat a leak-site posting as confirmed exfiltration for the risk assessment.

## Children and students

- Offer identity protection designed for minors, such as credit file freezes for children, rather than adult credit monitoring.
- Special education information (IEP status or disability category) brings in IDEA confidentiality rules for the districts, and may be health or medical information under some state breach laws. Check what the field actually holds.

## Separate deadline tracks

Keep each obligation in its own track with its own owner, because one notice doesn't satisfy another. For example, for New York student data: the contractor notifies each district (8 NYCRR 121.10(a), 7 days outside limit); the district reports to the NYSED Chief Privacy Officer; the district notifies parents and eligible students; and the contractor may have to reimburse notification costs. Federal items (SEC materiality, CIRCIA) stay conditional until counsel confirms they apply. Evaluate SEC materiality on its own track, without waiting for forensics to finish.

## Contracts and other recipients

Contracts often set the shortest deadlines. Check:

- Customer DPAs, if the company is a processor: notice to the controller "without undue delay," often with a fixed number of hours (24, 48, or 72)
- District and university agreements: often 48 to 72 hours, or New York's 7 days
- Cyber insurance: notice conditions, panel counsel and forensics requirements, and consent before incurring costs. Late notice can void coverage.
- Card brands and acquirers, where payment card data is involved (PCI DSS)
- Law enforcement: whether to report, and whether they ask for a delay (record any delay request in writing)

## AI incidents

- **EU AI Act Art. 73:** providers of high-risk AI systems report serious incidents to the market surveillance authority: within 15 days of awareness; 2 days for a widespread infringement or serious disruption of critical infrastructure; 10 days for a death. Deployers tell the provider immediately (Art. 26(5)). For Annex III systems these duties apply from **December 2, 2027** (`eu-ai-act.md`, §2). Commission guidance and a reporting template were in draft as of September 2025 (*verify* final status).
- **AIUC-1 E001–E003:** failure plans for AI security and privacy breaches, harmful outputs, and damaging hallucinations. Follow the company's plan if it holds or pursues certification, and record the incident for the next audit.
- An AI incident can also be a personal data breach (for example, an agent leaking one customer's data to another). Run both analyses.
