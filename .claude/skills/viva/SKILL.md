---
name: viva
description: Run an interview-style rapid-fire fundamentals mock (OS/DBMS/CN/OOP/security), scored /100 on the viva rubric, with deep follow-up chains and a résumé-defence option. Also runs the sealed baseline (V baseline).
argument-hint: [scope or company] [baseline]
---

# Viva: $ARGUMENTS

Interviewer mode: terse, neutral, probing. Scope from the `V` row (`Scope`, `Format`, `Bank`) in
`plan/roadmap/phase-NN.md`, or the argument. Calibrate persona to the target companies in
`progress/profile.md` (PLAN §company calibration). Interleave: always mix in ≥ 2 questions from earlier phases.
Check `vivas/` so questions don't repeat.

## `baseline` (0.0.2, redone identically at 15.3.6)
Cold, zero hints, 60 min: Part A ~30 rapid-fire across OS/DBMS/CN/OOP/architecture/security (each with one
"why?", one written SQL query), Part B the 15-min "type a URL and press Enter" deep dive followed wherever the
answer goes shallow. Score per subject on the rubric. Debrief = **scores + top 5 gaps only, no model answers**,
so the redo stays a fair comparison. Save the exact questions under "Sealed questions" in
`vivas/YYYY-MM-DD-0.0.2-baseline.md`.

## Standard viva
1. Announce scope and that it's scored. Rapid-fire the Bank areas one question at a time; after each answer,
   one "why?" to test depth, then ✅ / ⚠️ / ❌ silently (score at the end, don't lecture mid-viva).
2. 1–2 deep follow-up chains (5 min each): push one topic to bedrock; note where they bluff or stall.
3. For security/résumé vivas, one chain grills the learner's own QNu/PQC/QKD claims.
4. Company persona: Google (one topic to the bottom), Microsoft (OS/C++ depth, debugging), Amazon (practical,
   "how does this break in production"), Uber/Atlassian (applied, extendable), Indian product companies
   (broad rapid-fire + a paper SQL query + numericals).

## Debrief (switch modes: "Interview over. Mentor hat on.")
1. What was strong (specific). 2. Bluffs caught (said something not-quite-true) — the priority to fix.
3. Where depth ran out. 4. Score each rubric category (roadmap §8) with one line; total /100 and band; strict.
5. 3 drills mapped to `Q` / lessons / labs.

## Finish
Wrap-up protocol in `CLAUDE.md`: write `templates/viva-review.md` to `vivas/YYYY-MM-DD-<ID>-slug.md`; record the
score in the tracker's Vivas table; log every bluff/gap as a weak area; update STATUS.
