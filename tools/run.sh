#!/usr/bin/env bash
# Compile and run a lab's C or C++ file with warnings + runtime checks.
# Usage: tools/run.sh path/to/file.c[pp] [input-file]   (no input file -> reads stdin)
#        NOCHECK=1 tools/run.sh ...   -> plain -O2 build (for timing / benchmarks)
#        TSAN=1    tools/run.sh ...   -> ThreadSanitizer build (if libtsan is installed)
# Threads are linked with -pthread. C files use gcc/c11, C++ files g++/c++20.
set -euo pipefail
src="$1"; input="${2:-}"
root="$(cd "$(dirname "$0")/.." && pwd)"; source "$root/tools/_flags.sh"
build="$root/labs/.build"; mkdir -p "$build"
bin="$build/$(basename "${src%.*}")"
case "$src" in
  *.cpp|*.cc|*.cxx) cc=g++; std=-std=c++20 ;;
  *.c)              cc=gcc; std=-std=c11 ;;
  *) echo "run.sh: unknown source type: $src" >&2; exit 2 ;;
esac
if [ "${NOCHECK:-0}" = "1" ]; then chk="-O2"; else chk="-O1 -g $(check_flags "$build" "$cc")"; fi
$cc $std -Wall -Wextra -Wshadow -pthread $chk "$src" -o "$bin"
if [ -n "$input" ]; then
  start=$(date +%s%N); "$bin" < "$input"; end=$(date +%s%N)
  echo "[time $(( (end - start) / 1000000 )) ms]" >&2
else "$bin"; fi
