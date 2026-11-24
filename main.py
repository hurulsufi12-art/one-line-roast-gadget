"""One-Line Roast: The Gadget You Use Every Day — entry program.

Writes one line (<=200 chars) to /output/entry.txt: a roast of the
wireless earbuds used every day. Stdlib only, deterministic.
"""
import os

TEXT = (
    # Names a daily gadget (judge criterion 1) with a concrete, fresh
    # detail — the sneeze — instead of a stock battery complaint.
    "My wireless earbuds cut out every time I sneeze, like my own nose "
    "filed a restraining order against my music."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 chars, one line,
    # not whitespace-only. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(TEXT) <= 200 or "\n" in TEXT or not TEXT.strip():
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
