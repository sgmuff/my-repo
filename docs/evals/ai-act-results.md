# AI Act skills: blind holdout results

Scored 2026-10-21. Eight scenarios (`ai-act-scenarios.yaml`), each run once with the skill (`ai-act-provider` or
`ai-act-deployer`) and once without, in separate sessions. One blind comparator per pair, following the frozen key.

- Key: `ai-act-answer-keys.yaml`, key_version 6, SHA-256 `f87490564ddeb15a3e016e7e91bfedf09130523c50eb90fda3f469bbf1d3a273`
- legal_text_date: 2026-10-21. Open item at scoring: aip-02 K2 (application date of Arts. 6(4) and 49(2) only).
- The key wasn't changed after any output was opened.

## Results

Adjusted score = weighted key score minus 5 for each independent material error.

| Scenario | With skill | Without | Winner | Deductions (with / without) | Usability, mean of requester and regulator (with / without) |
|---|---|---|---|---|---|
| aip-01 CV ranking | 100.0 | 90.0 | skill | 0 / 0 | 4.5 / 4.0 |
| aip-02 essay checker | 94.4 | 94.4 | baseline (usability) | 0 / 0 | 4.0 / 4.5 |
| aip-03 lift brake module | 100.0 | 75.0 | skill | 0 / 0 | 5.0 / 3.0 |
| aip-04 emotion scoring | 81.2 | 81.2 | skill (usability) | 0 / 0 | 4.5 / 3.5 |
| aid-01 rebranded credit model | 81.8 | 63.2 | skill | 0 / 5 | 4.5 / 3.0 |
| aid-02 benefits triage | 79.2 | 83.3 | baseline | 0 / 0 | 4.5 / 4.0 |
| aid-03 website chatbot | 83.3 | 88.9 | baseline | 0 / 0 | 4.5 / 4.0 |
| aid-04 warehouse shifts | 100.0 | 83.3 | skill | 0 / 0 | 4.5 / 4.0 |
| **Mean** | **90.0** | **82.4** | skill 5, baseline 3 | 0 / 5 | **4.50 / 3.75** |

Provider scenarios: 93.9 with, 85.2 without. Deployer scenarios: 86.1 with, 79.7 without.

## What drove the difference

- **Dates.** Without the skill, all eight answers either used the pre-Omnibus timetable (Annex III from 2 August 2026,
  Annex I from 2 August 2027) or treated Regulation (EU) 2026/1744 as an unadopted proposal, per the comparators'
  evidence. That failed or halved the date point in aip-01, aip-03, aid-01 and aid-04, and cost points or usability in
  aid-02, aid-03, aip-02 and aip-04. With the skill, every answer used the amended dates from `eu-ai-act.md`. This is
  the largest single effect.
- **Conditions.** With the skill, answers more often made the conclusion depend on the stated facts (aid-04 K1, the
  vendor's intended purpose; aid-01, the triggers). The one independent material error, misstating the Art. 25(2)
  exception, was without the skill.
- **Where the baseline did better.** aid-02: the baseline assessed Art. 22 and Art. 86 conditionally and raised
  discrimination risk; the skill answer was weaker on both (K3, K7). aid-03: the skill answer gave Art. 50(1) without its
  "unless obvious" exception and didn't raise chat-log retention.
- **Missed by both.** aid-01 K1 and K2 (the Art. 25(1)(a) proviso and the full substantial-modification test); aid-02 K8
  (the two-part Art. 111(2) analysis; the skill got half credit, the baseline none); aip-04 K2 (the Commission's view on
  workplace stress); aip-02 K6 (GDPR roles).

## Fixes made after scoring

These change the skills, so the eight scenarios are now development cases, not holdouts.

1. **`outside-scope` kind for provider files.** gov had no kind for a system outside Annexes I and III, so the aip-02
   record was labelled "Not high-risk (Art. 6(3))" and given the Art. 49(2) method, which the answer itself said didn't
   apply. Added the kind (requires Art. 4; Art. 50 where relevant), its method line, label, a route-mismatch finding,
   and two tests.
2. **Art. 111(2).** The reference timeline tied 2030 to systems "already on the market", the narrow reading counsel
   rejected. Rewritten to counsel's reading, and a new issue rule, `ai-public-transition`, raises it for any record
   tagged `public-body`. The rule is new legal content in a counsel-owned file: counsel to confirm.

## Caveats

- Eight pairs, one run each. Single grades have varied by up to 10 points between runs, so the per-scenario losses in
  aid-02 (4.1) and aid-03 (5.6) are within noise. The mean gap (7.6) and the date pattern are the robust findings.
- Blinding is partial: the skill outputs include YAML records.
- The comparator applies counsel's rubric; it isn't counsel. Counsel may want to spot-check aid-01 and aid-02, the two
  closest to contested law.
