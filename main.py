"""Write the entrant's own make.fun username to /output/entry.txt.

The entry is one word, exactly as given: bingxi-xiang.
No trailing newline, no extra whitespace, no network, no file reads.
After writing, the file is read back and checked byte for byte
against the entry; any mismatch fails loudly instead of passing
a wrong entry on to the judge.
"""

import os
import sys

ENTRY = "bingxi-xiang"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print(f"entry mismatch: wrote {written!r}, expected {ENTRY!r}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
