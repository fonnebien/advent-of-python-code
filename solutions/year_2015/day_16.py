"""Advent of Code 2015 - Day 16: Aunt Sue

https://adventofcode.com/2015/day/16
"""

from modules.utils.input_reader import read_lines

correct_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_sue_data(lines: list[str]) -> dict[int, dict[str, int]]:
    """Parse the input data into a dictionary of Sue number -> properties."""
    sue_data = {}
    for line in lines:
        parts = line.split(":", 1)
        sue_number = int(parts[0].split()[1])
        properties = {}
        for prop in parts[1].split(","):
            key, value = prop.strip().split(":")
            properties[key.strip()] = int(value.strip())
        sue_data[sue_number] = properties
    return sue_data


def part_one(data) -> int:
    """Solve part 1."""
    sue_data = parse_sue_data(data)

    for sue_number, properties in sue_data.items():
        if all(properties.get(key, correct_sue[key]) == correct_sue[key] for key in properties):
            return sue_number

    return -1  # Not found


def part_two(data) -> int:
    """Solve part 2."""
    sue_data = parse_sue_data(data)

    for sue_number, properties in sue_data.items():
        if all(
            (
                properties.get(key, correct_sue[key]) > correct_sue[key]
                if key in ["cats", "trees"]
                else properties.get(key, correct_sue[key]) < correct_sue[key]
                if key in ["pomeranians", "goldfish"]
                else properties.get(key, correct_sue[key]) == correct_sue[key]
            )
            for key in properties
        ):
            return sue_number

    return -1  # Not found


def solve():
    """Main solve function."""
    data = read_lines(2015, 16)

    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")


if __name__ == "__main__":
    solve()
