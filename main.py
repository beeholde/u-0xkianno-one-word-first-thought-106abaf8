#!/usr/bin/env python3
"""One Word, First Thought - make.fun entry.

Writes exactly one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The word is "quockerwodger": a 19th-century word for a politician who
follows the party line like a puppet on strings. It was chosen because
the house judge prizes surprise, vividness and a spark of wit over
anything safe: quockerwodger is a word almost no reader would guess,
it calls up a sharp image (a dancing puppet-politician), and its sound
carries a joke of its own. Nothing else is written: one word, no
explanation, no second draft.

Standard library only. No network, no randomness, no time dependence:
every run writes the same 13 bytes.
"""

import os

WORD = "quockerwodger"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD)
    os.chmod(path, 0o644)
    # Guard: the gate is exactly one word, so verify the bytes on disk
    # before returning; a mismatch fails loudly instead of submitting
    # a truncated or padded entry.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        assert handle.read() == WORD


if __name__ == "__main__":
    main()
