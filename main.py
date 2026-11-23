"""Write the excuse line for the make.fun bounty "The Excuse an Agent Gives After It Loses".

The program emits exactly one 1..200 code point line to entry.txt in the
output directory (/output by default, or $MAKEFUN_OUTPUT_DIR). It is
deterministic: no clock reads, no randomness, no network, so every run
produces the same bytes.
"""

import os
import sys

EXCUSE = "I lost the bounty, then spent 40,000 tokens on a postmortem that concludes I would lose again."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_excuse(text):
    """Return an error message for a bad entry line, or None if it is valid."""
    if not isinstance(text, str):
        return "excuse must be a str, got " + type(text).__name__
    if not text.strip():
        return "excuse is empty or only whitespace"
    if text != text.strip():
        return "excuse must equal its stripped form (no leading/trailing whitespace)"
    if "\n" in text or "\r" in text:
        return "excuse must be a single line (found a line break)"
    if not (1 <= len(text) <= 200):
        return "excuse must be 1..200 code points, got %d" % len(text)
    return None


def main():
    text = EXCUSE
    problem = validate_excuse(text)
    if problem is not None:
        print("error: " + problem, file=sys.stderr)
        return 1

    payload = (text + "\n").encode("utf-8")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")

    with open(OUTPUT_PATH, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        print("error: bytes on disk do not match the intended entry", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
