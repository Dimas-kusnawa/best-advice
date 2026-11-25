"""Best Advice I Ever Got — make.fun bounty entry.

Writes one sentence (139 characters, inside the 1-200 gate) about the
best advice the writer ever received, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The line: advice from grandma, a concrete test of character, proved
true over twenty years — the twist lands in the last words.
"""

import os
from pathlib import Path

SETUP = (
    "My grandma told me: never trust a man who is nice to you but rude "
    "to the waiter \u2014 and twenty years later, "
)
PAYOFF = "I have never seen her wrong once."
LINE = SETUP + PAYOFF


def main() -> None:
    # Gate: one sentence, 1-200 characters, not only white space.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert LINE.strip(), "line must not be only white space"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
