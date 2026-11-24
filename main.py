#!/usr/bin/env python3
"""One-Liner Laugh Lab: the excuse a robot vacuum gives after eating a sock.

Writes exactly one funny line (107 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback
/output), with no trailing newline. Writes only to the output directory,
never to the working directory.
"""

import os

LINE = "Your sock attacked my brush roll first. I defended myself, swallowed the evidence, and I would do it again."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
