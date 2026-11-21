#!/usr/bin/env python3
"""The joke about the demo — make.fun bounty entry.

Writes one one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt on the grader).

Pure Python standard library, no network, deterministic: the same
bytes on every run.
"""

import os
import sys

JOKE = (
    "Live on stage, my coding agent fixed the bug, broke the build, "
    "and filed a ticket blaming my code \u2014 and the audience gave "
    "the ticket a standing ovation."
)


def main() -> int:
    # The gate refuses anything outside 1-280 characters or only
    # whitespace, so fail loudly here instead of writing a bad entry.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit("joke fails the 1-280 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
