---
name: wrap
description: End the current CS-core session — write the lesson note / lab report / viva review / trace as applicable, update the tracker, weak areas, review queue, STATUS and the README progress block.
---

# Wrap up this session

Follow the **Wrap-up protocol** in `CLAUDE.md` exactly, based on everything in this conversation.

- Write the session's artifact: lesson note (L/DD/C/WE) to the row's `File:`, lab report to the lab folder
  (LAB), trace to its file (TR), or viva review to `vivas/` (V/Baseline) — from the matching template, at full
  depth, including the learner's predictions, hint rungs, bluffs and explain-back. Never thinner than what was taught.
- Update `progress/tracker.md` statuses honestly: a concept is ✅ only when the full mastery bar (roadmap §4)
  has been shown across sessions; a LAB/TR is ✅ only when predict+measure+explain (or an unbroken trace) is
  recorded; otherwise 🔄 with a resume point. Record viva scores. Record hint rungs (H2–H3 → first review +1,
  H4 → repeat derive-back scheduled).
- Update `progress/review-queue.md` (+2/+7/+21/+60 for newly 🔄 concepts; mark reviewed rows), `progress/weak-areas.md`
  (new gaps verbatim with the correct mechanism; resolve those answered right twice), and `progress/STATUS.md`
  (Next session per the active track, or resume point; one log line; keep ~15).
- Prompt the learner to add their glossary / numbers / interview-bank entries and (at phase end) the concept map;
  verify what they write.
- After editing roadmap files or if the tracker looks stale, run `python3 tools/gen_tracker.py`. Use `date +%F`.
- Keep the README §Current progress block in sync with STATUS.
- Finish with a 2–3 line summary: what was recorded, current standing, and what's next (ID + type + Hook, not the mechanism name).
