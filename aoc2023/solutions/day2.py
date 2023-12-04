import re

from utils import load_input


def solution_part1(input_data: str) -> int:
    result = 0
    color_limits = {"red": 12, "green": 13, "blue": 14}

    for line in input_data.splitlines():
        found_violation = False
        subs = re.split(r"[;:, ]+", line)
        game_id = subs[1]
        counts = subs[2:]

        for i in range(0, len(counts), 2):
            if int(counts[i]) > color_limits[counts[i + 1]]:
                found_violation = True
                break

        if found_violation:
            continue

        result += int(game_id)

    return result


def solution_part2(input_data: str) -> int:
    result = 0

    for line in input_data.splitlines():
        highest_count = {"red": 0, "green": 0, "blue": 0}
        subs = re.split(r"[;:, ]+", line)
        counts = subs[2:]

        for i in range(0, len(counts), 2):
            num = int(counts[i])
            color = counts[i + 1]
            if num > highest_count[color]:
                highest_count[color] = num

        red, green, blue = highest_count.values()
        result += red * green * blue

    return result


def test_part1_example():
    input_data = (
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n"
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n"
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n"
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    )
    assert solution_part1(input_data) == 8


def test_part2_example():
    input_data = (
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n"
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n"
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n"
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    )
    assert solution_part2(input_data) == 2286


def main():
    input_data = load_input("day_2")
    print(f"Answer to day 2 part 1: {solution_part1(input_data)}")
    print(f"Answer to day 2 part 2: {solution_part2(input_data)}")


if __name__ == "__main__":
    main()
