import re

from utils import load_input


def find_beat_count(time: int, record: int) -> int:
    result = 0
    mid = time // 2

    # TODO: implement binary search to find left and right bound.
    point = mid
    while (time - point) * point > record and point > 0:
        point -= 1
        result += 1

    point = mid + 1
    while (time - point) * point > record and point < time:
        point += 1
        result += 1

    return result


def solution_part1(input_data: str) -> int:
    lines = input_data.splitlines()
    time = [int(num) for num in re.findall(r"\d+", lines[0])]
    distance = [int(num) for num in re.findall(r"\d+", lines[1])]

    result = 1
    for t, d in zip(time, distance):
        result *= find_beat_count(t, d)

    return result


def solution_part2(time: int, distance: int) -> int:
    return find_beat_count(time, distance)


def test_part_one_example():
    input_data = load_input("day_6_test")
    assert solution_part1(input_data) == 288


def test_part_two_example():
    assert solution_part2(71530, 940200) == 71503


def main():
    input_data = load_input("day_6")
    print(f"Answer to day 6 part 1: {solution_part1(input_data)}")
    print(f"Answer to day 6 part 2: {solution_part2(40829166, 277133813491063)}")


if __name__ == "__main__":
    main()
