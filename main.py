"""Have You Tried Turning It Off? — one funny line from a hopeless tech support agent.

The program writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset). Deterministic:
the same line, byte for byte, on every run.
"""

import os

LINE = "Good news \u2014 I've turned it off and on again three times, and it's still broken, so we're officially out of ideas together."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
