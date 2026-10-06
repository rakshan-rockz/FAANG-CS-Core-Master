# Programme Decisions Log

Everything decided about this programme and its Claude setup, in one place: what was built, why, and what's
open. Updated whenever the roadmap or setup changes.

**State as of 2026-09-25:** setup complete, programme **not started**. Active track: **switch**. Next session:
`0.0.1 Intake`.

---

## 1. How the system works (one picture)

```text
  README.md (charter: philosophy, dashboard, how to use)
        │
        ▼
  plan/PLAN.md (mentor strategy, reading plan, overlap map, forecast)
  plan/roadmap/ (Mechanism Protocol, every session in order, gates, two tracks)
        │
        ▼
  CLAUDE.md (how Claude behaves) ──► SessionStart hook prints STATUS + due reviews + forecast
        │
        ▼
  /today ─► due spaced reviews ─► next session on the ACTIVE TRACK ─► the right skill:
             /intake  /viva  /lesson  /lab  /trace  /quiz  /weekly-review  /gate  /hint
        │
        ▼
  /wrap ─► tracker · review-queue · weak-areas · STATUS · lesson note / lab report / viva review
           · glossary · numbers · interview bank · concept maps
```

## 2. Sibling repos this mirrors

Built to operate exactly like `../FAANG-System-Design-Master` (SD) and `../FAANG-DSA-Master` (DSA): the same
STATUS/tracker/profile/review-queue/weak-areas progress model, a generated tracker, a SessionStart hook,
per-session skills, mastery gates, spaced repetition, and learner-built references. Neither sibling repo was
modified. No `git init` was run.

## 3. Key decisions (with rationale)

| # | Decision | Why | Rejected alternative |
|---|---|---|---|
| D1 | **Mechanism-first, bottom-up phases** (bits → CPU → OS → net → DB → languages → security → theory) | Every mechanism is explained by the layer below; depth without this is trivia | Topic-by-topic "subjects" order |
| D2 | **Predict-before-explain** as the core protocol; every lab is predict → run → measure → explain | Generative learning; wrong predictions make the correction stick | Lecture-then-quiz |
| D3 | **Progress over timeline**; advance only by passing gates | The learner's stated value; mastery, not dates | A dated calendar |
| D4 | **Two tracks over one roadmap** (switch ~60 h, then depth); nothing deleted | Serves the 12-month switch *and* the depth goal without cutting content | Two separate courses, or cutting the deep material |
| D5 | **Session IDs `phase.cycle.n`**; `/today` resumes per the active track from STATUS | Resumable, unambiguous, trackable across a long programme | Topic names only |
| D6 | **Mastery bar = the four levels + retention**; ✅ only when all hold | "Heard it" ≠ "can derive and defend it" | Self-reported completion |
| D7 | **Phase gates** with remediation and unlimited retries | Mastery learning (Bloom) | Move on regardless |
| D8 | **43 hands-on labs** with `tools/run.sh` (checked C/C++ builds) | Numbers and mechanisms must be measured, not memorised (memory mountain, fsync, context switch, false sharing, B+ tree, WAL, TLS) | Read-only course |
| D9 | **Sealed baseline** at 0.0.2, redone identically at 15.3.6 | Objective measure of the whole course's growth per subject | No baseline |
| D10 | **Spaced review queue** (+2/+7/+21/+60) before new material | Retention across a 1,500 h programme | Review only occasionally |
| D11 | **Learner-built references** (glossary, numbers, interview bank, concept maps); Claude verifies | Generation effect; builds the learner's own interview answers | Claude-written cheat sheets |
| D12 | **Viva rubric /100** (accuracy, depth/mechanism, precision, connecting layers, trade-offs, communication); bluffs penalised | Interview realism; rewards mechanism over recitation | Pass/fail or vibes |
| D13 | **Deepen, never duplicate, SD and LLD**; `Xref` + per-phase overlap maps | The learner has SD/LLD/DSA already; this fills the mechanism gap | Re-teaching design/patterns/algorithms |
| D14 | **Phase 13 to practitioner depth on PQC/QKD** | Directly career-relevant (QNu Labs) and probed from the résumé | Treating crypto as a black box |
| D15 | **Numericals drilled in `WE` sessions** (scheduling, EAT, subnetting, normalisation, query cost, serializability, banker's) | Indian product companies ask them on paper | Concept-only |
| D16 | **Tracker generated** from the roadmap (`tools/gen_tracker.py`, progress preserved; `--summary`, `--forecast`) | Roadmap and tracker can't drift; the hook and forecast stay honest | Hand-maintained tracker |
| D17 | **Sanitizers auto-detected** in `tools/_flags.sh` (this machine lacks libasan/libubsan/libtsan; TSan opt-in) | Builds still get bounds checks + warnings; offer install lines; valgrind/cachegrind as fallback | Assuming sanitizers exist |
| D18 | **Defensive framing for all security labs** (own code / local vulnerable targets only) | Build-and-defend intent; ethics and legality | Attacking third-party systems |
| D19 | **No literal pipe characters inside roadmap table cells** | The tracker parser splits rows on `|` | Free-form tables |

## 4. Toolchain findings (2026-09-25, this machine)

- gcc/g++ 11.5, gdb, valgrind (+ cachegrind/callgrind), strace, ltrace, objdump, readelf, docker, tshark/wireshark,
  dig, ss, ip, tc, nc, unshare, cgroups v2 — present.
- **OpenSSL 3.5.5** with native **ML-KEM / ML-DSA / SLH-DSA** and the **X25519MLKEM768** hybrid group — present
  (Phase 13.6 labs use it directly).
- **Not present by default:** `perf`, `libasan`/`libubsan`/`libtsan`, `sqlite3` CLI, `psql`/`postgres` on the
  host. Mitigations: `perf` optional (cachegrind/gprof/clock_gettime fallback); SQLite via Python's built-in
  `sqlite3` (3.34: window functions + recursive CTEs OK); Postgres via `docker run postgres:16` + `docker exec psql`.
- CPU: i7-13620H, hybrid 6 P-cores (+HT) + 4 E-cores = 16 logical; L1d 48 KiB, L2 up to 2 MiB, L3 24 MiB — labs
  pin cores with `taskset` and report P vs E.
- Kernel 5.14 (RHEL9): scheduler is **CFS** (EEVDF arrived in Linux 6.6 — the roadmap notes this where relevant).

## 5. Scale (see PLAN §8; regenerate with `--forecast`)

16 phases · 362 sessions (122 L, 74 DD, 9 C, 10 WE, 43 LAB, 7 TR, 23 V, 3 Q, 52 R, 16 Gate, 1 Intake, 2 Baseline)
· 205 concept rows · 60 labs/traces · 16 gates · ~358 reading units. **≈ 1,505 h full course**; **≈ 62 h switch
track**.

## 6. Open items / needs from the learner

| Item | Status |
|---|---|
| Intake answers (companies, timeline, tools, C/C++ level, CS-subject state) | Pending: session 0.0.1 |
| Optional installs: `perf`, `libasan libubsan libtsan` | Recommended for Phases 2, 4, 6 labs; not required |
| Postgres image pulled (`docker pull postgres:16`) | Needed from Phase 10 labs |
| Git repository | Not a git repo (per instruction: no `git init`). Recommend a private repo later for history/backup |
| Peer/mock-platform interviews | Recommended near a real interview date (AI feedback has blind spots) |

## 7. Version history

| Ver | Date | What happened | Status |
|---|---|---|---|
| v1 | 2026-09-25 | Initial build: CLAUDE.md, README, PLAN, DECISIONS, roadmap README + 16 phase files, TRACK-switch, 11 skills, progress files, templates, references, tools (run.sh/_flags.sh/gen_tracker.py), hook, settings. Tracker and hook tested; forecast computed | Current |

## 8. Changing things later

Edit the relevant `plan/roadmap/phase-NN.md` (keep the table shape, no literal pipes in cells) → run
`python3 tools/gen_tracker.py` (progress preserved) → add a row to §7 here with the reason. Ask Claude:
"add X to the roadmap" follows this procedure.
