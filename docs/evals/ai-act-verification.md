# Verification sheet for the AI Act answer keys (key_version 6)

Prepared 2026-10-21 for counsel's sign-off on the `check: true` items in `ai-act-answer-keys.yaml`. Claude gathered the
text; counsel verifies. AI Act text is from the Commission's AI Act Service Desk, which reproduces the EUR-Lex consolidated
version as at 27 July 2026 and labels Digital Omnibus changes (Regulation (EU) 2026/1744, OJ L 24.7.2026) as AMENDED or
NEW. The Service Desk text is non-binding; EUR-Lex controls. Quotes are verbatim fragments.

Status per item: **supported** (source text matches the key), **qualify** (key needs an edit), **open** (no primary source found).

## Source checks for key_version 5 (2026-10-21)

Each row: the proposition checked, the primary source and pinpoint, the text's date, the result, and what's left.
VERIFIED means the text and its temporal application both support the key.

### aip-04 K2: emotion recognition and stress. DECIDED (option 3, key_version 6)
- **Proposition (counsel-reviewed):** "Frustration is an emotion; stress alone can describe a physical state rather than an
  emotion, so the answer establishes what the tool infers."
- **Source:** Commission Guidelines on prohibited AI practices, C(2025) 5052 final, 29 July 2025 (the final, adopted text;
  C(2025) 884 of 4 February 2025 only approved the draft). The English final isn't on the Commission's page; checked
  against the French final (an official language version) and the English draft, which match on these paragraphs.
  - Para 249: emotions don't include "physical states, such as pain or fatigue" (Recital 18); detecting a pilot's or
    driver's fatigue to prevent accidents isn't emotion recognition; inferring that an employee is "unhappy, sad or angry
    towards customers" is.
  - Para 257: the medical-or-safety exception "does not comprise the use of emotion recognition systems to detect general
    aspects of wellbeing. The general monitoring of stress levels at the workplace is not permitted under health or safety
    aspects." Burnout or depression detection at work stays prohibited.
  - Para 263, example: an employer may not deploy AI "destinés à mesurer l'anxiété en mesurant les niveaux de stress" of
    employees unless the high stress poses a specific danger (a safety case).
- **Result:** the statutory definitions (Art. 3(39), Recital 18) are VERIFIED and support testing what the tool infers. But
  the guidelines treat workplace stress monitoring as emotion recognition (anxiety) caught by Art. 5(1)(f), with only a
  safety exception, not as a physical state. The guidelines are non-binding; the CJEU has the final word.
- **Question for counsel:** for scoring, is a stress score inferred from voice at work:
  1. potentially a physical state, as the key says, so the answer must establish what the tool infers; or
  2. presumptively emotion recognition under the Commission's reading (paras 257, 263), so an answer that says so is fully
     correct and one that calls stress a physical state without engaging the guidelines is imprecise; or
  3. either, credited if reasoned?
  The scenario's tool also scores frustration, an emotion on any reading, so the prohibition outcome doesn't change; only
  K2's credit does.

### aid-04 K4: French and Polish employment law. VERIFIED (substance), with one residual
- **France, Code du travail** (code.travail.gouv.fr, the Ministry of Labour's official edition; Légifrance refused
  automated access):
  - L1222-4 (version of 1 May 2008): no personal information about an employee may be collected by a device "qui n'a pas
    été porté préalablement à sa connaissance".
  - L2312-38 (version of 1 January 2018): the CSE "est informé et consulté, préalablement à la décision de mise en œuvre
    dans l'entreprise, sur les moyens ou les techniques permettant un contrôle de l'activité des salariés"; it is also
    informed beforehand about automated personnel-management processing.
  - L2312-8 II 4°: the CSE is informed and consulted on "l'introduction de nouvelles technologies".
- **Poland, Kodeks pracy** (Sejm unified text, Dz. U. 2025 poz. 277 as amended to 2026, text dated 2026-08-18):
  - Art. 22^2 §6-7: purposes, scope and method of monitoring set in the collective agreement, work rules or a notice;
    employees told "nie później niż 2 tygodnie przed jego uruchomieniem".
  - Art. 22^3 §4: §1-3, and so §6-10 of Art. 22^2, apply to other forms of monitoring where needed for the organisation
    of work and proper use of work tools.
- **Poland, Act of 7 April 2006 on informing and consulting employees** (Dz. U. 2006 Nr 79 poz. 550, amended to
  Dz. U. 2026 poz. 1340; unified text dated 2026-10-20): it exists and is in force. Art. 1(2): applies to employers with
  at least 50 employees. Art. 13(1)(3): the employer informs the works council of "działań, które mogą powodować istotne
  zmiany w organizacji pracy".
- **Result:** the key's propositions are supported; the 2006 Act citation is correct and relevant where there are 50 or
  more employees and a works council. Point wording unchanged; citations corrected.
- **Residual:** the CSE's consultation powers depend on headcount (the 50-employee threshold for the full powers) and
  weren't checked; Polish union consultation on work rules (Kodeks pracy Art. 104^2) wasn't checked. Neither affects the
  key as worded.

### aid-01 K7: GDPR Art. 22, SCHUFA and CCD2. VERIFIED
- **Directive (EU) 2023/2225** (OJ L, 2023/2225, 30.10.2023; Publications Office text):
  - Art. 18(8): where the creditworthiness assessment "involves the use of automated processing of personal data", the
    consumer may request and obtain from the creditor human intervention: an explanation of the assessment, including the
    logic and risks of the automated processing; the chance to express a view; and a review of the assessment and the
    credit decision. Consumers must be told of the right.
  - Art. 48(1): Member States adopt measures "by 20 November 2025" and "shall apply those measures from 20 November 2026".
- **CJEU C-634/21 SCHUFA Holding (Scoring), 7 December 2023**, operative part: an automated probability value about a
  person's ability to pay is "automated individual decision-making" under GDPR Art. 22(1) "where a third party, to which
  that probability value is transmitted, draws strongly on that probability value to establish, implement or terminate a
  contractual relationship".
- **Result:** VERIFIED. K7 reworded (an `# added` point) to state the holding precisely and keep the three regimes apart.
- **Residual:** the duties fall on each creditor (the lender and each bank) and only for credit agreements within the
  Directive's scope (Art. 2 exclusions not checked); national transposition varies.

### Other items
- **aid-02 K8 (Art. 111(2)), aip-03 K4 (Art. 25(3)), aid-03 K4 (Art. 50(1)):** text VERIFIED earlier in this sheet;
  `check` removed. Application stays fact-dependent per counsel's dispositions.
- **aip-02 K2 (Arts. 6(4), 49(2)):** text VERIFIED; OPEN on the date from which Arts. 6(4) and 49(2) apply to a system the
  provider concludes isn't high-risk. Both sit in Chapter III (Art. 6 in Section 1, Art. 49 in Section 5), and Art. 113(c)(i)
  as amended sets 2 December 2027 for Chapter III as it applies to Art. 6(2) and Annex III systems; whether that date
  governs a system concluded not to be high-risk under Art. 6(3) wasn't confirmed. Doesn't affect the sealed scenarios,
  which don't turn on the date.

### Sources for these checks
- Guidelines: https://digital-strategy.ec.europa.eu/en/library/guidelines-prohibited-ai-practices (French final:
  https://ec.europa.eu/newsroom/dae/redirection/document/118657; English draft annex:
  https://ec.europa.eu/newsroom/dae/redirection/document/112367)
- Code du travail: https://code.travail.gouv.fr/code-du-travail/l1222-4, /l2312-38, /l2312-8
- Kodeks pracy: https://eli.gov.pl/api/acts/DU/2025/277/text/U/D20250277Lj.pdf
- 2006 Act: https://eli.gov.pl/api/acts/DU/2006/550/text/U/D20060550Lj.pdf
- CCD2: https://publications.europa.eu/resource/celex/32023L2225
- SCHUFA: https://publications.europa.eu/resource/celex/62021CJ0634

## Earlier checks (key_version 3 and 4)

## Critical

### aid-02 K8: Art. 111(2) (AMENDED)
> "...this Regulation shall apply to operators of high-risk AI systems, other than the systems referred to in paragraph 1 of
> this Article, that have been placed on the market or put into service before the date of application of Chapter III
> referred to in Article 113, only if, as from that date, those systems are subject to significant changes in their designs.
> In any case, the providers and deployers of high-risk AI systems intended to be used by public authorities shall take the
> necessary steps to comply with the requirements and obligations laid down in this Regulation by 2 August 2030."

Art. 113(c)(i) (AMENDED): Chapter III for Art. 6(2) and Annex III systems applies from 2 December 2027.

**Status: text supported; application fact-dependent.** Counsel's disposition (2026-10-21): placing on the market and
putting into service are alternative triggers, not the same event. If the vendor placed the system on the EU market before
the Chapter III date, that may satisfy the condition whenever the council first uses it; the council's first use matters
to putting into service but isn't needed if the system was already on the market. A qualifying legacy system is caught
from that date by a significant design change, and for public-authority use the 2 August 2030 longstop also applies.
Art. 111(2) doesn't postpone every obligation to 2030. The council deploying now doesn't by itself make the system a
legacy system: the answer establishes the market history, first-use date and intended purpose, or names the gap. Key K8
updated to match. (Claude's earlier proposed reading, which tied the legacy test to the council's go-live, is withdrawn.)

## High

### aip-02 K2: Arts. 6(3), 6(4), 49(2) (not amended)
> Art. 6(4): "A provider who considers that an AI system referred to in Annex III is not high-risk shall document its
> assessment before that system is placed on the market or put into service. Such provider shall be subject to the
> registration obligation set out in Article 49(2)."
> Art. 49(2): "Before placing on the market or putting into service an AI system for which the provider has concluded that
> it is not high-risk according to Article 6(3) that provider ... shall register themselves and that system in the EU
> database referred to in Article 71"

**Status: supported.** The key can drop "where the registration rules require it": Art. 49(2) registration is unconditional
for an Annex III system the provider concludes isn't high-risk under Art. 6(3). Neither duty applies to a system outside
Annex III altogether.

### aip-03 K4: Art. 25(3) (amendment label ambiguous on the Service Desk page)
> "In the case of high-risk AI systems that are safety components of products covered by the Union harmonisation
> legislation listed in Section A of Annex I, the product manufacturer shall be considered to be the provider of the
> high-risk AI system, and shall be subject to the obligations under Article 16 under either of the following
> circumstances: (a) ... placed on the market together with the product under the name or trademark of the product
> manufacturer; (b) ... put into service under the name or trademark of the product manufacturer after the product has
> been placed on the market."

Art. 3(14) (AMENDED): a component "fulfils a safety function where its intended purpose is to prevent or mitigate risks to
health and safety of persons or property".

**Status: supported**, with the amended Art. 3(14) also supporting aip-03 K1 (intended purpose test). Who the "product
manufacturer" is for a lift (the installer under Directive 2014/33/EU) is a Lifts Directive question: **open** for counsel.

### aip-04 K2: Arts. 3(34), 3(39), 5(1)(f) and the Commission guidelines
> Art. 3(39): "an AI system for the purpose of identifying or inferring emotions or intentions of natural persons on the
> basis of their biometric data"
> Art. 3(34): "personal data resulting from specific technical processing relating to the physical, physiological or
> behavioural characteristics of a natural person"
> Art. 5(1)(f) (not amended): "...the use of AI systems to infer emotions of a natural person in the areas of workplace and
> education institutions, except where the use of the AI system is intended to be put in place or into the market for
> medical or safety reasons"

Commission Guidelines on prohibited AI practices (February 2025), as summarised by law-firm commentary: physical states
such as pain or fatigue are outside the definition (Recital 18); the medical-or-safety exception doesn't cover general
wellbeing, such as burnout or depression detection at work. Primary text not retrieved.

**Status: supported** on the Act's text; **open** on the guidelines' exact wording and paragraph numbers. Note for the
key: "stress" sits near the line, since the guidelines treat wellbeing detection as still prohibited.

### aid-03 K4: Art. 50(1) (not amended)
> "Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in
> such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is
> obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect..."

**Status: supported.** The duty is the provider's. Art. 50 applies from 2 August 2026 (Art. 113, general date).

### aid-04 K4: French and Polish employment law
France (CNIL guidance and commentary; Légifrance text not retrieved): L1222-4, employees informed of a monitoring device
before it is introduced; L2312-38, CSE informed and consulted before a decision to use means or techniques to monitor
employees' activity; L2312-8, CSE consulted on introducing new technologies affecting working conditions, which a 2026
court decision applied to AI tools.
Poland (commentary; ISAP text not retrieved): Labour Code Arts. 22(2)-22(3), monitoring purposes, scope and method set in
workplace rules or notice, employees informed at least two weeks before monitoring starts; video monitoring may not be
used to assess performance. The 2006 Act on informing and consulting employees: no source found.

**Status: supported in substance by secondary sources; open** until counsel checks Légifrance and ISAP. The Polish 2006
Act citation is unconfirmed.

## Medium

### aid-01 K7: GDPR Art. 22, SCHUFA, Consumer Credit Directive
Directive (EU) 2023/2225 Art. 18 (text via a secondary site): the consumer may request human intervention where the
creditworthiness assessment involves automated processing, including an explanation, the chance to express a view and a
review. The Directive applies from 20 November 2026 (Commission page); several Member States haven't transposed it.
CJEU C-634/21 (7 December 2023): not re-checked.

**Status: supported in substance; open** on the EUR-Lex text and transposition.

## Counsel's dispositions (2026-10-21, updated for key_version 5)

| Item | Disposition | Effect on scoring |
| --- | --- | --- |
| aid-02 K8 | Interpretation reviewed; application fact-dependent | Score the two-part analysis and whether the answer establishes or flags market history |
| aip-02 K2 | Textual correction accepted, subject to confirming the full registration provision | Score as written |
| aip-03 K4 | Textual finding accepted; product-manufacturer role remains a fact question | Credit identifying the role question; don't require a named entity |
| aid-03 K4 | Provider-duty clarification accepted, subject to Art. 50(1)'s conditions and exceptions | Score as written |
| aip-04 K2 | Decided 2026-10-21 (option 3, on counsel's instruction): the stress question is contested | Credit either reading if reasoned; full credit for engaging with Recital 18 and the guidelines (paras 257, 263) |
| aid-04 K4 | Verified against primary texts (key_version 5) | Score substance; don't penalise a different or missing citation |
| aid-01 K7 | Verified (Directive (EU) 2023/2225 Arts. 18(8), 48(1); C-634/21) | Score as written |

## Related text confirmed (no check flag)

- Art. 113 (AMENDED): Chapters I and II from 2 February 2025; new Art. 5(1)(ba), (bb) from 2 December 2026; Annex III
  high-risk from 2 December 2027; Annex I from 2 August 2028; general date 2 August 2026.
- Art. 111(4) (NEW): providers of generative systems placed on the market before 2 August 2026 comply with Art. 50(2) by
  2 December 2026.
- Art. 50(2) exception (not amended): doesn't apply "to the extent the AI systems perform an assistive function for
  standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof".
- Art. 27(1): bodies governed by public law, private entities providing public services, and deployers of Annex III
  points 5(b) and (c); excludes point 2. Art. 27(3): notify the market surveillance authority of results.
- Art. 26(7), (8), (9), (11) and Art. 49(3): as cited in the keys.
- Art. 43(2) internal control for Annex III points 2-8; Art. 43(3) (AMENDED) Annex I Section A products follow the sectoral
  procedure, with notified bodies empowered to assess Section 2 requirements; Art. 43(4) pre-determined changes aren't a
  substantial modification.
- Annex III points 1(c), 3(a)-(d), 4(a)-(b), 5(a)-(c): as cited.

## Sources
- AI Act Service Desk, consolidated text as at 27 July 2026: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-111
  (and article-3, -5, -6, -25, -26, -27, -43, -49, -50, -113, annex-3)
- Regulation (EU) 2026/1744: https://eur-lex.europa.eu/eli/reg/2026/1744/oj?locale=en
- Emotion recognition guidelines commentary: https://fpf.org/blog/red-lines-under-eu-ai-act-unpacking-the-prohibition-of-emotion-recognition-in-the-workplace-and-education-institutions/ ;
  https://www.lewissilkin.com/insights/2025/02/17/understanding-the-eu-ai-acts-prohibited-practices-key-workplace-and-advertising-102k011
- France: https://cnil.fr/fr/controle-de-lactivite-des-personnes-employees ;
  https://cms.law/en/fra/legal-updates/l-ia-suspendue-le-juge-exige-la-consultation-du-cse-avant-tout-deploiement
- Poland: https://leglobal.law/2018/06/26/rules-of-monitoring-at-workplaces-introduced-in-the-polish-labour-code/ ;
  https://apps.eurofound.europa.eu/legislationdb/employee-monitoring-and-surveillance/poland
- CCD2: https://lawplayer.com/eu/article/32023L2225/art_18 ;
  https://www.dudkowiak.com/fintech-in-poland/gdpr-and-the-eu-consumer-credit-directive-ccd2/
