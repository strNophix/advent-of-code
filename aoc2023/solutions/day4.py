import re

from utils import load_input


def solution_part1(input_data: str, winning_count: int = 5, play_count: int = 8) -> int:
    result = 0
    play_offset = 1 + winning_count
    for line in input_data.splitlines():
        numbers = re.findall(r"\d+", line)
        streak = 0
        for i in range(play_offset, play_offset + play_count):
            if numbers[i] in numbers[1:play_offset]:
                streak += 1

        if streak > 0:
            result += 2 ** (streak - 1)

    return result


def test_part_one_example():
    input_data = (
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n"
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n"
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n"
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n"
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n"
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n"
    )
    assert solution_part1(input_data) == 13


def main():
    input_data = load_input("day_4")
    print(f"Answer to day 4 part 1: {solution_part1(input_data, 10, 25)}")


if __name__ == "__main__":
    main()
