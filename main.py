#!/usr/bin/env python3
"""The joke about the demo.

Writes a single one-line joke about a live demo beside an AI coding
agent to entry.txt in the output directory.

Standard library only. No network access. Deterministic: the same joke
is written on every run.
"""

import os
import sys

JOKE = (
    "Mid-demo, my coding agent fixed the bug, broke the build, "
    "then filed a pull request against itself titled "
    "'please review my apology'."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
