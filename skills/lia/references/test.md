# Legitimate interests and compatibility

| Field | Value |
|---|---|
| Covers | The GDPR and UK GDPR Art. 6(1)(f) three-part test; UK recognized legitimate interests (Art. 6(1)(ea), Annex 1); Art. 6(4) compatibility |
| Sources | GDPR Art. 5(2), 6(1)(f), 6(4), 13(1)(d), 14(2)(b), 21 and Recitals 47–50; CJEU C-621/22 *KNLTB* (October 4, 2024); EDPB Guidelines 1/2024 on processing based on Art. 6(1)(f); ICO guidance on legitimate interests |
| Last verified | 2026-10-18 for structure; see the verify points below |
| Volatile points | Whether EDPB Guidelines 1/2024 are final; UK Annex 1 commencement and contents |

Facts about lawful bases in general are in `../../_shared/references/gdpr.md`, section 3. This file covers only how to run the tests.

## 1. When an LIA is the right tool

Run an LIA when a controller relies on legitimate interests for a purpose. A processor never runs one for its customer's purposes: the customer chooses its basis. Public authorities can't rely on legitimate interests for their tasks (Art. 6(1), last subparagraph).

An LIA never supplies an Art. 9 condition. Special category data needs an Art. 9(2) condition as well, which the DPIA names. Tell foreseeable incidental capture (a keystroke log that may hold health details) apart from processing that targets such data; the first is a risk to design out, the second needs the condition.

## 2. The three tests

All three must be met. Record each as a call.

1. **Purpose.** Is the interest lawful, clearly stated, and real and present, not speculative? A commercial interest can be legitimate (*KNLTB*). Recital 47 says direct marketing *may* be one; it isn't automatic.
2. **Necessity.** Is the processing reasonably necessary for that interest, and is there a less intrusive way to reach it? Record the alternatives considered, and ask for evidence that each falls short, such as the uplift an AI score gives over simple rules. A business's preference or convenience isn't necessity, and a less intrusive way that reaches the same result defeats it.
3. **Balancing.** Do the person's interests, rights, and freedoms override? Weigh:
   - their reasonable expectations, given the relationship and the context of collection (Recital 47)
   - the nature of the data and of the processing, including profiling and combining sources
   - the impact, with its likelihood and severity
   - whether they're children or otherwise vulnerable
   - what the outcome changes for the person: ordering a sales queue is not the same as deciding access to an opportunity
   - the safeguards, which can tip the balance

   Give each impact a basis, such as scale or what the score changes, so the ratings aren't false precision.

## 3. Objection and transparency

People can object (Art. 21(1)), and the controller must stop unless it shows compelling legitimate grounds. For direct marketing, including profiling for it, the right is absolute (Art. 21(2)–(3)): processing for that purpose stops, though a minimal suppression record may be kept so the objection is honored. The notice must name the interest relied on (Art. 13(1)(d), 14(2)(b)). For data not collected from the person, give it within a reasonable period and no later than one month, or at first contact if earlier (Art. 14(3)).

GDPR legitimate interests don't settle electronic marketing rules. Email and text marketing may need consent under ePrivacy or PECR whatever the GDPR basis; flag that for counsel.

## 4. UK recognized legitimate interests

UK GDPR Art. 6(1)(ea) and Annex 1 list purposes that need no balancing test, such as certain crime, safeguarding, and emergency purposes. Record the listed purpose and check its conditions. *Verify* that the provision has commenced and that the purpose is on the current list (`gdpr.md`, section 1).

## 5. Compatibility (Art. 6(4))

Service messages a person needs to use what they signed up for are part of the original purpose. Marketing is a new one; keep the two apart.


A new purpose for data collected for another needs either consent, a legal basis in law, or a compatibility assessment of five factors: (a) the link between the purposes, (b) the context of collection and the relationship, (c) the nature of the data, especially Art. 9 and 10 data, (d) the possible consequences, and (e) safeguards such as encryption or pseudonymization. A compatible purpose still rests on the original lawful basis, and only if the original processing was lawful. An incompatible purpose needs a new basis, such as consent; an LIA doesn't make it compatible.

## Verify points

- EDPB Guidelines 1/2024 were adopted for consultation on October 8, 2024. Check whether a final version exists before citing them as final.
- UK Annex 1 and its commencement (`gdpr.md`, section 1).
