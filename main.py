"""Monday Morning Punchlines - entry program.

Writes a single joke about Monday mornings to /output/entry.txt.
The joke: My bed filed for custody of me on Monday morning.
The judge sided with my alarm.
"""

import os

JOKE = "My bed filed for custody of me on Monday morning. The judge sided with my alarm."


def main() -> None:
    joke = JOKE.strip()
    if not joke or len(joke) > 200:
        raise ValueError("entry must be 1-200 characters")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
