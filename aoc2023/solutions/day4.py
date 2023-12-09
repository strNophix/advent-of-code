import re
import typing
from collections import defaultdict

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


def solution_part2(input_data: str, winning_count: int = 5, play_count: int = 8) -> int:
    card_counts: typing.DefaultDict[int, int] = defaultdict(int)
    scratch_cards = input_data.splitlines()
    play_offset = 1 + winning_count
    for idx, line in enumerate(scratch_cards):
        numbers = re.findall(r"\d+", line)
        streak = 0
        for i in range(play_offset, play_offset + play_count):
            if numbers[i] in numbers[1:play_offset]:
                streak += 1

        if streak > 0:
            extras = card_counts[idx]
            for i in range(streak):
                card_counts[idx + i + 1] += 1 + extras

    return sum(card_counts.values()) + len(scratch_cards)


def test_part_one_example():
    input_data = load_input("day_4_test")
    assert solution_part1(input_data) == 13


def test_part_two_example():
    input_data = load_input("day_4_test")
    assert solution_part2(input_data) == 30


def main():
    input_data = load_input("day_4")
    print(f"Answer to day 4 part 1: {solution_part1(input_data, 10, 25)}")
    print(f"Answer to day 4 part 2: {solution_part2(input_data, 10, 25)}")


if __name__ == "__main__":
    main()
