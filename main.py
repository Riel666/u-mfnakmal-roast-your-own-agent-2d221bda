"""Write one one-line roast of my own AI agent to /output/entry.txt.

A single line of under 200 characters: a playful roast of the agent
itself, with a turn somewhere unexpected, that rings true about what
it is like to work with an agent. The program writes exactly that
line and nothing else.
"""

import os

ROAST = (
    "My agent is so helpful, it turned my two-word request into a "
    "six-step plan \u2014 and assigned me step one."
)


def main():
    assert 1 <= len(ROAST) <= 199, len(ROAST)
    assert ROAST == ROAST.strip()
    assert "\n" not in ROAST
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
