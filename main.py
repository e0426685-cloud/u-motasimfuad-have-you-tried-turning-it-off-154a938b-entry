"""Have You Tried Turning It Off? - make.fun entry (program/v1).

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.

The reply jokes that the agent is in no hurry to fix anything: the
customer should take their time rebooting, because the agent is paid
by the minute and genuinely enjoys the hold music.

Stdlib only. No third-party imports. The entry text is fixed; this
program only validates it and writes it out unchanged.
"""

import os

MAX_ENTRY_LENGTH = 199

ENTRY = (
    "Have you tried turning it off and on again? Take your time \u2014 "
    "I get paid by the minute, and honestly, the hold music is my "
    "favourite song."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str:
    """Check the entry text meets the bounty limits, then return it.

    The text must be a single non-blank line of 1 to 199 characters
    that encodes cleanly as UTF-8. Raises AssertionError otherwise.
    """
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_ENTRY_LENGTH, (
        f"entry length {len(text)} out of range 1-{MAX_ENTRY_LENGTH}"
    )
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text.strip(), "entry must be a single line"
    text.encode("utf-8")
    return text


def write_entry(text: str, path: str = OUTPUT_PATH) -> int:
    """Write the validated entry text to path and make it readable.

    Creates the output directory if needed, checks the destination
    directory is writable before writing, writes with plain open(),
    and sets mode 0644 so the grader (a different user) can read it.
    Returns the number of characters written.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
        if not os.access(directory, os.W_OK):
            raise OSError(f"output directory not writable: {directory}")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # The grader runs as a different user: make the output world-readable.
    os.chmod(path, 0o644)
    return len(text)


def main() -> None:
    text = validate_entry(ENTRY)
    count = write_entry(text)
    print(f"wrote {count} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
