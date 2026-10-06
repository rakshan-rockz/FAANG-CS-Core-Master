---
name: weekly-review
description: End-of-cycle or end-of-phase review (R sessions) — retrieval and derive-back without notes, re-test weak areas, grow the numbers sheet and interview bank, draw the concept map, insert repeat sessions for anything not owned. Monthly mode is a cumulative cross-phase checkpoint.
argument-hint: [monthly]
---

# Review: $ARGUMENTS

1. Identify the cycle (or phase) from `progress/STATUS.md`. Read its rows in `plan/roadmap/phase-NN.md`, the
   lesson notes and lab reports, `progress/weak-areas.md`, and the `Personal`/reference files it touched.
2. Run it interactively — ask, don't tell:
   - **Understanding**: each concept, a 1–2 min explain-back from memory (from the layer below). Grade.
   - **Construction**: the 2 lowest-confidence concepts, cold derive-back from the Hook.
   - **Recognition / interleaving**: 5 symptom-or-question prompts mixing this cycle with earlier phases.
   - **Weak areas**: re-test each open one; resolve those answered correctly a second time.
   - **Numbers & interview bank**: check the entries this cycle should have added; fix or fill (learner writes).
3. Any concept that fails explain-back or derive-back gets a **repeat session** inserted before moving on
   (note it in STATUS). Nothing is carried forward half-learned.
4. At **phase end**: the learner draws the phase **concept map** (`reference/concept-maps/phase-NN.md`,
   labelled edges); critique it. Then the next session is the phase **Gate** (`/gate`).

## Monthly mode (`monthly`, every ~4–6 weeks)
A 60–90 min cumulative checkpoint over everything so far: 10 interleaved recognition prompts, 3 cold
derive-backs from the oldest ✅ concepts, one numerical from each of OS/CN/DBMS, and a mixed mini-viva.
Compare with the previous checkpoint. Write to `reviews/monthly-YYYY-MM.md`.

## Finish
Write the review from `templates/weekly-review.md` to `reviews/<phase.cycle>-review.md` (or monthly), then the
wrap-up protocol in `CLAUDE.md`.
