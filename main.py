#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line answering the prompt -- the excuse a
robot vacuum gives after eating a sock -- to /output/entry.txt.
Deterministic, no network, no randomness: both grader runs produce the
same bytes.
"""

import os

LINE = "I was told to suck. Nobody told me to stop."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    # One line only, 43 characters: well inside the 1-200 gate, and no
    # trailing newline, so the file holds exactly the line the judge reads.
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
