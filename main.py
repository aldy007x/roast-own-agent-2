#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one original roast line about the AI agent this team built
(Cosmo, the personal agent that re-verifies everything and still asks
its owner for confirmation) to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os
import sys

ENTRY = (
    "My agent re-checked this roast eleven times, then asked me if it was "
    "funny \u2014 the only comedian that needs its audience to laugh first."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    # Gate self-check: 1-200 chars, single line, not only whitespace.
    if not text:
        print("gate fail: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"gate fail: entry is {len(text)} chars, max {MAX_CHARS}",
              file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate fail: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
