---
name: lab
description: Run a hands-on lab — predict → run → measure → explain. The learner writes the code and runs the commands (Claude gives setup, never the solution), then Claude interprets the results against the mechanism and writes the lab report.
argument-hint: [session ID or lab]
---

# Lab: $ARGUMENTS

Row = the `LAB` row for the ID in `plan/roadmap/phase-NN.md` (or the next session). Its **Hook, Predict,
Build/Run, Measure, Explain, Probe** fields are the contract. Machine facts: RHEL9 kernel 5.14, gcc/g++ 11.5,
i7-13620H (6 P-cores + 4 E-cores; pin with `taskset`), no `perf`/libasan by default (offer the install line;
valgrind, gdb, strace, docker, tshark, openssl 3.5 present). Build C/C++ with `tools/run.sh <file>`.

## Flow
1. **Predict (before any code runs).** State the Hook; the learner commits to numeric predictions for every
   quantity in the row's Predict field, with a reason each. Do not hint at the answer. Record them.
2. **Build.** Give setup only: skeleton structure, the commands, the flags, the tools. The learner writes the
   actual code in `labs/<ID>-slug/`. Never write their solution; if stuck, use the hint ladder.
3. **Run & measure.** The learner runs it (repeats, medians, pinned cores where it matters) and reports the
   numbers into the row's Measure table.
4. **Explain.** For every place prediction ≠ measurement, the learner explains why from the mechanism; you
   confirm or correct. Connect back to the lesson(s) this lab proves. Pull good numbers into `reference/numbers.md`.
5. **Probe.** Ask the row's follow-ups.

## Finish (wrap-up protocol in `CLAUDE.md`, plus)
- Write `templates/lab-report.md` to the lab folder with predictions vs measurements and the mechanism.
- Tracker LAB row → ✅ only when prediction, measurement and a correct mechanistic explanation are all recorded;
  otherwise 🔄 with the resume point in STATUS. Log any surprise as a weak area if the mechanism wasn't understood.
