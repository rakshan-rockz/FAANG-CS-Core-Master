# Labs

The learner's hands-on work. Each lab has its own folder `labs/<ID>-slug/` with the code the learner writes,
the commands run, and a report from `templates/lab-report.md`. Build C/C++ with `tools/run.sh <file>`.
The protocol is always **predict → run → measure → explain**: commit a numeric prediction *before* running.
Claude gives setup and interprets output; the learner writes the code. Compiled artifacts land in
`labs/.build/` (gitignored).
