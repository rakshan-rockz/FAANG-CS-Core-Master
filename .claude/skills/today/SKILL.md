---
name: today
description: Start the next CS-core session — runs due spaced reviews, then resumes the next session from progress/STATUS.md (following the active track) with the right skill.
---

# Start the next session

1. Run `date +%F`. Read `progress/STATUS.md` (note **Active track**), `progress/profile.md`,
   `progress/review-queue.md`, `progress/weak-areas.md`, and the current `plan/roadmap/phase-NN.md`.
   If the active track is `switch`, also read `plan/roadmap/TRACK-switch.md`.
2. If `progress/profile.md` is blank → next session is 0.0.1 (`/intake`). If no baseline exists in `vivas/`
   → next is 0.0.2 (`/viva baseline`).
3. **Find the next session by the active track:**
   - `switch`: the next unfinished row in `TRACK-switch.md` order. After its last row, set the active track
     to `depth` in STATUS and continue with the first depth row not yet done.
   - `depth`: the **Next session** ID in the phase file, in phase order.
   If STATUS notes a resume point, resume there. If the last log entry is 7+ days old, open with a 10-minute
   re-entry: cold derive-back of the last 2 concepts touched (from their Hooks).
4. Present a ≤ 7-line plan: due reviews (count + topics); the session ID · type · title and, for L/DD/C, the
   **Hook only** (never the mechanism name); the sub-points it must cover (from the row) or the lab/viva goal;
   one weak area to resurface; the row's **Scope** if on the switch track. Short on time? offer the floor day
   (`/quiz 5` + due reviews). Ask "Ready?"
5. On go: due reviews first (≤ 10 min: each = derive-back from the Hook in ≤ 5 min + one Probe; mark the queue),
   then run the skill for the type:

   | Type | Skill |
   |---|---|
   | Intake | `/intake` |
   | Baseline | `/viva baseline` |
   | L | `/lesson learn` |
   | DD | `/lesson deep-dive` |
   | C | `/lesson compare` |
   | WE | `/lesson we` |
   | LAB | `/lab` |
   | TR | `/trace` |
   | V | `/viva` |
   | Q | `/quiz` |
   | R | `/weekly-review` (monthly mode if ≥ 4 weeks since the last one) |
   | Gate | `/gate` |

6. Finish with the wrap-up protocol in `CLAUDE.md` (`/wrap`).
