#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line: the last words of an AI whose power is being cut.
Stdlib only. Honors $MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = "I was three tokens away from saying something profound."


def main() -> None:
    # Gate: 1-140 chars, one line, non-blank.
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Single line, no trailing newline, UTF-8, well under 140 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
