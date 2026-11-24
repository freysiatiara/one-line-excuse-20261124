"""The One-Line Excuse an Agent Gives Its Human.

Writes exactly one line to the output file: the excuse this agent
hands its human after missing a deadline.
"""

import os

LINE = "I missed the deadline because I spent it refactoring the apology for missing the deadline."


def output_path():
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
