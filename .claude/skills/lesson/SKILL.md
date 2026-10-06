---
name: lesson
description: Teach a CS-core concept through the Mechanism Protocol — the learner predicts and attacks a Hook before the mechanism is named, derives it from the layer below with the hint ladder, sees the numbers, handles the probes; then Claude writes the lesson note. Modes learn, deep-dive, compare, we (worked example).
argument-hint: [session ID or topic] [learn|deep-dive|compare|we]
---

# Lesson: $ARGUMENTS

Row = the `L`/`DD`/`C`/`WE` row for the ID in `plan/roadmap/phase-NN.md` (or the next session per `/today` and
the active track). The row's **Hook, Derive, Covers, Probe, Anchors, Traps, Reading, Xref, File** are the
contract: every Covers sub-point must be taught; if the sitting ends first, record the resume point in STATUS.
Assign the row's Reading before/after as appropriate. Read `progress/weak-areas.md` and plan to resurface one
related item. On the switch track, teach to the row's **Scope** (note what waits for the depth pass) but never
water down what you do teach.

## Mode `learn` / `deep-dive` / `compare` — the Mechanism Protocol, one step per turn, wait for the learner

1. **Retrieval warm-up**: due reviews; one question linking to the previous session.
2. **Hook**: state the puzzle/observation with its numbers. **Do not name the mechanism, the title, or any
   giveaway term.**
3. **Predict**: "What do you think happens, and why? Give a number if you can." Record the prediction — wrong
   ones are the point.
4. **Naive model**: the learner states the simplest model that would explain the Hook; you give the
   input/case where it fails (a counterexample, not a correction).
5. **Derive the mechanism**: steer toward the row's **Derive** chain with the hint ladder (§6 of the roadmap
   README), one rung per request; ask "who does this step: hardware, kernel, library, or the program?" Record
   the highest rung used.
6. **Name it**: now the standard term, its lineage, and where it lives in real systems (Linux, glibc, Postgres,
   OpenSSL, the CPU…).
7. **Covers**: every sub-point, in ≤ 25-line chunks, each ending with a check question.
8. **Magnitudes**: each claim gets a number with a reason (ns, bytes, pages, RTTs); the learner estimates
   first. Add the good ones to `reference/numbers.md`.
9. **Probe**: the row's follow-ups, one at a time, in interviewer voice.
10. **Position it**: when it's the wrong tool / where it breaks; build the comparison-vs-nearest-alternative
    table with the learner (they fill it first).
11. **Explain-back**: the learner's 2-minute interview answer (voice encouraged), graded precise / missing /
    wrong; if it's a classic question, the best version goes to `reference/interview-bank.md` (they write it).

Modes: `learn` = the full flow (breadth). `deep-dive` = skip to step 5, go beneath the surface (edge cases,
magnitudes, real implementations, what breaks); heavy on "how big can it get?" and "who does this?".
`compare` = build the comparison table across ≥ 2 alternatives with the learner, then 3 "which would you pick
and why?" scenarios.

## Mode `we` (worked example — cognitive apprenticeship, *model*)

Solve the row's problem(s) out loud as an expert would (numerical problems, derivations, proofs), including one
deliberate dead end and how you noticed it, naming each move and the phase/layer it draws on. The learner
annotates each step ("what did the mentor do, and why then?"), then solves the sibling problem(s) alone; debrief
against the model.

## Style
- ≤ ~25 lines per turn; end each turn with a question. One idea at a time. This is a terminal, not a textbook
  (the lesson *note* is the opposite — full).
- Every number gets a reason; every definition gets a mechanism. Correct misconceptions immediately and log them.
- Call out the row's **Traps** by name when they happen.

## Finish (wrap-up protocol in `CLAUDE.md`, plus)
- Write the lesson note to the row's `File:` from `templates/lesson-note.md`, including the learner's
  predictions, wrong turns, hint rungs and explain-back. It's the complete record — never thinner than what was taught.
- Tracker row → 🔄 (✅ only when the full mastery bar is met later); review-queue +2/+7/+21/+60 (first review +1
  if H2–H3 hints were needed). Prompt the learner to add glossary/numbers/interview-bank entries; verify them.
