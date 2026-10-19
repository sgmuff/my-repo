# EU AI Act: general-purpose AI models

| Field | Value |
|---|---|
| Covers | AI Act Chapter V (Arts. 51–56): duties of providers of general-purpose AI (GPAI) models, with and without systemic risk |
| Version covered | Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744; see `eu-ai-act.md` for the rest of the Act |
| Sources | EUR-Lex (Regulation 2024/1689, Annexes XI–XIII); the General-Purpose AI Code of Practice (July 10, 2025); Commission guidelines on GPAI model obligations (July 2025); the AI Office training content summary template |
| Last verified | 2026-10-18, against secondary sources (law-firm, regulator-guide, and tracker summaries); primary texts not yet read line by line. Reviewed and approved by counsel on 2026-10-19. |
| Review interval | Quarterly |
| Volatile points | §2 (when fine-tuning makes a company a GPAI provider); §4 (Code of Practice signatories and updates); any Omnibus changes to Chapter V |

## Contents

1. Dates
2. Who is a GPAI model provider
3. Duties of every GPAI provider (Art. 53)
4. Duties for models with systemic risk (Art. 55)

---

## 1. Dates

GPAI duties apply from August 2, 2025. Models placed on the market before that date must comply by August 2, 2027 (Art. 111(3)). Regulation (EU) 2026/1744 left Chapter V unchanged in substance; its GPAI changes are institutional, such as the AI Office's exclusive competence over AI systems built on a provider's own GPAI model. The Commission's fining power over GPAI providers (Art. 101) applies from August 2, 2026. *Verify* that date against the Official Journal text.

## 2. Who is a GPAI model provider

A provider develops a GPAI model, or has one developed, and places it on the EU market under its own name. Calling a vendor's model through an API doesn't make the company a GPAI provider (`eu-ai-act.md`, section 9). Modifying or fine-tuning a model can. Under the Commission's guidelines (July 2025), a downstream modifier becomes the provider of the modified model when the compute used for the modification exceeds one third of the original model's training compute. When that isn't known, the benchmark is one third of 10^25 FLOP for models with systemic risk, and one third of 10^23 FLOP otherwise. A model is indicatively GPAI when trained with more than 10^23 FLOP and able to generate language, images, or video. *Volatile:* check the current guidelines and their paragraph numbers before deciding.

## 3. Duties of every GPAI provider (Art. 53)

1. Technical documentation of the model, its training and testing, and evaluation results (Annex XI), kept up to date for the AI Office and authorities
2. Information and documentation for downstream providers that integrate the model (Annex XII)
3. A policy to comply with EU copyright law, including honoring text-and-data-mining opt-outs
4. A public, sufficiently detailed summary of the content used for training, on the AI Office template

Open-source models released under a free and open license are exempt from 1 and 2 unless they carry systemic risk. Providers outside the EU appoint an authorized representative (Art. 54).

## 4. Duties for models with systemic risk (Art. 55)

A model is presumed to carry systemic risk when its training compute exceeds 10^25 floating-point operations, or when the Commission designates it (Art. 51). On top of Art. 53, its provider must:

1. Evaluate the model with state-of-the-art protocols, including adversarial testing
2. Assess and mitigate systemic risks at EU level
3. Track, document, and report serious incidents to the AI Office without undue delay
4. Ensure adequate cybersecurity for the model and its physical infrastructure

Following the Code of Practice is the usual way to show compliance (Art. 56).
