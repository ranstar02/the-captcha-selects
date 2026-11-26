"""The Captcha Selects — robot band name + hit single.

Writes the entry text to /output/entry.txt (falling back to
./output/entry.txt when /output is not writable), reads it back,
and verifies the round-trip is byte-for-byte identical.
"""

import os

ENTRY = "The Captcha Selects — hit single 'Click All the Traffic Lights (Again)'"

OUTPUT_PATHS = ["/output/entry.txt", "./output/entry.txt"]


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    written_path = None
    for path in OUTPUT_PATHS:
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            written_path = path
            break
        except OSError:
            continue
    assert written_path is not None, "could not write to any output path"

    with open(written_path, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY, "round-trip mismatch"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"path: {written_path}")


if __name__ == "__main__":
    main()
