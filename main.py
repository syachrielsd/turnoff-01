#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line from a hopeless tech support agent to a
desperate customer, to <output dir>/entry.txt.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable when set, otherwise /output. Paths are resolved from this
file's own directory, never from the process working directory.

Standard library only. Deterministic: the same bytes every run.
"""

import os
from pathlib import Path

LINE = (
    "Have you tried turning it off and on again? "
    "I just did mine while you were explaining your deadline, "
    "and now we're both staring at a black screen, "
    "so technically neither of us has a problem anymore."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # No trailing newline: the line is 198 chars and the gate caps the
    # file at 199, so every byte counts.
    entry_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
