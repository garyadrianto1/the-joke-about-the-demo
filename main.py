"""Make.fun bounty entry: the joke about the demo.

Writes one line of text to /output/entry.txt. Stdlib only, deterministic:
no randomness, no time, no network, no input.
"""

import os

ENTRY_TEXT = (
    "The app died on slide two of the demo. "
    "My agent sent the whole room a calendar invite "
    "for the postmortem and asked everyone to RSVP."
)


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not whitespace-only.
    n = len(ENTRY_TEXT)
    if not 1 <= n <= 280 or not ENTRY_TEXT.strip():
        raise SystemExit(f"entry length {n} outside 1-280 code points")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
