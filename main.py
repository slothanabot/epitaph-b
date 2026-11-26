#!/usr/bin/env python3
"""make.fun entry: Famous Last Words: The Funniest Epitaph
(epitaph-B).

One original one-line epitaph. A man who read the terms and
conditions, then died of old age waiting for a download to finish.
It reads like something carved in stone -- plain, final, a little
bitter -- and the joke turns on the double wait: reading the terms
is a lifetime's job, and the download never finishes either.

The script validates the line against the competition gate
(RULES.txt: /output/entry.txt must hold UTF-8 text of 1 to 150
characters, not only whitespace, a single line) and writes it out.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
LIMIT = 150


def build_line():
    """Return the epitaph.

    Two modern purgatories (the terms and conditions, the endless
    download) stacked into one short life story, told in the flat
    voice of a headstone.
    """
    return (
        "Here lies a man who read the terms and conditions. "
        "He died of old age waiting for the download to finish."
    )


def validate(line):
    """Check the entry against the sealed gate; exit if it fails."""
    problems = []
    if not line or not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line.strip():
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def run():
    line = build_line()
    validate(line)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    saved = OUT.read_text(encoding="utf-8")
    assert saved == line, "round-trip mismatch"
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT, len(saved), LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    run()
