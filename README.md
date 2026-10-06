# FAANG CS Core Master

A mentor-run, in-depth **Computer Science core** course — computer architecture, operating systems, networks,
databases, programming languages & compilers, security & cryptography, and theory of computation — run by
Claude Code the way its sibling repos (`FAANG-System-Design-Master`, `FAANG-DSA-Master`) are run.

Two goals, one course:
1. **Pass the switch.** The CS-fundamentals rounds (OS, DBMS, CN, OOP) and SQL rounds that Microsoft, Amazon,
   Google, Uber, Atlassian, Adobe, Oracle, Flipkart and similar product companies run — reachable in ~60 h via
   the 🎯 switch track.
2. **Master CS core in depth** — a strong university sequence plus real-systems insight and hands-on labs —
   over the full depth track, with cryptography/PQC/QKD taken to practitioner depth (directly relevant to the
   learner's work at QNu Labs).

**The North Star:** be able to explain any layer of the machine *from the mechanism of the layer below*,
predict what happens when a parameter changes, and defend it through an interviewer's third "why?". Not
definitions — mechanisms.

## 🚀 How to use this repo (with Claude Code)

Open Claude Code in this folder and type **`/today`**. It runs your due reviews, then the next session on your
active track. Start with `/intake`.

| When you want to… | Type |
|---|---|
| Do the next thing | `/today` |
| Set up your profile & pick the track | `/intake` |
| A fundamentals mock, scored /100 | `/viva os` (or `dbms`, `cn`, `oop`, a company name) |
| Learn a concept (predict first, then derive it) | `/lesson` |
| A hands-on lab (predict → run → measure → explain) | `/lab` |
| Trace one event through every layer | `/trace` |
| Get unstuck, one hint at a time (never the answer) | `/hint` |
| A 15-minute floor day | `/quiz 5` |
| A cycle/phase review | `/weekly-review` |
| A phase exit gate | `/gate` |
| End a session (saves everything) | `/wrap` |

**How a lesson works:** it starts with a *puzzle*, not a definition — "why does this loop get 10× slower past
8 MB?", "why does `fork()` return twice?", "why does `NOT IN` with a NULL return nothing?". You predict the
answer, attack it, and derive the mechanism from the layer below with the smallest possible hints. Then you see
the numbers, handle the interviewer's follow-ups, and explain it back in two minutes. Labs make it real: you
measure the cache, the context switch, the fsync, the TCP handshake, and you build a B+ tree, a WAL and an
interpreter. The notes are written *afterwards*, as the record of *your* reasoning.

Details: [`plan/roadmap/README.md`](plan/roadmap/README.md) (the protocol, tracks, rubric) ·
[`plan/roadmap/TRACK-switch.md`](plan/roadmap/TRACK-switch.md) (the ~60 h interview path) ·
[`plan/PLAN.md`](plan/PLAN.md) (strategy, reading plan, overlap with System Design/LLD) ·
[`DECISIONS.md`](DECISIONS.md) (every setup decision) · [`CLAUDE.md`](CLAUDE.md) (how Claude runs it).

**Source of truth:** `progress/STATUS.md` (what's next + active track) and `progress/tracker.md` (generated).
The block below mirrors them.

---

## 📊 Current Progress

**Active track:** switch (interview fundamentals first) · **Next session:** `0.0.1` Intake → `0.0.2` Baseline CS
viva (sealed)

```text
Switch track (🎯 interview fundamentals, ~62 h)
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0/37 rows

Full course (Phases 0–15)
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% · concepts 0/205 ✅ · labs/traces 0/60 · gates 0/16
```

**State (2026-09-25):** repository built and tested (tracker generates, hook runs, `tools/run.sh` builds C/C++).
Nothing taught yet. Start with `/intake`, then the sealed baseline, then the switch track.

**Up next:** Intake (targets, companies, tools, C/C++ level) → sealed baseline CS viva → switch track: OS
(process/scheduling/memory/concurrency/deadlock) → DBMS (relational, SQL, normalisation, indexes, transactions)
→ CN (layering, TCP, subnetting, routing, day-in-the-life) → OOP/C++ → quantum-threat awareness → rapid-fire
vivas + company mock + baseline redo. Then the depth track fills in everything, in full.

**Study rhythm (suggested, not enforced):** most days a lesson or lab + its review; vivas and SQL rounds on
heavier days; a monthly cumulative checkpoint. Progress over timeline — a gap just means `/today` opens with a
short re-entry review.

---

## 🗂️ Repository map

| Path | Purpose |
|---|---|
| `plan/roadmap/phase-00…15.md` | Every session (ID, type, Hook/Derive/Covers/Probe/Anchors/Reading) + each phase gate |
| `plan/roadmap/README.md` | The Mechanism Protocol, session types, hint ladder, mastery bar, viva rubric, route, tracks, pedagogy |
| `plan/roadmap/TRACK-switch.md` | The 🎯 interview-fundamentals subset in teaching order, with scopes + the deferred list |
| `plan/PLAN.md` | Mentor strategy: why each phase, reading plan, overlap map vs System Design/LLD, company calibration, traps, forecast |
| `progress/` | `STATUS.md` (active track + what's next), `tracker.md` (generated), `profile.md`, `review-queue.md`, `weak-areas.md` |
| `reference/` | Learner-built: `glossary.md`, `numbers.md`, `interview-bank.md`, `concept-maps/` |
| `lessons/phase-N/` | One note per lesson (the standalone record of your discovery) |
| `labs/<ID>-slug/` | Your lab code + reports (build with `tools/run.sh`) |
| `vivas/`, `reviews/` | Viva reviews & the sealed baseline & whole-stack traces; cycle/phase/monthly reviews |
| `templates/` | Lesson note, lab report, viva review, weekly review |
| `tools/` | `run.sh` + `_flags.sh` (checked C/C++ builds), `gen_tracker.py` (`--summary`, `--forecast`) |
| `.claude/` | Skills (session commands), the SessionStart hook, settings |
| `CLAUDE.md`, `DECISIONS.md` | How Claude behaves; the decision log |

## 📚 Scope at a glance

**16 phases · 362 sessions · ~1,505 h full course · ~62 h switch track.** Primary texts: CS:APP, OSTEP,
Kurose & Ross, TCP/IP Illustrated, Silberschatz + CMU 15-445, Database Internals, Crafting Interpreters,
Engineering a Compiler, Serious Cryptography, Sipser (full list in [`plan/PLAN.md`](plan/PLAN.md) §3).
Regenerate the numbers any time with `python3 tools/gen_tracker.py --forecast`.

**Deepens, never duplicates,** the System Design and LLD courses: this is the *mechanism* under their *design*.
Every phase cross-references the relevant System Design sessions.
