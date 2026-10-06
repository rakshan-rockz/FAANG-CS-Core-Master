#!/usr/bin/env python3
"""Regenerate progress/tracker.md from plan/roadmap/phase-*.md.

Preserves Status / Conf / Last touched (concept/lab/trace rows), Score / Date (vivas & baseline)
and gate progress for IDs that still exist, so it is safe to re-run after editing the roadmap.

Usage:
  python3 tools/gen_tracker.py            regenerate the tracker
  python3 tools/gen_tracker.py --summary  one-line summary (used by the SessionStart hook)
  python3 tools/gen_tracker.py --forecast print the effort forecast by session type
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKER = os.path.join(ROOT, "progress", "tracker.md")

# session types
CONCEPT = ("L", "DD", "C")          # mastery-tracked (⬜/🟨/✅)
DOING = ("WE", "LAB", "TR")         # done/not-done, own status
VIVA = ("V", "Baseline")            # scored
OTHER = ("Q", "R", "Intake", "Gate")  # counted, not individually tracked
ID_RE = re.compile(r"^\d+\.\d+\.\d+$")
STATUSES = ("⬜", "🔄", "✅")

# forecast durations (hours) per session; reading is added separately at 2h/unit + 20% overhead
DUR = {"L": 1.25, "DD": 1.5, "C": 1.25, "WE": 1.25, "LAB": 2.5, "TR": 1.25,
       "V": 1.25, "Q": 0.5, "R": 1.0, "Gate": 3.0, "Intake": 1.5, "Baseline": 1.5}
READING_UNIT_H = 2.0
OVERHEAD = 0.20


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def title_of(typ, txt):
    if typ in ("Intake", "Baseline", "Q", "R"):
        m = re.search(r"\*\*(.+?)\*\*", txt)
        return (m.group(1) if m else txt.split(" — ")[0].split("(")[0]).strip()[:70]
    m = re.search(r"\*\*(.+?)\*\*", txt)
    if m:
        return m.group(1).strip()[:70]
    return re.split(r" — |: |·", txt, 1)[0].strip()[:70]


def reading_units(txt):
    """Count scheduled reading units: ';'-separated items in the Reading: field (— = none)."""
    m = re.search(r"·\s*Reading:\s*(.+?)(?:·\s*Xref:|·\s*File:|$)", txt)
    if not m:
        return 0
    body = m.group(1).strip().rstrip("·").strip()
    if body in ("", "—", "-"):
        return 0
    return len([u for u in body.split(";") if u.strip() and u.strip() not in ("—", "-")])


# ---- previous progress -------------------------------------------------------------------------
old, old_viva, old_gate = {}, {}, {}
if os.path.exists(TRACKER):
    for line in open(TRACKER, encoding="utf-8"):
        c = cells(line)
        if len(c) == 6 and ID_RE.match(c[0]):
            old[c[0]] = c[3:6]
        elif len(c) == 5 and ID_RE.match(c[0]):
            old_viva[c[0]] = c[3:5]
        elif len(c) == 4 and re.match(r"^Gate \d+$", c[0]):
            old_gate[c[0]] = c[1:4]

# ---- parse roadmap -----------------------------------------------------------------------------
phases, rows, vivas, counts, reading = [], [], [], {}, 0
for f in sorted(glob.glob(os.path.join(ROOT, "plan", "roadmap", "phase-*.md"))):
    ph = int(re.search(r"phase-(\d+)", f).group(1))
    title = open(f, encoding="utf-8").readline().strip("# \n")
    phases.append((ph, title))
    rows.append(("H", title))
    for line in open(f, encoding="utf-8"):
        c = cells(line)
        if len(c) < 3 or not ID_RE.match(c[0]):
            continue
        sid, typ, txt = c[0], c[1], " | ".join(c[2:])
        counts[typ] = counts.get(typ, 0) + 1
        reading += reading_units(txt)
        if typ in CONCEPT or typ in DOING:
            rows.append((sid, typ, title_of(typ, txt)))
        elif typ in VIVA:
            vivas.append((sid, typ, title_of(typ, txt)))

# gates: one per phase file that has a "## Gate N"
gate_phases = []
for f in sorted(glob.glob(os.path.join(ROOT, "plan", "roadmap", "phase-*.md"))):
    ph = int(re.search(r"phase-(\d+)", f).group(1))
    if re.search(r"^## Gate ", open(f, encoding="utf-8").read(), re.M):
        gate_phases.append(ph)


def status_of(sid):
    return old.get(sid, ("⬜", "", ""))[0]


concept_ids = [r[0] for r in rows if r[0] != "H" and r[1] in CONCEPT]
doing_ids = [r[0] for r in rows if r[0] != "H" and r[1] in DOING]
mastered = sum(status_of(i) == "✅" for i in concept_ids)
started = sum(status_of(i) == "🔄" for i in concept_ids)
labs_done = sum(status_of(i) == "✅" for i in doing_ids)
gates_passed = sum(1 for g in gate_phases if old_gate.get(f"Gate {g}", ("⬜",))[0] == "✅")

# ---- forecast ----------------------------------------------------------------------------------
def forecast():
    c = dict(counts)
    c["Gate"] = len(gate_phases)          # gates have no ID row; add them here
    total_sessions = sum(c.get(t, 0) for t in c)
    session_h = sum(DUR.get(t, 0) * n for t, n in c.items())
    reading_h = reading * READING_UNIT_H
    total = (session_h + reading_h) * (1 + OVERHEAD)
    return total_sessions, session_h, reading_h, total


if "--forecast" in sys.argv:
    ts, sh, rh, total = forecast()
    print("Session counts by type:")
    fc = dict(counts); fc["Gate"] = len(gate_phases)
    for t in ("Intake", "Baseline", "L", "DD", "C", "WE", "LAB", "TR", "V", "Q", "R", "Gate"):
        if fc.get(t):
            print(f"  {t:9} {fc[t]:3}  ({DUR.get(t,0)} h each)")
    print(f"Total sessions: {ts}")
    print(f"Session hours: {sh:.1f} h")
    print(f"Reading units: {reading}  -> {rh:.1f} h (2 h/unit)")
    print(f"Subtotal: {sh + rh:.1f} h  +20% overhead  =>  {total:.0f} h full course")
    sys.exit(0)

if "--summary" in sys.argv:
    _, _, _, total = forecast()
    print(f"Concepts ✅ {mastered} · 🔄 {started} · of {len(concept_ids)} | "
          f"Labs/traces done {labs_done}/{len(doing_ids)} | Gates {gates_passed}/{len(gate_phases)} | "
          f"~{total:.0f} h full course")
    sys.exit(0)

# ---- write -------------------------------------------------------------------------------------
_, sh, rh, total = forecast()
out = ["# Curriculum Tracker", "",
       "Generated by `tools/gen_tracker.py` from `plan/roadmap/` (re-run after edits; progress is preserved).",
       "Concept status: ⬜ not started · 🔄 in progress · ✅ mastered (recognition + understanding + "
       "construction + adaptation + retention). Labs/traces: ⬜/🔄/✅. Conf 1–5.", "",
       f"**Concepts (L/DD/C):** ✅ {mastered} · 🔄 {started} · total {len(concept_ids)}  ",
       f"**Labs & traces (LAB/TR/WE):** ✅ {labs_done} · total {len(doing_ids)}  ",
       f"**Gates:** {gates_passed} / {len(gate_phases)}  ",
       f"**Forecast:** ~{total:.0f} h full course (sessions {sh:.0f} h + reading {rh:.0f} h + 20%)", ""]

for r in rows:
    if r[0] == "H":
        out += ["", f"## {r[1]}", "", "| ID | Type | Topic | Status | Conf | Last touched |",
                "|---|---|---|---|---|---|"]
    else:
        st, cf, lt = old.get(r[0], ("⬜", "", ""))
        out.append(f"| {r[0]} | {r[1]} | {r[2]} | {st} | {cf} | {lt} |")
# drop headers with no rows
clean, i = [], 0
while i < len(out):
    if out[i].startswith("## ") and (i + 4 >= len(out) or not out[i + 4].startswith("| ")):
        i += 4
        continue
    clean.append(out[i]); i += 1
out = clean

out += ["", "## Vivas & baseline", "", "| ID | Type | Session | Score /100 | Date |",
        "|---|---|---|---|---|"]
for sid, typ, t in vivas:
    sc, dt = old_viva.get(sid, ("", ""))
    out.append(f"| {sid} | {typ} | {t} | {sc} | {dt} |")

out += ["", "## Gates", "", "| Gate | Status | Attempts | Passed on |", "|---|---|---|---|"]
for g in gate_phases:
    st, at, po = old_gate.get(f"Gate {g}", ("⬜", "", ""))
    out.append(f"| Gate {g} | {st} | {at} | {po} |")

open(TRACKER, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"{len(phases)} phases, {len(concept_ids)} concepts, {len(doing_ids)} labs/traces, "
      f"{len(vivas)} vivas, {len(gate_phases)} gates, {reading} reading units -> {TRACKER}")
