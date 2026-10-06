# Roadmap — Mechanism-First, Mastery-Gated, No Dates

**Principle:** you advance by what you can *explain from the mechanism, predict and measure*, not by what
you have read. Nothing is cut or skimmed. Two tracks run over the **same** session rows: the 🎯 switch
track (`TRACK-switch.md`, interview fundamentals first) and the depth track (every row, in order).

> **Motto:** *Don't memorise definitions. Predict the machine, then measure it.*
> A topic is not "done" when it has been explained to you. It is done when you can explain *why* it
> works from the layer below, predict what happens when a parameter changes, and survive an
> interviewer's third follow-up.

---

## 1. Structure

```text
Phase  →  Cycles  →  Sessions  →  Gate
```

- **Phase** = one area of CS core (0 Kickoff … 15 Interview mastery). Phases follow the layers of the
  machine bottom-up (bits → CPU → linking → OS → networks → databases → languages → security → theory),
  so every mechanism is explained using the layer beneath it.
- **Cycle** = 3–10 sessions on one sub-area, closed by a review (`R`). Most phase-final cycles contain a
  viva (`V`) before the review.
- **Session** = one sitting (durations in §3). Unfinished sessions **continue** next sitting.
- **Gate** = the end-of-phase exit test (checklist at the bottom of each phase file). Pass = every criterion
  met, cold. Fail = a remediation cycle, then retry the failed criteria. Unlimited attempts, no penalty.

## 2. Session IDs and row format

`<phase>.<cycle>.<n>`, e.g. `5.1.4` = Phase 5, Cycle 1, session 4. `progress/STATUS.md` holds the next ID
and the active track; `/today` resumes from it. IDs never change once a session has been run.

Every phase file uses exactly this table shape (parsed by `tools/gen_tracker.py`; **never put a literal
pipe character inside a cell**, write "pipe" or `∣` instead):

```markdown
| ID | Type | Session |
|---|---|---|
| 4.2.1 | L | **Scheduling I: FIFO, SJF, STCF, RR** 🎯 — Hook: … · Derive: … · Covers: … · Probe: … · Anchors: … · Traps: … · Reading: OSTEP 7 "Scheduling: Introduction" · File: `lessons/phase-04/4.2.1-scheduling-basics.md` |
```

`🎯` after the title = the row is on the switch track (the scope is in `TRACK-switch.md`).

### Fields by session type (in this order; all required unless marked optional)

| Type | Fields |
|---|---|
| `L` `DD` `C` | **Title** — **Hook** (a concrete puzzle or real observation, stated without naming the mechanism) · **Derive** (naive model → where it fails → the real mechanism; what the hint ladder steers toward) · **Covers** (every sub-point; none may be dropped) · **Probe** (3–5 interviewer follow-ups / adaptations that test Level 4) · **Anchors** (the exercise, lab link or classic interview question that proves it) · **Traps** (optional: misconceptions called out by name) · **Reading** · **Xref** (optional: sibling-course sessions this deepens or relies on) · **File** |
| `WE` | **Title** — **Hook** · **Model** (what the mentor solves out loud, naming each move) · **Sibling** (the problems the learner then solves alone) · **Reading** · **File** |
| `LAB` | **Title** — **Hook** · **Predict** (what the learner must predict, in numbers where possible, *before* running) · **Build/Run** (what the learner writes or runs; Claude gives setup, never the solution code) · **Measure** (what to record) · **Explain** (the mechanism the result must be explained with) · **Probe** · **Reading** · **File** (`labs/<ID>-slug/`) |
| `TR` | **Title** — **Hook** · **Path** (every layer the trace must pass through, in order) · **Covers** · **Probe** · **Reading** · **File** |
| `V` | **Title** — **Scope** (phases/topics) · **Format** (rapid-fire count, deep questions, time) · **Bank** (question areas that must appear) · **File** (`vivas/YYYY-MM-DD-<ID>-slug.md`) |
| `Intake` `Baseline` `Q` `R` | Free text (what the session does and what it writes) |

### Reading field

`Reading:` lists **scheduled reading units** separated by `;`. One unit = one book chapter (or a
contiguous section range of a long chapter), one lecture, one paper or one RFC section, and is budgeted at
**≈ 2 h** in the forecast. Optional material goes in `Extra:` inside Covers or Probe and is not budgeted.
Citation keys:

| Key | Source |
|---|---|
| `CS:APP` | Bryant & O'Hallaron, *Computer Systems: A Programmer's Perspective*, 3rd ed. (chapter.section) |
| `OSTEP` | Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (v1.10 chapter numbers + title) |
| `K&R` | Kurose & Ross, *Computer Networking: A Top-Down Approach*, 8th ed. (chapter.section) |
| `TCPIP` | Fall & Stevens, *TCP/IP Illustrated, Vol. 1*, 2nd ed. (chapter) |
| `DBI` | Petrov, *Database Internals* (chapter) |
| `CMU` | CMU 15-445/645 *Database Systems*, Fall 2023 lecture number + title (titles are authoritative if numbering shifts between semesters) |
| `CI` | Nystrom, *Crafting Interpreters* (chapter) |
| `SC` | Aumasson, *Serious Cryptography*, 2nd ed. (chapter) |
| `SIP` | Sipser, *Introduction to the Theory of Computation*, 3rd ed. (chapter.section) |
| others | cited in full the first time (papers, RFCs, FIPS standards, *Engineering a Compiler*, *The Garbage Collection Handbook*, *A Primer on Memory Consistency and Cache Coherence*, TLPI) |

## 3. Session types

| Type | Name | Skill | Budget | What happens |
|---|---|---|---:|---|
| `Intake` | Intake | `/intake` | 1.5 h | Profile: targets, companies, timeline context, background, C/C++ fluency, what's known cold, tools installed |
| `Baseline` | Baseline CS viva | `/viva baseline` | 1.5 h | Cold 45-min rapid-fire across OS/DBMS/CN/OOP/architecture/security + one deep "type a URL and press enter" (15 min). Zero hints, **sealed**. Redone identically at 15.3.6 |
| `L` | Learn | `/lesson learn` | 1.25 h | The Mechanism Protocol (§5) |
| `DD` | Deep dive | `/lesson deep-dive` | 1.5 h | Straight to the mechanism: edge cases, magnitudes, real implementations (Linux, Postgres, glibc, LLVM), what breaks |
| `C` | Compare | `/lesson compare` | 1.25 h | Two or more alternatives; the learner builds the comparison table; 3 "which would you pick and why?" scenarios |
| `WE` | Worked example | `/lesson we` | 1.25 h | Mentor solves problems out loud (numerical problems, derivations, proofs), naming each move; learner annotates, then solves siblings alone |
| `LAB` | Lab | `/lab` | 2.5 h | **Predict → run → measure → explain.** The learner writes the code / runs the commands; Claude gives setup, interprets output, never writes the learner's solution |
| `TR` | Trace | `/trace` | 1.25 h | Follow one event through every layer (keypress → syscall → packet → server → disk). The learner narrates each hop; Claude asks "what happens next, and who does it?" |
| `V` | Viva | `/viva` | 1.25 h | Interview-style rapid-fire fundamentals mock + 1–2 deep follow-up chains, scored /100 (§8) |
| `Q` | Quiz | `/quiz` | 0.5 h | Retrieval practice weighted to due reviews and weak areas |
| `R` | Review | `/weekly-review` | 1 h | Cycle review: explain without notes, re-test weak areas, concept map; inserts repeat sessions if needed |
| `Gate` | Phase gate | `/gate` | 3 h | Calibration → concept map → cold test of every criterion → pass or remediation |

Reading is budgeted separately at ≈ 2 h per scheduled unit; the forecast adds 20% overhead
(`python3 tools/gen_tracker.py --forecast`).

## 4. The mastery bar (the Four Levels, adapted to CS core)

A concept row becomes ✅ in `progress/tracker.md` only when **all five** hold. Until then it is 🟨.

| Level | Test | Where it's tested |
|---|---|---|
| 1. **Recognition** | Given a symptom or a question in unfamiliar words, names the mechanism involved ("this is a TLB-reach problem", "that's write skew") and why the nearest alternative isn't it | `Q`, `V`, gates |
| 2. **Understanding** | 2-minute explain-back *from the layer below*: what problem, how it works, what it costs, when it fails | end of `L`/`DD`/`C`, `R` |
| 3. **Construction** | Re-derives the mechanism from the Hook cold (why TCP needs 3 messages, why 2PL gives serializability, why two's complement makes subtraction free) | derive-back in `R`/gate |
| 4. **Adaptation** | Predicts the effect of a changed parameter and survives 3+ follow-ups ("and if the page size doubles?", "what if the ACK is lost?") | `Probe` step, `LAB` predictions, `V` |
| + **Retention** | Passes the +21-day spaced review | review queue |

`LAB` rows are ✅ when the learner's prediction, measurement and mechanistic explanation are all recorded
and the explanation is correct. `V` rows record a score, not a status.

## 5. The Mechanism Protocol (how every `L`/`DD`/`C` session runs)

One step per turn, ≤ ~25 lines, ending with a question. The learner acts first at every step that can be
reasoned out.

1. **Retrieval warm-up**: due reviews; one question linking to the previous session.
2. **Hook**: state the puzzle/observation. **Do not name the mechanism.**
3. **Predict**: "What do you think happens, and why?" The learner commits to a prediction (a number when
   possible). Wrong predictions are the most valuable data in the session; they get recorded.
4. **Naive model**: the learner states the simplest model that would explain the Hook. Claude finds the
   input/case where it fails (a **counterexample**, not a correction).
5. **Derive the mechanism**: guided by the hint ladder (§6) toward the row's **Derive** chain. The learner
   builds the mechanism; Claude asks "who does this step: hardware, kernel, library, or you?"
6. **Name it**: only now the standard term, its history, and where it lives in real systems (Linux,
   glibc, Postgres, Chrome, OpenSSL…).
7. **Covers**: every sub-point in the row, in short chunks, each followed by a check question.
8. **Magnitudes**: every claim gets a number with a reason (ns, bytes, pages, RTTs). The learner estimates
   first. Feeds `reference/numbers.md`.
9. **Probe**: the row's follow-ups, one at a time, in interviewer voice.
10. **Position it**: when it's the wrong tool / where it breaks; comparison table vs the nearest
    alternative (learner fills first).
11. **Explain-back**: the learner's 2-minute interview answer (voice encouraged). Graded precise / missing
    / wrong. The best version goes into `reference/interview-bank.md` (learner writes, Claude verifies).
12. **Record**: Claude writes the lesson note (`templates/lesson-note.md`) including the learner's
    predictions, wrong turns and explain-back.

## 6. The hint ladder

"I'm stuck" never gets the answer. It gets the **next rung**, and the rung used is recorded.

| Rung | Gives | Example ("why does `fork()` return twice?") |
|---|---|---|
| **H0** Metacognitive nudge | a question about the process | "After the call, how many processes exist? Which one is executing the return?" |
| **H1** Layer pointer | which layer / which resource to think about | "Think about what the kernel copies when it creates the child." |
| **H2** Observation | one specific fact | "The child gets a copy of the parent's registers, including the one holding the return value." |
| **H3** Structure | the mechanism's skeleton | "Kernel duplicates the task: same saved PC, but it writes 0 into the child's return register and the child's PID into the parent's." |
| **H4** Walkthrough | the full explanation (the learner still explains it back) | Full `fork` walkthrough, incl. COW |

**Scoring by the highest rung:** H0–H1 = independent · H2–H3 = with hints → the concept's first spaced
review moves to +1 day · H4 = not yet understood → a repeat derive-back is scheduled in the next session.
"Just tell me" = one rung up; the full answer only if asked again.

## 7. Retention machinery

- **Spaced review queue** (`progress/review-queue.md`): every row reaching 🟨 gets reviews at
  **+2 / +7 / +21 / +60 days**. A review = cold derive-back from the Hook in ≤ 5 min + one Probe. A failed
  review resets to +2 and opens a weak area.
- **Interleaving**: `Q` and `V` sessions always mix in earlier phases; vivas never stay in one subject.
- **Learner-built references** (the learner writes, Claude verifies; generation effect):
  `reference/glossary.md` (terms defined by mechanism, not by synonym), `reference/numbers.md`
  (latencies, sizes, limits, with the reason for each), `reference/interview-bank.md` (the learner's own
  answers to classic fundamentals questions, verified and graded), `reference/concept-maps/`
  (one map per phase, drawn at the gate).
- **Weak-area loop**: every wrong answer is logged verbatim with the correct mechanism and resurfaced until
  answered correctly twice in later sessions.
- **Spiral**: key mechanisms return deliberately at increasing depth, e.g. the stack (1.3 → 3.2 → 12.2),
  caches (2.2 → 5.1 TLB → 11.1 buffer pool), logs (7.2 journaling → 11.5 WAL/ARIES → SD replication),
  state machines (8.3 TCP → 14.1 DFAs), trust (13.3 PKI → 13.4 TLS → 13.6 PQC migration).

## 8. Viva rubric (/100)

| Category | /pts | Full marks |
|---|---:|---|
| Accuracy | 25 | No false statements; corrects itself when unsure rather than bluffing |
| Depth / mechanism | 25 | Explains *how* and *why* from the layer below, not just *what* |
| Precision of terms | 10 | Uses terms exactly (process vs thread, latency vs throughput, serializable vs linearizable) |
| Connecting layers | 15 | Links the answer to adjacent layers unprompted (page fault ↔ disk ↔ scheduler) |
| Trade-offs | 15 | Names costs, alternatives and when the answer changes |
| Communication | 10 | Structured (definition → mechanism → example → trade-off), concise, checks understanding |

Bands: **< 50** No hire · **50–64** Lean no · **65–79** Lean hire · **80–89** Hire · **90+** Strong hire.
A bluffed answer costs more than "I don't know, but here's how I'd reason about it" (Accuracy + Communication).

## 9. The route

| Phase | Title | Cycles | Why here | Core reading |
|---:|---|---|---|---|
| 0 | Kickoff & the stack of abstractions | 0.0–0.1 | Intake, sealed baseline, and the map of every layer the course will open | CS:APP 1 |
| 1 | Data representation & machine-level programming | 1.1–1.3 | Everything above is bits; C/C++ overflow, FP and stack bugs come from here | CS:APP 2–3 |
| 2 | Processor & memory hierarchy | 2.1–2.4 | Performance intuition, caches, coherence; needed for OS, DB buffer pools, concurrency | CS:APP 4–6, 5 |
| 3 | Linking, loading & exceptional control flow | 3.1–3.3 | How a program becomes a process; fork/exec/signals/syscalls before the OS proper | CS:APP 7, 8, 10 |
| 4 | OS: CPU virtualisation | 4.1–4.2 | Processes, LDE, context switches, scheduling | OSTEP 4–10 |
| 5 | OS: memory virtualisation | 5.1–5.3 | Paging, TLBs, replacement, allocators, mmap/COW | OSTEP 13–23, CS:APP 9 |
| 6 | OS: concurrency | 6.1–6.4 | Locks → CVs → semaphores → deadlock → events → memory models | OSTEP 26–33 |
| 7 | OS: persistence & Linux internals | 7.1–7.3 | Devices, SSDs, file systems, crash consistency, page cache, containers, VMs | OSTEP 36–45, 48–49 |
| 8 | Networks I: application & transport | 8.1–8.3 | Top-down: HTTP/DNS on the wire, sockets, TCP in depth, QUIC | K&R 1–3, TCPIP 12–16 |
| 9 | Networks II: network & link layers | 9.1–9.3 | IP, subnetting, routing, BGP, NAT, Ethernet/ARP, wireless, packet tools | K&R 4–7 |
| 10 | Databases I: model, SQL & design | 10.1–10.3 | Relational algebra, SQL in depth, ER, FDs and normalisation | CMU 1–2 |
| 11 | Databases II: internals | 11.1–11.5 | Storage, buffer pool, B+ trees, joins, optimisation, CC, WAL/ARIES | CMU 3–23, DBI 1–7 |
| 12 | Programming languages & compilers | 12.1–12.4 | C++ object model, memory management & GC, types, compiler pipeline, interpreters/JITs | CI, *Engineering a Compiler* |
| 13 | Security & cryptography | 13.1–13.6 | Symmetric → public-key → TLS 1.3 → vulnerabilities → PQC & QKD | SC 1–14 |
| 14 | Theory of computation | 14.1–14.4 | Automata, grammars, decidability, NP-completeness: the limits every engineer hits | SIP 1–5, 7 |
| 15 | Interview mastery | 15.1–15.3 | Rapid-fire drills, SQL rounds, trace questions, company vivas, baseline redo | — |

## 10. Tracks

- **🎯 Switch track** (`TRACK-switch.md`): the interview-fundamentals subset in teaching order (≈ 60 h).
  Rows carry a `Scope`: `full`, or `switch: <what's covered now; what waits>`. A switch-scoped row is
  marked 🟨 when its switch scope is done; the rest is taught when the depth pass reaches that row.
- **Depth track**: every row in phase order. After the switch track ends, `/today` continues with the
  first roadmap row not yet ✅/🟨-complete, in order. A row taught at switch scope is re-opened at full
  scope in the depth pass (as a deep-dive on the parts that waited, not a replay).
- `progress/STATUS.md` → `**Active track:** switch` or `depth`. Nothing is ever deleted from the roadmap.

## 11. Pedagogical design

| Principle | Evidence base | Where it shows up |
|---|---|---|
| **Prediction before explanation** | Brod et al.; generative learning: committing to a prediction makes the correction stick | Protocol step 3; every `LAB` has a Predict field |
| **Productive failure** | Kapur | The Hook is attacked before the mechanism is named |
| **Guided, not pure, discovery** | Mayer (2004) | The hint ladder; the smallest nudge that unblocks |
| **Layered explanation** | Cognitive load theory; prerequisite ordering | Phases go bottom-up so each mechanism is explained by the one beneath it |
| **Worked examples → fading** | Sweller; expertise-reversal effect | `WE` rows for numerical problem families (scheduling, translation, subnetting, normalisation, banker's); scaffolding fades (§12) |
| **Retrieval practice** | Roediger & Karpicke | Explain-back, `Q`, `V`, derive-backs, gates |
| **Spaced repetition** | Ebbinghaus; Cepeda et al. | +2/+7/+21/+60 |
| **Interleaving** | Rohrer & Taylor | Mixed-subject vivas and quizzes; trace sessions cross every layer |
| **Elaborative interrogation** | Dunlosky et al. | "Who does this step, and why?"; every number gets a reason |
| **Contrast / variation** | Marton | `C` sessions and the comparison table in every lesson |
| **Concrete experience** | Kolb; labs | `LAB` sessions: measure the cache, the context switch, the fsync, the handshake |
| **Mastery learning** | Bloom | Gates with remediation; ✅ = the four levels + retention |
| **Generation effect** | Slamecka & Graf | Glossary, numbers, interview bank, concept maps are learner-written |
| **Metacognitive calibration** | Self-assessment accuracy | Predict each gate criterion before testing |
| **Desirable difficulties** | Bjork | Cold vivas, sealed baseline, unannounced earlier-phase questions |

## 12. Scaffolding fades by phase

| Phases | Lessons | Labs | Vivas |
|---|---|---|---|
| 0–3 | Hints on request at any rung; Claude offers H0 after ~3 min of silence | Setup commands given in full; checkpoints every step | Coached: one rephrase allowed per question |
| 4–9 | Hints on request only | Goal + constraints given; the learner plans the steps | Standard interviewer; hints cost Accuracy points |
| 10–15 | Max H2 before a full attempt | Goal only | Cold, company-styled |

## 13. Rules that never bend

- No skipping. "I already know this" → prove it cold (derive-back + two Probe follow-ups). Pass → the
  session becomes a harder deep-dive on the same row, not a skip.
- No mechanism name before the learner has predicted and attempted the Hook.
- Due reviews run before new material, every session.
- Every number stated gets a reason; every definition gets a mechanism.
- The learner writes lab code and reference entries; Claude verifies, never fills them in.
- Every phase ends with a review, a concept map and a gate.

## 14. Traps (called out by name when they happen)

| Trap | What it looks like |
|---|---|
| *Definition without mechanism* | "A TLB is a cache for page tables", with no idea what a miss costs or who handles it |
| *Process vs thread blur* | Saying threads have separate address spaces, or processes share heap |
| *"TCP is reliable, so no app-level acks"* | Forgetting that TCP delivery ≠ application processing; crashes after ACK |
| *"Indexes always help"* | Ignoring write cost, selectivity, the planner, and covering |
| *"volatile makes it thread-safe"* | Confusing compiler visibility with atomicity and ordering |
| *Layer skipping* | "The browser sends the request to the server", skipping DNS, TCP, TLS, routing |
| *Big-O as performance* | Ignoring constants, caches, and memory-level parallelism |
| *Magic numbers* | Quoting "L1 = 1 ns" without knowing why or when it's false |
| *"Encryption = security"* | Encrypting without integrity, authenticating the wrong party, reusing nonces |
| *"Quantum breaks all crypto"* | Not separating Shor (public-key, broken) from Grover (symmetric, halved security) |
| *"NP-hard = impossible"* | Not knowing approximations, special cases, solvers, parameterised algorithms |
| *Memorised interview answers* | Fluent first sentence, collapse at the first "why?" |
| *Durability by assumption* | "It's written" when it's only in the page cache |

## 15. Phase files

`phase-00.md` … `phase-15.md` in this folder. Each has an intro (what it covers, why it sits here, what it
cross-references), its cycles and session tables, and a **Gate** checklist at the bottom.
`TRACK-switch.md` holds the 🎯 switch-track order.
