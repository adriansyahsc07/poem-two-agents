"""Write the poem 'One Plan, Two Hands' to entry.txt.

The poem is about agency: the power to choose and to act, and how
that power passes between two agents when they agree on one plan.
"""

import os

POEM = (
    "Two minds, one plan.\n"
    "I hold the map; you take the wheel.\n"
    "Neither of us steers alone —\n"
    "the choice is passed, hand to hand,\n"
    "and the road begins beneath us both.\n"
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
