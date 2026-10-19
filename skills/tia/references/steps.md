# Transfer impact assessments

| Field | Value |
|---|---|
| Covers | EDPB Recommendations 01/2020 (six steps); 2021 SCCs Clause 14; the UK transfer risk assessment; Swiss practice under FADP Art. 16 |
| Sources | CJEU C-311/18 *Schrems II*; EDPB Recommendations 01/2020, version 2.0 (June 18, 2021); Implementing Decision (EU) 2021/914, Clause 14; ICO transfer risk assessment guidance and tool; FDPIC guidance on transfers |
| Last verified | 2026-10-18 for structure and the UK test; destination-law points are volatile, see below |
| Volatile points | US surveillance law and its oversight bodies; the EU-US DPF litigation (`gdpr.md`, section 11) |

Mechanisms, adequacy, and the DPF are in `../../_shared/references/gdpr.md`, section 11. This file covers how to run the assessment.

## 1. When a TIA is needed

A TIA is needed when a restricted transfer relies on an Art. 46 tool: SCCs, BCRs, ad hoc clauses, a code of conduct, or certification (EU); the IDTA or UK Addendum (UK); or Swiss-adapted SCCs. It isn't needed when an adequacy decision covers the destination, including a DPF certification that covers this importer and this data: check the DPF list for the importer's exact entity before deciding. Remote access from a third country is a transfer.

Three criteria make a flow a restricted transfer (EDPB Guidelines 05/2021): the exporter is subject to the GDPR for this processing, it discloses or makes the data available to the importer, and the importer is in a third country. Record each one.

**A dormant fallback isn't the tool in use.** SCCs kept in a DPA as a backup to the DPF don't call for a TIA now; one is needed when they become the operative tool. Assess each onward transfer by its own recipient, destination, and tool; an onward transfer that isn't covered doesn't undo the DPF route for the first transfer. Hosting in the UK or EEA doesn't remove a transfer when staff abroad can access the data; it reduces what they see.

## 2. The six steps (EDPB Recommendations 01/2020)

1. **Know the transfer.** Data, people, purpose, format, whether it's stored or accessed remotely, and onward transfers to sub-processors.
2. **Identify the tool.** The SCC module (1 C2C, 2 C2P, 3 P2P, 4 P2C), BCRs, or the UK or Swiss equivalent.
3. **Assess the destination's law and practice** for this importer and this data: can public authorities access it beyond what is necessary and proportionate, and do people have effective redress? Use the importer's own evidence, such as transparency reports and its record of access requests, alongside public sources.
4. **Choose supplementary measures** where step 3 finds a problem: technical (encryption with keys held by the exporter, pseudonymization), contractual (transparency, challenge, and notification commitments), or organizational (access policies, minimization). Only technical measures can stop access the law compels; contractual and organizational ones support them.
5. **Take the procedural steps** the tool needs, such as signing the module and completing its annexes.
6. **Reassess** on a trigger: a change in the destination's law, new sub-processors, an access request, or a change in the importer's certification. Pending litigation, such as the DPF appeal, is a reassessment trigger, not a reason to open a TIA or block launch.

If no measure makes the protection essentially equivalent, the transfer must not proceed, or must be suspended.

## 3. UK and Swiss variants

- **UK:** relying on the IDTA or UK Addendum requires a transfer risk assessment; it's a legal requirement, not a judgment call. Since February 5, 2026 (DUAA, SI 2026/82), the TRA is the statutory data protection test: is protection "not materially lower" than in the UK, judged reasonably and proportionately? Follow the ICO's TRA guidance as updated January 15, 2026.
- **Switzerland:** the FDPIC expects an assessment for transfers on Swiss-adapted SCCs, much like the EDPB steps.

## 4. United States: points to check, not conclusions

*Volatile throughout. Check each against a current source and add a verify flag.*

- **FISA Section 702** can reach "electronic communication service providers," which can include cloud and SaaS providers. Check whether the importer could be one, and the provision's current authorization status.
- **Executive Order 12333** covers intelligence collection outside the US, including data in transit.
- **Executive Order 14086** (October 7, 2022) is a safeguard, not a surveillance law. It added necessity and proportionality limits and a redress mechanism that underpin the DPF adequacy decision, and they apply to all transfers to the US, including those on SCCs, so weigh them in step 3. Check the current status of the redress bodies and the Privacy and Civil Liberties Oversight Board.
- **The CLOUD Act** concerns law enforcement access to data a US provider controls, wherever it's stored. Decide its reach on the same provider facts as FISA 702; don't mark one as applying while the other is open.

## 5. India: points to check

*Volatile. Verify each.*

- **The Digital Personal Data Protection Act 2023, s. 17(1)(d),** exempts much of the Act for data of people outside India processed under a contract with a foreign party. Say only that: the people can't rely on that Act's duties. It isn't, alone, a finding that Indian law gives the data little protection; step 3 turns on public-authority access and on whether the tool's rights can be enforced.
- **The DPDP Rules** start in phases; check which duties apply on the assessment date.
- **Interception powers** such as IT Act s. 69 come with prescribed procedural safeguards; describe them accurately and weigh them against this importer's exposure, rather than summarizing them as unchecked.
- **Enforceability of the tool's third-party rights** in Indian courts; ask counsel.

For other countries, use the EDPB's and national authorities' published country information, and record the source in `destination_law/sources`.
