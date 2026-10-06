---
name: trace
description: Trace one event through every layer of the machine (keypress → syscall → packet → server → disk, or a program from source to crash). The learner narrates each hop; Claude asks "what happens next, and who does it?" and never lets a layer be skipped.
argument-hint: [session ID or scenario]
---

# Trace: $ARGUMENTS

Row = the `TR` row for the ID in `plan/roadmap/phase-NN.md` (or the next session / the argument). Its **Hook,
Path, Covers, Probe** fields are the contract. The point is to force the whole stack into one continuous story
with no hand-waving.

## Flow
1. State the Hook. Ask the learner to list the hops end to end at a high level first (predict the path).
2. Walk the row's **Path** hop by hop. At each hop the learner says: what happens, and **who does it**
   (hardware / kernel / library / the program / a remote machine), and what data/headers change. After each,
   ask "what happens next?" — do not advance for them.
3. Where they skip a layer or hand-wave ("it goes to the server"), stop and drill that hop (the *layer
   skipping* trap). Tag each hop with the phase that owns it.
4. Fire the row's **Probe** follow-ups, including "what changes if X?" and "what breaks here, and what's the
   symptom?".
5. Close by having the learner narrate the whole trace once, unbroken, in ≤ 3 minutes.

## Finish (wrap-up protocol in `CLAUDE.md`, plus)
- Write the trace to the row's `File:` (or `vivas/…` for the 15.x whole-stack traces) as a labelled hop list
  with who-does-what. Tracker TR row → ✅ when the learner narrates it unbroken and survives depth-on-demand at
  any hop; else 🔄. Log skipped layers as weak areas.
