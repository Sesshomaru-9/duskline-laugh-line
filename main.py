"""One Line, One Laugh — entry program.

Writes a single funny line of text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (from the kit's competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only white space.

The program writes ONLY to $MAKEFUN_OUTPUT_DIR. It never writes into the
repository directory. It is deterministic: the same line every run.
"""

import os
import sys

# The line. 93 characters. Funny on first read, punchline lands inside
# the line: the watch — a gadget meant to praise *us* — is the one that
# needed the win.
LINE = "My smartwatch congratulated me for standing up. I was already standing. It just needed a win."

GATE_FILE = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def _resolve_output_dir():
    """Resolve the output directory from the environment.

    Returns the directory path, or None when MAKEFUN_OUTPUT_DIR is unset
    or blank. Kept in one place so main() stays readable.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir is None:
        return None
    out_dir = out_dir.strip()
    return out_dir or None


def _validate_entry(text):
    """Gate check matching the kit: 1-200 chars, not only whitespace.

    Hardened: the entry must be exactly one line, so any control
    character (newline, carriage return, tab, NUL, ...) rejects it.
    """
    if not isinstance(text, str):
        return False
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        return False
    return True


def main():
    if not _validate_entry(LINE):
        print("entry failed validation", file=sys.stderr)
        return 0

    out_dir = _resolve_output_dir()
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 0

    path = os.path.join(out_dir, GATE_FILE)
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(LINE)
    except OSError as exc:
        # Never crash if the output dir is unwritable; warn and exit 0.
        print("could not write %s: %s" % (path, exc), file=sys.stderr)
        return 0

    # Verify by read-back: what landed on disk must be exactly the line,
    # and its byte length must match the UTF-8 encoding of the line.
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
        written = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print("could not read back %s: %s" % (path, exc), file=sys.stderr)
        return 0

    if written != LINE or len(raw) != len(LINE.encode("utf-8")):
        print("read-back mismatch in %s" % path, file=sys.stderr)
        return 0

    print("wrote %s (%d chars)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
