import typing

from utils import load_input

DIGIT_LOOKUP_TABLE = {
    "o": ["one"],
    "t": ["two", "three"],
    "f": ["four", "five"],
    "s": ["six", "seven"],
    "e": ["eight"],
    "n": ["nine"],
}

DIGIT_CONVERSION_TABLE = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char

    return ""


def get_spelled_digit_prefix(line: str) -> typing.Optional[str]:
    if options := DIGIT_LOOKUP_TABLE.get(line[0]):
        for option in options:
            if line.startswith(option):
                return option

    return None


def compress_digit(digit: str) -> str:
    return DIGIT_CONVERSION_TABLE[digit]


def parse_first_digit(line: str, backwards: bool = False) -> str:
    iterator = range(len(line) - 1, -1, -1) if backwards else range(len(line))

    for i in iterator:
        char = line[i]

        if char.isdigit():
            return char

        if digit := get_spelled_digit_prefix(line[i:]):
            return compress_digit(digit)

    return ""


def solution_part1(input_data: str) -> int:
    total_sum = 0
    for line in input_data.splitlines():
        calibration_value = int(get_first_digit(line) + get_first_digit(line[::-1]))
        total_sum += calibration_value

    return total_sum


def solution_part2(input_data: str) -> int:
    total_sum = 0
    for line in input_data.splitlines():
        first_digit = parse_first_digit(line)
        last_digit = parse_first_digit(line, backwards=True)
        total_sum += int(first_digit + last_digit)

    return total_sum


def test_get_first_digit():
    assert get_first_digit("a9c3") == "9"
    assert get_first_digit("02") == "0"


def test_parse_first_digit():
    assert parse_first_digit("oooneeee") == "1"
    assert parse_first_digit("2three") == "2"
    assert parse_first_digit("8aone", backwards=True) == "1"
    assert parse_first_digit("8aone9", backwards=True) == "9"


def test_part1_example():
    input_data = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
    assert solution_part1(input_data) == 142


def test_part2_example():
    input_data = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
    assert solution_part2(input_data) == 281


def main():
    input_data = load_input("day_1")
    print(f"Answer to day 1 part 1: {solution_part1(input_data)}")
    print(f"Answer to day 1 part 2: {solution_part2(input_data)}")


if __name__ == "__main__":
    main()
