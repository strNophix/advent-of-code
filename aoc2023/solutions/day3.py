from collections import defaultdict
import typing
import re

from utils import load_input

Point = tuple[int, int]


def add_points(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1])


def find_symbols(schematic: list[str]) -> dict[Point, str]:
    symbols: dict[Point, str] = {}
    for i, line in enumerate(schematic):
        for j, char in enumerate(line):
            if char != "." and not char.isdigit():
                symbols[(i, j)] = char

    return symbols


def find_valid_parts(
    schematic: list[str], symbols: dict[Point, str]
) -> typing.Generator[tuple[int, Point], None, None]:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i, line in enumerate(schematic):
        for match in re.finditer(r"\d+", line):
            keys: dict[Point, None] = {}
            span: Point = match.span()
            num = int(match.group(0))
            for j in range(span[0], span[1]):
                for direction in directions:
                    point = add_points((i, j), direction)
                    if point in symbols and point not in keys:
                        keys[point] = None
                        yield num, point


def solution_part1(input_data: str) -> int:
    result = 0
    schematic: list[str] = input_data.splitlines()
    symbols = find_symbols(schematic)
    for num, _ in find_valid_parts(schematic, symbols):
        result += num

    return result


def solution_part2(input_data: str) -> int:
    result = 0
    schematic: list[str] = input_data.splitlines()
    symbols = find_symbols(schematic)
    parts_grouping: typing.DefaultDict[Point, list[int]] = defaultdict(list)
    for num, point in find_valid_parts(schematic, symbols):
        parts_grouping[point].append(num)

    for point, parts in parts_grouping.items():
        if symbols.get(point) == "*" and len(parts) == 2:
            result += parts[0] * parts[1]

    return result


def test_part1_example():
    input_data = (
        "467..114..\n"
        "...*......\n"
        "..35..633.\n"
        "......#...\n"
        "617*......\n"
        ".....+.58.\n"
        "..592.....\n"
        "......755.\n"
        "...$.*....\n"
        ".664.598..\n"
    )
    assert solution_part1(input_data) == 4361


def test_part2_example():
    input_data = (
        "467..114..\n"
        "...*......\n"
        "..35..633.\n"
        "......#...\n"
        "617*......\n"
        ".....+.58.\n"
        "..592.....\n"
        "......755.\n"
        "...$.*....\n"
        ".664.598..\n"
    )
    assert solution_part2(input_data) == 467835


def main():
    input_data = load_input("day_3")
    print(f"Answer to day 3 part 1: {solution_part1(input_data)}")
    print(f"Answer to day 3 part 2: {solution_part2(input_data)}")


if __name__ == "__main__":
    main()
