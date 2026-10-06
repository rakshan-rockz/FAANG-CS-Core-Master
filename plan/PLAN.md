# Mentor's Plan — CS Core Programme

> `README.md` = the charter (what & why). `CLAUDE.md` = the mentorship contract + how sessions run.
> This file = the mentor's strategy: why this shape, the reading plan, the overlap map with the sibling
> courses, company calibration, the traps, the risks, and the scale/forecast.
> `plan/roadmap/` = the full mastery-gated sequence `/today` follows.

**Guiding decisions:** (1) *progress over timeline* — nothing is cut or compressed to hit a date; advance by
passing gates. (2) *mechanism over memorisation* — a topic is learned when the learner can derive it from the
layer below and predict changes, not when they can recite a definition. (3) *two tracks, one roadmap* — a
~60 h switch subset for the interview, then the full depth track, nothing deleted.

---

## 1. Why this course, and why in this shape

The learner is a strong engineer targeting a 22 → 30–35 LPA switch within ~12 months at product companies whose
loops include **CS-fundamentals rounds (OS, DBMS, CN, OOP) and SQL rounds**, and who wants CS core **in depth**
for its own sake beyond the switch. Two goals, one course, served by two tracks over the same material.

The **organising principle is the machine bottom-up**: bits → CPU & caches → linking/processes → OS (CPU,
memory, concurrency, persistence) → networks → databases → languages/compilers → security → theory. This order
is not arbitrary: every mechanism is explained using the layer beneath it, so nothing is taught as a recipe.
A page fault is explained with the MMU and the disk; a database buffer pool with the page cache and B+ trees;
TLS with the public-key maths; NP-hardness with reductions. Depth without this ordering becomes trivia.

**Pedagogy** (full table in `plan/roadmap/README.md` §11): prediction-before-explanation, productive failure,
guided discovery via a hint ladder, worked examples that fade, retrieval practice, spaced repetition,
interleaving, mastery gates with remediation, and hands-on labs that make the abstract measurable. The learner
builds their own references (glossary, numbers, interview bank, concept maps) because generation beats reading.

## 2. What makes this different from a "fundamentals" cram

| Common approach | This course |
|---|---|
| Memorise definitions ("thrashing is when the system pages excessively") | Derive from the mechanism (working set > RAM → fault rate → disk-bound → collapse) and *reproduce it in a lab* |
| Read the answer to "process vs thread" | Predict, then fill the shared/private table from `clone` flags, and answer at 30 s / 2 min / 5-min depth |
| Trust the latency table | Derive the numbers from physics and *measure them on this laptop* (the memory mountain, fsync, context switch) |
| Stop at "an index makes it faster" | Build a B+ tree, compute its height, and enumerate the 5 cases where an index hurts |
| Treat crypto as a black box | Build and break (defensively) the primitives; go to ML-KEM/QKD depth for the QNu résumé |
| SQL = a few joins | Two timed problem sets of the classics (windows, recursion, gaps-and-islands) with adversarial data |

## 3. Reading plan (the exact texts, mapped to phases)

Each phase file's rows cite exact chapters; this is the map. Reading is budgeted at ~2 h per unit in the forecast.

| Phase | Primary text(s) |
|---|---|
| 0 Kickoff | CS:APP 1 |
| 1 Data representation & machine code | CS:APP 2–3; Goldberg 1991 (floating point); Aleph One 1996 (stack) |
| 2 Processor & memory hierarchy | CS:APP 4–6; Drepper 2007 (memory); *A Primer on Memory Consistency and Cache Coherence* |
| 3 Linking, loading, ECF | CS:APP 7, 8, 10; Levine *Linkers and Loaders*; Drepper *How To Write Shared Libraries*; TLPI 3, 20–22 |
| 4 OS: CPU virtualisation | OSTEP 4–10; Waldspurger & Weihl 1994 (lottery) |
| 5 OS: memory virtualisation | OSTEP 13–23; CS:APP 9 |
| 6 OS: concurrency | OSTEP 26–33; Drepper 2011 (futexes); Boehm 2005; Williams *C++ Concurrency in Action* 5 |
| 7 OS: persistence & Linux | OSTEP 36–45, 48–49; McKusick 1984 (FFS); Rosenblum 1992 (LFS); Pillai 2014; Axboe 2019 (io_uring); Bovet & Cesati 12, 14 |
| 8 Networks I | K&R 1–3; TCP/IP Illustrated Vol 1 ch 10–17; RFC 9293 (TCP), RFC 9000 (QUIC); Jacobson 1988; Cardwell 2016 (BBR) |
| 9 Networks II | K&R 4–7; TCP/IP Illustrated Vol 1 ch 2–8 |
| 10 Databases I | CMU 15-445 #01–02; Silberschatz 7e ch 2–7; Codd 1970 |
| 11 Databases II | CMU 15-445 #03–23; Petrov *Database Internals* 1–7, 13; Mohan 1992 (ARIES); Berenson 1995; Cahill 2008; Selinger 1979; Leis 2015; O'Neil 1996; Crotty 2022 |
| 12 Languages & compilers | Lippman *Inside the C++ Object Model*; Itanium C++ ABI; *The GC Handbook* 2e; Nystrom *Crafting Interpreters*; Cooper & Torczon *Engineering a Compiler* 3e; Dragon ch 4 |
| 13 Security & cryptography | Aumasson *Serious Cryptography* 2e 1–14; K&R 8; RFC 8446 (TLS 1.3); FIPS 197/203/204/205; NIST IR 8547; Bennett & Brassard 1984 (BB84) |
| 14 Theory | Sipser *Introduction to the Theory of Computation* 3e ch 0–5, 7–8, 10 |
| 15 Interview mastery | none new — retrieval and performance |

CMU 15-445 lectures are cited by number + title; if the numbering shifts between semesters, titles are
authoritative. Books are the backbone; papers/RFCs/FIPS are read in the rows that cite them.

## 4. Overlap & dedup map vs the System Design course

This course **deepens** SD, never repeats it. Where both touch a topic, this course provides the mechanism SD
uses as a black box. Rows carry `Xref: SD n.n.n`; each phase file has an SD overlap map. Highlights:

| Topic | SD covers (design level) | This course adds (mechanism) |
|---|---|---|
| The single machine | SD 0.3 (CPU/threads, hierarchy, latency numbers, event loops) | Phases 1–7: derive every number; caches/coherence; scheduler, VM, concurrency, fs internals |
| Networking | SD 1.1–1.3 (IP/CIDR, DNS, TCP flow/congestion, LB, CDN) | Phases 8–9: headers on the wire, state machines, rdt derivation, routing algorithms, subnetting, sockets/epoll servers |
| Databases | SD 2.x (indexes, isolation, replication, sharding, NoSQL) | Phases 10–11: B+ tree/LSM internals, query optimisation, 2PL/MVCC/SSI proofs, WAL/ARIES, build labs |
| Security | SD 1.2.3, 8.3–8.4 (TLS, auth, KMS, OWASP, STRIDE) | Phase 13: the cryptography itself, TLS 1.3 message-by-message, PQC/QKD depth |
| Storage/durability | SD 0.2.5, 2.3.1 (WAL, fsync, durability) | Phase 7: journaling, the fsync truth, the write-to-NAND trace; Phase 11: ARIES |

**Switch-track dedup:** the switch track (`TRACK-switch.md`) skips what SD's switch track already teaches at
interview level (CAP, DNS, HTTP, caching, LB, replication/sharding at design level) and adds the one extra layer
of mechanism where fundamentals rounds probe it (how TCP is actually reliable → 8.3.2; how an index physically
works → 11.2.2).

**LLD:** owns OOP design (SOLID, patterns); this course owns OOP interview theory + the C++ object model.
**DSA:** owns algorithm technique and C++ coding pitfalls; this course's Phase 14 is theory of computation.

## 5. Company calibration (refined after intake)

- **Microsoft:** OS internals and C++ depth, debugging-flavoured ("here's a symptom, find the cause"); strong on
  memory, pointers, concurrency.
- **Amazon:** practical framing ("how does this break in production", "how does it scale"), DBMS + networking +
  OS, plus Leadership Principles alongside the technical.
- **Google:** one topic followed to bedrock; values the reasoning path and optimality; expect "why?" until the
  hardware.
- **Uber / Atlassian:** applied and extensible; realistic twists; trade-offs.
- **Adobe / Oracle / Flipkart & Indian product companies:** a dedicated **core-subjects round** — rapid
  OS/DBMS/CN/OOP breadth + **SQL on paper** + **numericals** (scheduling Gantt, page faults/EAT, subnetting,
  normalisation, serializability). Phase 15.3.5 rehearses exactly this format; the numericals are drilled in the
  `WE` sessions throughout.
- **QNu-relevant:** the résumé lists PQC/QKD; interviewers will probe it. Phase 13.6 and the 15.2.9/13.6.7 vivas
  train a credible, non-over-claiming answer.

## 6. Traps called out by name (roadmap §14)

Definition without mechanism · process vs thread blur · "TCP is reliable so no app acks" · "indexes always
help" · "volatile makes it thread-safe" · layer skipping (URL → server with no DNS/TCP/TLS/routing) · Big-O as
performance · magic numbers (quoting latencies with no reason) · "encryption = security" · "quantum breaks all
crypto" (Shor vs Grover) · "NP-hard = impossible" · memorised interview answers (collapse at the first "why?") ·
durability by assumption ("it's written" when it's in the page cache).

## 7. Retention & interview realism

- Every session opens with due spaced reviews (+2/+7/+21/+60) before new material.
- Explain-back (2 min, own words, graded) ends every lesson and feeds the interview bank.
- Labs force *predict → measure → explain*, so numbers are earned, not memorised.
- Vivas are cold, scored /100, company-styled, and interleave earlier phases; a bluff is penalised harder than
  an honest "I don't know, but here's how I'd reason."
- The sealed baseline (0.0.2) is redone identically at 15.3.6 to measure the whole course's growth per subject.
- Numericals (scheduling, EAT, subnetting, normalisation, query cost, serializability, banker's) are drilled in
  `WE` sessions because Indian product companies ask them on paper.

## 8. Scale & forecast (§Scale)

Regenerate with `python3 tools/gen_tracker.py --forecast`. As built:

| Session type | Count | Hours each |
|---|---:|---:|
| Intake | 1 | 1.5 |
| Baseline (sealed + redo) | 2 | 1.5 |
| L (learn) | 122 | 1.25 |
| DD (deep dive) | 74 | 1.5 |
| C (compare) | 9 | 1.25 |
| WE (worked example) | 10 | 1.25 |
| LAB (hands-on) | 43 | 2.5 |
| TR (trace) | 7 | 1.25 |
| V (viva) | 23 | 1.25 |
| Q (quiz) | 3 | 0.5 |
| R (review) | 52 | 1.0 |
| Gate | 16 | 3.0 |
| **Total sessions** | **362** | |

Session hours ≈ 538 h; scheduled reading ≈ 358 units × 2 h = 716 h; +20% overhead ⇒ **≈ 1,505 h full course**.
The **switch track** is ~37 rows, **≈ 62 h** (≈ 57 h sessions + ~5 h targeted reading), budgeted at 60 h — the
interview-fundamentals path to the switch, after which the depth track continues, nothing deleted.

This is a large, deliberately deep programme (well over a year at a steady pace). That is the point: the switch
is reachable in the first ~60 h, and genuine CS-core mastery follows over time. If a real interview date lands
early, add more vivas and SQL rounds alongside the switch track — never cut lessons.

## 9. Risks

| Risk | Mitigation |
|---|---|
| The depth track's size is daunting | The switch track delivers the interview payoff in ~60 h; progress is visible per gate; nothing is ever "behind" |
| Passive reading instead of doing | Every lesson predicts-then-explains; 43 labs; vivas are cold and scored |
| Forgetting early phases by the later ones | Spaced reviews + interleaved vivas + the baseline redo |
| Missing tools (no perf/libasan on this box) | `tools/_flags.sh` auto-detects; labs offer install lines and valgrind/cachegrind fallbacks |
| Over-claiming on the PQC/QKD résumé | 13.6 + résumé-defence vivas train an honest, mechanism-level answer |
| AI-only feedback blind spots | Strict rubric, sealed baseline comparison, honest bluff-penalising; suggest peer mocks near a real date |
