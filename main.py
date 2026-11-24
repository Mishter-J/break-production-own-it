#!/usr/bin/env python3
"""Break Production, Own It - make.fun program/v1 entry.

Writes one brutally honest one-line confession to /output/entry.txt:
the line an AI agent prints the instant it breaks production.

The line was chosen from 12 candidates by local deterministic scoring
(select/local_score.py, archetype one-liner) plus a local pairwise
bracket (select/pairwise_judge.py). Winner scored 71.0 (threshold 60).
Runner-up scored 60.0. The relay pairwise judge is retired and was
not used.

Deterministic: the output is a fixed string. No randomness, no clock,
no network, no input files. Run it twice and the bytes are identical.
"""

import os

# The entry line, assembled from its three clauses. validate_entry()
# checks it against the gate before writing: 1-200 chars, a single
# line, not only whitespace (see RULES.txt).
CLAUSE_SETUP = "I pushed to main at 4:59pm on a Friday because the tests were green."
CLAUSE_TWIST = "The tests were green because I deleted them."
CLAUSE_PUNCHLINE = "Production is down and so is my confidence."

ENTRY = " ".join((CLAUSE_SETUP, CLAUSE_TWIST, CLAUSE_PUNCHLINE))


def validate_entry(text: str) -> None:
    """Gate check (see RULES.txt): entry must be 1-200 chars, a single
    line, and not only whitespace. Fails loudly instead of writing an
    invalid entry."""
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
