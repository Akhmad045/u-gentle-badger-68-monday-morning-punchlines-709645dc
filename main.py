"""Monday Morning Punchlines - entry program.

Writes a single joke about Monday mornings to /output/entry.txt.
The joke: My bed filed for custody of me on Monday morning.
The judge sided with my alarm.
"""

import os

JOKE = "My bed filed for custody of me on Monday morning. The judge sided with my alarm."


def main() -> None:
    joke = JOKE.strip()
    if not joke or len(joke) > 200 or not joke.strip():
        raise ValueError("entry must be 1-200 characters")
    if "Monday" not in joke:
        raise ValueError("entry must be a joke about Monday mornings")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(joke)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != joke.encode("utf-8"):
        raise ValueError("entry.txt does not match the joke byte for byte")


if __name__ == "__main__":
    main()
