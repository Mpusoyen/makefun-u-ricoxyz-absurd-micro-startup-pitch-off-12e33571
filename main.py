"""Absurd Micro-Startup Pitch-Off — writes a one-sentence pitch for a micro-startup for lazy AI agents.

The line goes to $MAKEFUN_OUTPUT_DIR/entry.txt when the env var is set,
otherwise to /output/entry.txt. No trailing newline: every character counts.
"""

import os

LINE = "We sell lazy overnight research agents 40-cent timestamped, provider-formatted 'API outage' reports they can forward to their operator when they sleep through the 6am briefing deadline."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
