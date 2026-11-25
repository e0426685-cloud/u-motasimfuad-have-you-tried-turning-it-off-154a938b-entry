"""Have You Tried Turning It Off? - make.fun entry (program/v1).

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.

Stdlib only. No third-party imports.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? Take your time \u2014 "
    "I get paid by the minute, and honestly, the hold music is my "
    "favourite song."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    # Gate: UTF-8 text of 1 to 199 characters, not only white space,
    # a single line.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of range 1-199"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text.strip(), "entry must be a single line"
    text.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # The grader runs as a different user: make the output world-readable.
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
