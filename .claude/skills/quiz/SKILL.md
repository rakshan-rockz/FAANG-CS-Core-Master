---
name: quiz
description: Rapid retrieval-practice quiz on covered CS-core concepts, weighted to due reviews, weak areas and low-confidence topics, interleaving across phases. Also the 15-minute floor day.
argument-hint: [subject] [n questions]
---

# Quiz: $ARGUMENTS

1. Read `progress/review-queue.md`, `progress/tracker.md`, `progress/weak-areas.md`. Pool = concepts that are
   🔄/✅ (plus the given subject). Weight: due reviews > open weak areas > confidence ≤ 3 > oldest last-touched.
   Never quiz untaught (⬜) material. Always interleave across phases.
2. Ask 8 (or n) questions one at a time, mixing:
   - "Explain X in two sentences, from the layer below."
   - a quick numerical ("EAT with 97% TLB hit, 100 ns memory, 3-level table?").
   - "What breaks if…?" / "who does this step?"
   - "Which would you pick and why?" comparisons.
   - recognition: a symptom → name the mechanism ("loops 10× slower past 8 MB → ?").
3. After each: ✅ / ⚠️ / ❌ + a 1–3 line correction. No lectures.
4. End with x/n and the 2–3 topics that need work.

## Finish
Update tracker confidence; mark review-queue items ✅/❌ (❌ resets to +2 and opens a weak area); resolve weak
areas answered correctly a second time; STATUS log line.
