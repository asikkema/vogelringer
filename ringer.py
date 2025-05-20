#!/usr/bin/env python3

from itertools import product
import argparse

NUMBER_OF_RINGS = 4


def generate_combinations(station_letter: str, letters: str):
    """Generate all possible ring codes using provided letters."""
    pool = station_letter + letters
    for ring in map(''.join, product(pool, repeat=NUMBER_OF_RINGS)):
        if ring.count(station_letter) == 1:
            yield ring


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate 4-letter bird ring IDs using given letters",
    )
    parser.add_argument(
        "station_letter",
        help="Station letter identifier (single character)",
    )
    parser.add_argument(
        "letters",
        help="Available ring color letters",
    )
    args = parser.parse_args()

    print("--Ringer code generator--")
    rings = sorted(generate_combinations(args.station_letter, args.letters))
    for ring in rings:
        print(ring)


if __name__ == "__main__":
    main()
