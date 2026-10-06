---
name: intake
description: Intake interview (session 0.0.1, refreshed at gates) — captures targets, companies, timeline, background, C/C++ fluency, CS-subject state and tool availability into progress/profile.md, with unscored calibration questions, to set the active track and calibrate emphasis and viva style.
---

# Intake interview

Goal: fill `progress/profile.md` so emphasis, examples, viva style and difficulty fit this learner.
~30–45 min. **Content is never reduced by intake**; only emphasis, examples, pacing and viva personas change.

1. Explain in 3 lines why this matters: target companies set viva style; the 12-month switch context sets
   the active track (switch first); the QNu/crypto background changes how hard Phase 13 is pushed; C/C++
   fluency and installed tools set how the labs run.
2. Ask the profile sections a few at a time: targets & companies (which first?) & timeline → rhythm &
   availability → background (experience, which CS subjects are solid vs rusty, systems built, crypto/PQC/QKD
   depth) → C/C++ fluency and other languages → tools installed (perf, libasan/libtsan, docker, postgres image,
   openssl 3.5) → preferences (voice, bluntness, interview anxieties). Probe vague answers ("'I know OS' —
   explain a context switch" / "'used Postgres' — did you ever read an EXPLAIN?").
3. Calibration (unscored, ~10 min): 5 quick questions across subjects (process vs thread; what a page fault
   is; TCP vs UDP; what an index does; what a vtable is) each with one "why?"; note answers in the Mentor column.
4. State the calibration: the depth bar for the target companies, which subjects to push hardest (weak ones +
   crypto for QNu relevance), the answer shape (definition → mechanism → example → trade-off → next layer),
   and set **Active track: switch** in STATUS (unless the learner wants full depth from the start). If a real
   interview is near, say honestly what the switch track covers by then and offer extra vivas/SQL rounds —
   never cut lessons.
5. Confirm tool availability with the learner and note gaps (e.g. no perf/libasan) so labs adapt. Write
   `progress/profile.md`; update `progress/STATUS.md` (Started date; next = 0.0.2 baseline).
