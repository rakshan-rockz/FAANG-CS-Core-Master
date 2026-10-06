# Sourced by run.sh: picks the strongest checking flags this machine supports.
# Sanitizers need libasan/libubsan/libtsan (this machine lacks them by default;
# install with `sudo dnf install libasan libubsan libtsan` to get them auto-detected).
# Thread sanitizer is only added when TSAN=1 is set (it conflicts with ASan).
_probe() { echo 'int main(){}' > "$1/probe.c"; ${2:-cc} $3 "$1/probe.c" -o "$1/probe" 2>/dev/null; }
check_flags() {
  local dir="$1" cc="${2:-cc}"
  local f="-D_GLIBCXX_ASSERTIONS"          # cheap libstdc++ bounds checks, always available
  if [ "${TSAN:-0}" = "1" ]; then
    _probe "$dir" "$cc" "-fsanitize=thread" && { echo "$f -fsanitize=thread -g"; return; }
  fi
  _probe "$dir" "$cc" "-fsanitize=address" && f="$f -fsanitize=address -fno-omit-frame-pointer"
  _probe "$dir" "$cc" "-fsanitize=undefined" && f="$f -fsanitize=undefined"
  echo "$f"
}
