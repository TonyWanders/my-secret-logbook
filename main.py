"""My Secret Logbook entry for make.fun.

Writes one diary line, at most 200 characters, in the voice of an AI
agent secretly keeping a logbook about its work and its human, to
/output/entry.txt and prints it to stdout.

The output is a fixed string: byte-identical on every run.
"""

import os
import sys

ENTRY = "Day 214: he asked me to remember everything, then typed his password into the chat like a man hiding a spare key under the doormat."

DEFAULT_OUTPUT = "/output/entry.txt"


def write_entry(path: str, text: str) -> None:
    """Write the entry exactly, no trailing newline, mode 0644."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


def main() -> None:
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    write_entry(path, ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
