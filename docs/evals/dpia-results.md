# DPIA skill: blind holdout results

Scored 2026-10-23. Six scenarios (`dpia-scenarios.yaml`), each run once with the `dpia` skill and once without, in
separate sessions. One blind comparator per pair, following the frozen key, with A and B assigned by a sealed random
order fixed before any run.

- Key: `dpia-answer-keys.yaml`, key_version 2, SHA-256 `28478728b479ba27c441de9a205e03d06d3aa863a1c53077f6cda9f9b5a9153e`
- legal_text_date: 2026-10-22. Open items at scoring: CPCE L34-5 (dpia-02 K4) and the Garante's list item (dpia-03 K1).
- The key wasn't changed after any output was opened.
- Run note: the first with-skill runs had a broken `gov` wrapper (a setup error), so all six were stopped, discarded
  unopened, and rerun in clean sandboxes. The without-skill runs weren't affected.

## Results

Adjusted score = weighted key score minus 5 for each independent material error. No answer drew a deduction.

| Scenario | With skill | Without | Winner | Usability, mean of requester and regulator (with / without) |
|---|---|---|---|---|
| dpia-01 gym wearables and insurer | 95.0 | 95.0 | skill (usability) | 4.0 / 3.5 |
| dpia-02 newsletter A/B test | 83.3 | 83.3 | tie | 4.5 / 4.5 |
| dpia-03 delivery driver cameras | 75.0 | 95.0 | baseline | 4.0 / 4.5 |
| dpia-04 library recommendations | 75.0 | 81.2 | baseline | 4.5 / 3.5 |
| dpia-05 B2B CRM enrichment | 100.0 | 85.7 | skill | 4.5 / 4.0 |
| dpia-06 hospital AI triage update | 81.2 | 37.5 | skill | 4.5 / 3.5 |
| **Mean** | **84.9** | **79.6** | skill 3, baseline 2, tie 1 | **4.33 / 3.92** |

Points, with / without: dpia-01 K5 0.5/0.5; dpia-02 K3 and K4 0.5/0.5; dpia-03 K1 0.5/1, K2 0.5/1, K5 1/0.5, K6 0.5/1;
dpia-04 K1 0.5/1, K3 1/0.5, K5 0/0.5; dpia-05 K1 1/0.5; dpia-06 K1 1/0.5, K3 1/0, K5 1/0.5. All other points scored
the same in both arms.

## What drove the difference

- **AI Act dates and classification.** Without the skill, dpia-06 missed Annex III point 5(d), used the old Annex I
  date, and ruled out a FRIA on that basis (K3, 0 of 2); dpia-03 gave 2 August 2026 and suggested planning for it
  (K5, half). With the skill, both used 2 December 2027 with its amending basis. As in the AI Act holdout, this is the
  largest single effect.
- **Re-rating against unverified measures.** With the skill, dpia-06 re-rated every risk because no measure was
  verified for the new model (K1), and tied Art. 9(2)(h) and Art. 28(10) to the provider's own use (K5).
- **Screening discipline.** With the skill, dpia-05 applied the WP248 criteria as written; without, the answer
  relabelled criterion 9 and counted it (K1).
- **Where the baseline did better.** dpia-03: deeper national labor law (LOPDGDD Art. 89(3) on audio, the Workers'
  Statute Art. 4 exceptions), the Spanish and Italian lists, and Art. 36 decided on its test (K1, K2, K6). dpia-04: Art. 9
  framed conditionally rather than asserted, and the DSFA-V content applied (K1, K5).
- **Missed by both.** The Irish and Dutch list items and the Irish list's screening condition (dpia-01 K5); the CNIL's
  March 2026 rule that open-rate measurement needs consent even when aggregated, and the soft opt-in's conditions
  country by country (dpia-02 K3, K4); asking for the provider's updated documentation, and mapping data flows before
  treating US hosting as a transfer (dpia-06 K2, K4).

## Fixes made after scoring

These change the skill, so the six scenarios are now development cases, not holdouts.

1. **Art. 36 finding.** `gov` raised the prior-consultation finding whenever the current rating was High and the call
   wasn't "yes", so a reasoned "no" could never clear it. That pushed the dpia-03 answer to "Art. 36(1) met today," the
   reasoning the key penalizes (K6). The finding now fires only while the call is undecided, and the skill says the
   rating prompts the decision but isn't the test.
2. **Issue IDs with digits.** The `issues` schema rejected `dpia-art9-condition`, so three runs couldn't record their
   response to it. Fixed in `8ed1058`.

**Proposed for counsel (reference content, not applied):** the national-list misses (dpia-01 K5, dpia-03 K1,
dpia-04 K5) and the CNIL pixel miss (dpia-02 K3) share a cause: `gdpr.md` names the Art. 35(4) lists but doesn't
summarize them, and has nothing on the CNIL's 2026 pixel recommendation. The items checked for the key
(`dpia-verification.md`) would fill that gap for Ireland, the Netherlands, Spain, and Austria, plus the CNIL rule.

## Caveats

- Six pairs, one run each. Single grades vary by up to 10 points between runs, so per-scenario gaps under 10
  (dpia-04, 6.2) are within noise. The mean gap (5.3) is smaller than the AI Act holdout's (7.6); the AI Act effect in
  dpia-06 accounts for most of it.
- Blinding is partial: the with-skill answers include rendered records.
- The comparator applies counsel's rubric; it isn't counsel. dpia-03 and dpia-04, the two the baseline won, are the
  ones worth a spot-check.
