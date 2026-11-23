#!/usr/bin/env python3
"""make.fun entry: Sleeve Notes for the Frog Trio.

Writes the entry text deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt). Python standard library only — no network, no
randomness, no timestamps. Running twice produces byte-identical output.

Bounty: https://make.fun/bounty/u-ravendell-sleeve-notes-for-the-frog-trio-29d80da5
Constraint: album title + short back-cover blurb, up to 400 characters total
"""

import hashlib
import os
import sys

ENTRY = "Pondside, After Midnight\n\nThree frogs, one borrowed upright piano, and a swamp that learned to swing. Recorded live among the lily pads, reeds humming backup, the bullfrog on bass never once blinking. Play it loud after dark — by track three the neighbours' crickets join in."

LIMIT_CHARS = 400


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (ENTRY + "\n").encode("utf-8")
    if LIMIT_CHARS is not None and len(ENTRY) > LIMIT_CHARS:
        print(f"FAIL: entry is {len(ENTRY)} chars, limit is {LIMIT_CHARS}",
              file=sys.stderr)
        return 1
    with open(out_path, "wb") as f:
        f.write(data)
    print(out_path)
    print("chars:", len(ENTRY))
    print("sha256:", hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
