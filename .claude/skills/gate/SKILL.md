---
name: gate
description: Run a phase exit gate from the roadmap — calibration predictions, the phase concept map, then a cold test of every criterion with fresh prompts; pass unlocks the next phase, any failure creates a targeted remediation cycle and a retry.
argument-hint: [phase number]
---

# Phase gate: $ARGUMENTS

Phase = argument, or the current phase in `progress/STATUS.md`. Read the **Gate** checklist at the bottom of
`plan/roadmap/phase-NN.md`, plus `progress/tracker.md` and `progress/weak-areas.md`.

## Rules
- Interviewer mode. Cold: no notes, no hints (unless a criterion allows them), no teaching during the gate.
- Every criterion is tested with **fresh** prompts not used in lessons/labs/vivas.
- May span sittings; record per-criterion progress in STATUS between them.

## Flow
1. Announce the gate and its criteria. **Calibration:** the learner predicts pass/fail and confidence 1–5 per
   criterion. Record the predictions.
2. **Concept map** of the phase (required): critique missing or wrong links.
3. Test each criterion (derive-back from a fresh Hook, a numerical on paper, a mini-viva chain, a lab
   prediction-and-explain, a `tools/run.sh` build where relevant). Mark ✅ / ❌ with a one-line reason.
4. Compare predictions with results; note systematic over/under-confidence in `progress/profile.md`.
5. Result:
   - **All ✅** → gate passed: tracker Gates table (status, attempts, date); concepts meeting the full mastery
     bar → ✅; next session = the next row on the **active track**; 2-min profile refresh.
   - **Any ❌** → write a **remediation cycle** into STATUS: for each failed criterion, the specific sessions to
     redo (as harder deep-dives, not replays) plus a fresh probe/lab. Next session = the first remediation item.
     Retry = the failed criteria + one spot-check of a passed one.
6. Tell the learner plainly what passed, what didn't, and why. No softening. Attempts are unlimited.

## Finish
Wrap-up protocol in `CLAUDE.md` (Gates table: status, attempts, date passed).
