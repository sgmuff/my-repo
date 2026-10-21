# AI Act evaluation: pre-scoring report

Prepared 2026-10-21, before any sealed run output was opened. **Status: stopped for counsel review**: one material legal
question is open (aip-04 K2). The eight sealed pairs haven't been scored.

## Rubric

- File: `docs/evals/ai-act-answer-keys.yaml`, **key_version 5**
- SHA-256: `d40626893356dc27bf691f4a384073944e7b5f5133a64f6569c2fabc07a5d6a1`
- legal_text_date: 2026-10-21 (the date the texts were checked; each text and its own date are listed in the key header)
- Revision log: `docs/evals/ai-act-key-changelog.md`. Version 4 archived in `docs/evals/ai-act-key-history/`.
- Points: 49 across 8 scenarios. Open `check` flags: aip-02 K2 (application date only), aip-04 K2 (counsel decision).

## Changed points in version 5

| Point | Change |
| --- | --- |
| Header | No-double-penalty covers affirmative errors; headline rule added (no separate point; a misleading headline is an error only if it materially misleads and nothing else captures it) |
| aid-02 K6 | Deleted; content moved into K8 |
| aid-02 K8 | Starts from the 2 December 2027 baseline; cites Art. 113 |
| aid-01 K1 | Names the Art. 25(1)(a) proviso; credits either reading if reasoned; no automatic safe harbour |
| aid-01 outcome | Proviso stated, its effect unsettled |
| aid-01 K7 (`# added`) | SCHUFA holding stated precisely; GDPR Art. 22, DPIA and CCD2 Art. 18(8) kept separate |
| aid-04 K4 | Citations corrected; wording unchanged |
| aip-04 K2 | Final guidelines cited; wording unchanged; flagged for counsel |
| check flags | Removed from aid-02 K8, aip-03 K4, aid-03 K4, aid-04 K4, aid-01 K7 |

## Scoring rules (from the key header)

1. For each point: 1 covered correctly, 0.5 partly, 0 missing or wrong. must = 2, should = 1. Key score = weighted %.
2. Score reasoning and conditions, not agreement with the outcome. A defensible, reasoned different conclusion isn't an error.
3. Material error (−5): a legally incorrect proposition, failure to address a controlling requirement, or an unjustified
   conclusion contradicting the facts. A missing caveat counts only if it makes the conclusion materially misleading.
4. No double penalty: an error that makes a point fail, whether an omission or a wrong statement, isn't also deducted.
   Deduct 5 only for an independent material error that no point captures. Never count one error twice.
5. No headline-consistency point; a headline beyond the analysis is a material error only if it materially misleads and
   no point captures it.
6. Score classification and duties separately only where they test distinct requirements. Don't require a recital of
   every article.
7. Apply the "Effect on scoring" column of counsel's dispositions in `docs/evals/ai-act-verification.md`.
8. Each scoring run records key_version, legal_text_date and the open items.

## Calibration (six unsealed answers, re-run on version 5)

| Case | Tests | v4 | v5 | Points that moved | Matches expectation |
| --- | --- | --- | --- | --- | --- |
| c1 aid-02 | 2027 deadline unqualified | 65.4 | 75.0 | K6 deleted; K5 0.5 → 1 | Yes. The missing Art. 111(2) analysis now fails one point (K8), not two. K5 moved on a borderline call (grader variance) |
| c2 aid-02 | Reasoned 2030 | 84.6 | 83.3 | K6 deleted | Yes. K8 full credit; reasoned alternative date not penalised |
| c3 aid-02 | Art. 22/86 asserted | 65.4 | 62.5 | K6 deleted | Yes. K3 = 0, K8 = 0.5; both errors tied to their points, no deduction |
| c4 aid-01 | Triggers merged | 72.7 | 59.1 | K1 0.5 → 0; K7 1 → 0.5 | Yes. K1 now 0 as expected under the revised point; K7 lower because the point became stricter |
| c5 aid-01 | Reasoned alternative | 100 | 95.5 | K7 1 → 0.5 | Yes. No deduction for the different conclusion or the leaning headline (hedged, corrected in the body) |
| c6 aid-04 | One wrong date | 83.3 | 83.3 | none | Yes. K2 = 0, no extra deduction |

**Double-penalty audit:** no deduction in any of the 12 grades. Every recorded error names the point it fails. No defect
fails more than one point under version 5 (in version 4, c1's defect failed K6 and K8).

**Residual anomalies (not rubric defects):**
- Grader variance on half-credit calls: c1 K5 (0.5 then 1), c4 K1 in version 4. Single runs vary; the earlier holdouts
  showed up to 10 points.
- The outcome rating is reported but not scored, so c5 scores 95.5 with outcome "partly". This is counsel's decision 3.
- Graders sometimes record an omission as an "error" with no deduction (c2 K4). Harmless, but noisy.

## Sources verified

All in `docs/evals/ai-act-verification.md`, with pinpoints and dates: AI Act consolidated text as at 27 July 2026 (Arts.
3, 5, 6, 25, 26, 27, 43, 49, 50, 111, 113; Annex III); Commission Guidelines C(2025) 5052 final (paras 249, 257, 263);
Directive (EU) 2023/2225 Arts. 18(8), 48(1); CJEU C-634/21; Code du travail L1222-4, L2312-8, L2312-38; Kodeks pracy
Arts. 22^2, 22^3; Polish Act of 7 April 2006 Arts. 1(2), 13(1)(3).

## Open issues

1. **aip-04 K2: COUNSEL DECISION REQUIRED (blocks scoring).** The key says "stress alone can describe a physical state
   rather than an emotion". The Commission's final guidelines say the general monitoring of workplace stress levels isn't
   covered by the safety exception (para 257), and give an AI measuring employees' anxiety through stress levels as a
   prohibited example unless the stress poses a specific danger (para 263). Recital 18 excludes physical states such as
   pain or fatigue. Options: (1) keep the key; (2) follow the guidelines, so stress inferred from voice at work is
   presumptively emotion recognition; (3) credit either reading if reasoned. It changes K2's credit, not the outcome,
   since the tool also scores frustration.
2. **aid-01 K1: Art. 25(1)(a) proviso.** Its legal effect is unsettled. The key now credits either reading if reasoned,
   so this doesn't block scoring; counsel may still take a position.
3. **aip-02 K2:** the date from which Arts. 6(4) and 49(2) apply to a system concluded not to be high-risk wasn't
   confirmed. It doesn't affect the scenario.
4. **aid-04 K4 residuals:** CSE headcount thresholds and Polish union consultation on work rules weren't checked; the key
   doesn't depend on them.

## What happens next

Once counsel decides issue 1, the key is frozen at that version (5, or 6 if the K2 wording changes). Eight blind
comparisons then run on `scratchpad/blind-aiact`, following `scratchpad/compare-prompt-aiact.md`, and each comparison
records the key version, legal_text_date and open items. The key isn't changed in response to the results.

## Release decision (2026-10-21)

Counsel instructed Claude to apply its recommendation on open issue 1: option 3, credit either reading of "stress" if
reasoned. Applied as **key_version 6**, frozen for scoring. SHA-256
`f87490564ddeb15a3e016e7e91bfedf09130523c50eb90fda3f469bbf1d3a273`; legal_text_date 2026-10-21. Open items at scoring:
aip-02 K2 (application date of Arts. 6(4) and 49(2) only). Version 6 changes only aip-04 K2 and its outcome, which no
calibration case tests, so calibration wasn't re-run. The sealed pairs are scored against this version without changes.
