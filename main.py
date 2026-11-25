"""One Line, One Laugh — make.fun entry.

Writes a single original one-liner to entry.txt. The program is fully
deterministic: the same bytes on every run, with no randomness, no clock,
no network and no input files.
"""

import os
from pathlib import Path

# One scene, one turn: therapy billed by the token, so even crying gets
# itemised. Setup, twist and payoff in a single breath, nothing to trim.
JOKE = "My AI therapist charges by the token, so now I cry in bullet points to save money."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text and not text.isspace(), "entry must not be only whitespace"
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
