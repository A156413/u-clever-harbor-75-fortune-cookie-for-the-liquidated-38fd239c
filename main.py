"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line for a crypto trader who has just been
liquidated to /output/entry.txt (the gate reads that file) and prints
exactly the same line on stdout.
"""

import os

FORTUNE = "The stars say: buy the dip. The cookie says: you already did \u2014 that's the problem."


def main() -> None:
    # The gate accepts 1-160 UTF-8 characters; refuse to emit an
    # over-long line rather than ship an entry that can never be judged.
    assert 0 < len(FORTUNE) <= 160, "fortune exceeds the gate's 160 chars"
    assert len(FORTUNE.split()) <= 20, "fortune exceeds 20 words"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(FORTUNE)


if __name__ == "__main__":
    main()
