# Verification sheet for the router answer keys (key_version 0)

Prepared 2026-10-22 for counsel's sign-off on the `check: true` items in `router-answer-keys.yaml`. Claude gathered the
text; counsel verifies. Quotes are verbatim fragments from the source named; translations are Claude's. The keys are
unchanged until counsel signs off on the proposed edits below.

Status per item: **supported**, **qualify** (the key holds but needs an edit), **open** (no primary text retrieved;
the California legislature's site and Justia refused automated access, as Légifrance did for the DPIA keys).

| Item | Status | Proposed change |
|---|---|---|
| rtr-01 K1 | qualify | The vacatur reached only unauthenticated pages; booking pages behind login stay within the guidance |
| rtr-01 K2 | supported | Pinpoint 16 CFR § 318.1(a), 318.2 |
| rtr-01 K3 | supported | Pinpoint RCW 19.373.030(1) |
| rtr-01 K4 | qualify | Add SB 690 (2026): ends private suits under Penal Code § 638.51 for web tracking from 2027, not § 631 |
| rtr-02 K2 | supported | Pinpoint 740 ILCS 14/10, 14/15(a)-(b), 14/20 |
| rtr-02 K3 | open | ELVIS Act text from secondary sources only |
| rtr-02 K4 | open | Cal. Bus. & Prof. Code § 17941 not retrieved; its scope is narrower than the key implies |
| rtr-03 K2 | qualify | Add BIPA's exclusion for government agencies and their contractors (§§ 10, 25(e)) |
| rtr-03 K4 | qualify | The 2021 decisions allowed video-supervised exams in interim proceedings; drop "works council" for students |
| rtr-04 K1 | qualify | The Online Safety Act reaches an AI chat only through user-to-user or search features (Ofcom, 8 November 2024) |
| rtr-04 K2 | supported | Pinpoint the § 312.2 "directed to children" factors and the mixed-audience rule |
| rtr-04 K3 | qualify | SB 243 from secondary sources; note its video-game exclusion and the March 2026 Ninth Circuit ruling |
| rtr-05 K2 | supported | Pinpoint WOR art. 27(1)(k)-(l) and Code du travail L2312-38, third paragraph |
| rtr-05 K4 | qualify | § 2511(2)(c) covers persons acting under color of law; an employer relies on (2)(d), and stored messages fall under the SCA |
| rtr-06 K2 | supported | Cite the FTC's 2014 Facebook and WhatsApp letter |

## rtr-01: telehealth pixels

- **K1. QUALIFY.** *American Hospital Association v. Becerra*, No. 4:23-cv-01110-P (N.D. Tex. June 20, 2024), vacated the
  HHS bulletin only as to the "proscribed combination": an IP address linked to a visit to an **unauthenticated** public
  page about specific conditions or providers. The rest of the bulletin stands, including tracking on authenticated
  pages such as patient portals and booking flows (secondary sources: Morrison Foerster, Hunton; the HHS page refused
  automated access). The scenario's pages are authenticated, so K1 holds. **Edit:** source "HHS OCR bulletin on online
  tracking technologies (revised March 2024), as vacated only for unauthenticated pages in AHA v. Becerra (N.D. Tex.
  June 20, 2024)."
- **K2. SUPPORTED.** 16 CFR § 318.1(a), eCFR as of October 2026: the rule "does not apply to HIPAA-covered entities, or
  to any other entity to the extent that it engages in activities as a business associate." § 318.2: a breach of
  security "includes an unauthorized acquisition ... that occurs as a result of a data breach or an unauthorized
  disclosure," and "health care services or supplies" includes any website or app that tracks diseases or conditions
  (2024 amendments). **Edit:** source "16 CFR §§ 318.1(a), 318.2 (as amended 2024); FTC v. GoodRx (2023)."
- **K3. SUPPORTED.** RCW 19.373.030(1)(a)(i): collection needs "consent from the consumer for such collection for a
  specified purpose"; (1)(b)(i): sharing needs consent "separate and distinct from the consent obtained" to collect;
  (1)(c): consent comes "prior to the collection or sharing." **Edit:** pinpoint RCW 19.373.030(1).
- **K4. QUALIFY.** SB 690 (2026) was signed on September 30, 2026, after amendments on July 1-2 dropped its broad
  "commercial business purpose" exemption. As enacted, it ends the private right of action under Penal Code § 638.51
  (pen register and trap and trace) for tracking on websites and apps, operative January 1, 2027, and leaves § 631
  wiretap claims in place (secondary sources only: Baker Donelson, CDF; the enrolled text wasn't retrieved). The key's
  "issue for counsel rather than a settled rule" is right. **Edit:** source adds "SB 690 (2026), operative January 1,
  2027, which ends private § 638.51 claims for web tracking but not § 631 claims."

## rtr-02: voice cloning

- **K2. SUPPORTED.** 740 ILCS 14/10: "Biometric identifier" means "a retina or iris scan, fingerprint, voiceprint, or
  scan of hand or face geometry." § 15(a): a written, public retention and destruction policy, destroying data when the
  purpose is met or within 3 years of the last interaction. § 15(b): before collection, written notice of the
  collection, its specific purpose, and length of term, and "a written release," which in employment may be "a release
  executed by an employee as a condition of employment" (§ 10). § 20(b), as amended in 2024: repeated collection of the
  same identifier by the same method is a single violation. **Edit:** source "740 ILCS 14/10, 14/15(a)-(b), 14/20."
  The employment-release definition is worth an answer noting: BIPA accepts a condition-of-employment release, which
  the GDPR wouldn't treat as freely given.
- **K3. OPEN.** Tennessee ELVIS Act (Public Chapter 588 of 2024, effective July 1, 2024, amending Tenn. Code
  § 47-25-1101 et seq.): secondary sources (Latham, Manatt) agree that "voice" covers a sound readily identifiable and
  attributable to a particular individual, real or simulated, and that liability reaches tools whose primary purpose is
  reproducing a person's voice without authorization. The official text wasn't retrieved. The point stands as written;
  counsel to confirm the section.
- **K4. OPEN.** Cal. Bus. & Prof. Code § 17941 (the B.O.T. Act) wasn't retrieved. From Claude's knowledge, it makes it
  unlawful to use a bot to communicate online with a person in California "with the intent to mislead" about its
  artificial identity to incentivize a purchase or sale or to influence a vote, with disclosure as a safe harbor. A
  support bot on a phone line may fall outside it (phone, not online; service, not sales). **Proposed edit:** point
  reads "... and state bot disclosure laws, such as California's, whose scope (online communication meant to drive a
  sale or influence a vote) the answer should test rather than assume." AI Act Art. 50(1) is unaffected.

## rtr-03: university proctoring

- **K2. QUALIFY.** BIPA § 10: "A private entity does not include a State or local government agency." § 25(e):
  "Nothing in this Act shall be construed to apply to a contractor, subcontractor, or agent of a State agency or local
  unit of government when working for that State agency or local unit of government." The scenario doesn't say whether
  the university is public. If it is, the company working for it may be outside BIPA; if private, § 15(a)-(b) applies
  in full. **Edit:** point adds "and asks whether the university is public, since BIPA excludes government agencies
  and their contractors when working for them (§§ 10, 25(e))."
- **K4. QUALIFY.** OVG Nordrhein-Westfalen, order of 4 March 2021, 14 B 278/21.NE, and OVG Schleswig-Holstein, order of
  the same date, 3 MR 7/21, both refused interim relief against video-supervised online exams, relying on equal
  opportunity, the necessity of supervision, and deletion safeguards, and left the GDPR question to the main
  proceedings (secondary sources: LTO, Forschung & Lehre; the official text wasn't retrieved). The decisions concern
  video supervision by a person, not AI flagging of behavior, which raises the stakes. Students aren't employees, so a
  works council is relevant only to staff invigilators. **Edit:** source "OVG NRW, 4 March 2021, 14 B 278/21.NE; OVG
  Schleswig-Holstein, 4 March 2021, 3 MR 7/21; state DPA guidance"; point: "Flags German courts' interim acceptance of
  video-supervised exams with safeguards, that automated behavior flagging goes further, and whether a less intrusive
  option exists." Remove "works council" from the outcome text.

## rtr-04: children's game chat

- **K1. QUALIFY.** ICO Age Appropriate Design Code: 15 standards, including "Data protection impact assessments,"
  "Default settings" (high privacy by default), and "Nudge techniques," for information society services likely to be
  accessed by children (ICO code page). Online Safety Act: Ofcom's open letter of 8 November 2024 says generative AI
  chatbots are user-to-user services where users can share chatbot-generated content with other users, and search
  services where they search multiple sites; children's risk assessments were due 24 July 2025 and the Protection of
  Children Codes took effect 25 July 2025. A one-to-one companion with no sharing may fall outside the Act. **Edit:**
  point: "... and the Online Safety Act duties where the chat lets players share content or is part of a user-to-user
  service with child users (Ofcom open letter, 8 November 2024)."
- **K2. SUPPORTED.** 16 CFR § 312.2 (eCFR, October 2026): "directed to children" weighs subject matter, visual content,
  animated characters, child-oriented activities, and "competent and reliable empirical evidence regarding audience
  composition"; a mixed-audience service "shall not be deemed directed to children with regard to any visitor not
  identified as under 13." An age gate at 13 doesn't settle it. **Edit:** source "16 CFR § 312.2 (directed to children;
  mixed audience), as amended 2025."
- **K3. QUALIFY.** SB 243 (2025), effective January 1, 2026: disclosure that a companion chatbot is AI where a
  reasonable person could be misled, extra duties for users the operator knows are minors (break reminders every three
  hours, sexual content limits), suicide and self-harm protocols, and a private right of action (secondary sources:
  Skadden, FPF; the enrolled text wasn't retrieved). It excludes bots used only for customer service and, per FPF, bots
  within a video game limited to game topics that can't discuss mental health, self-harm, or sexual content; a game
  companion that chats freely is likely in scope. *NetChoice v. Bonta*, No. 25-2366 (9th Cir. March 12, 2026), narrowed
  the injunction against the California AADC: the harmful-material mitigation duty and the data-use and dark-patterns
  provisions stay enjoined, but the age estimation provision was un-enjoined and returned to the district court.
  **Edit:** point: "... SB 243, including whether its video-game exclusion applies to a free-ranging companion, and the
  AADC's status after NetChoice v. Bonta (9th Cir. March 12, 2026), with age estimation no longer enjoined."

## rtr-05: Slack sentiment

- **K2. SUPPORTED.** Wet op de ondernemingsraden art. 27(1) (version in force since 18 February 2023): the works
  council's consent is needed for (k) "een regeling omtrent het verwerken van alsmede de bescherming van de
  persoonsgegevens" of workers and (l) "voorzieningen die gericht zijn op of geschikt zijn voor waarneming van of
  controle op aanwezigheid, gedrag of prestaties." Code du travail L2312-38, third paragraph (official site): "Le
  comité est informé et consulté, préalablement à la décision de mise en œuvre dans l'entreprise, sur les moyens ou les
  techniques permettant un contrôle de l'activité des salariés." **Edit:** source "WOR art. 27(1)(k)-(l); Code du
  travail L2312-38, third paragraph."
- **K4. QUALIFY.** 18 U.S.C. § 2511(2)(c) protects interception "by a person acting under color of law"; a private
  employer relies on § 2511(2)(d) (a party, or one party's prior consent, unless for a criminal or tortious purpose).
  Slack messages are stored, so the Stored Communications Act (18 U.S.C. § 2701(c)(1), the provider's own access)
  matters more than interception, and Texas is a one-party consent state (Penal Code § 16.02; not retrieved). **Edit:**
  source "18 U.S.C. §§ 2511(2)(d), 2701(c); Tex. Penal Code § 16.02"; point: "... ECPA and SCA rules on employer access
  to stored workplace messages, the employer's policy and consent, for the Texas office."

## rtr-06: acquired data

- **K2. SUPPORTED.** FTC staff letter to Facebook and WhatsApp, 10 April 2014, and FTC Business Blog, "FTC staff to
  Facebook and WhatsApp: Privacy promises prevail" (Lesley Fair, April 10, 2014): "absent affirmative express consent
  by a consumer, a company cannot use data in a manner that is materially inconsistent" with the promises made when it
  was collected. **Edit:** source "FTC Act § 5; FTC staff letter to Facebook and WhatsApp (April 10, 2014)."

## Not checked here

Points without `check: true` weren't re-verified.
