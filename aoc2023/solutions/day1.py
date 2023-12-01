import typing

from utils import load_input


def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char

    return ""


def compress_digit(char: str) -> str:
    translation_table = {
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
    return translation_table[char]


def get_spelled_digit_prefix(line: str) -> typing.Optional[str]:
    digit_lookup_table = {
        "o": ["one"],
        "t": ["two", "three"],
        "f": ["four", "five"],
        "s": ["six", "seven"],
        "e": ["eight"],
        "n": ["nine"],
    }

    if options := digit_lookup_table.get(line[0]):
        for option in options:
            if line.startswith(option):
                return option

    return None


def parse_norm_digits(line: str) -> list[str]:
    result: list[str] = []
    for idx, char in enumerate(line):
        if char.isdigit():
            result.append(char)

        if digit := get_spelled_digit_prefix(line[idx:]):
            result.append(compress_digit(digit))

    return result


def solution_part1(input_data: str) -> int:
    total_sum = 0
    for line in input_data.splitlines():
        calibration_value = int(get_first_digit(line) + get_first_digit(line[::-1]))
        total_sum += calibration_value

    return total_sum


def solution_part2(input_data: str) -> int:
    total_sum = 0
    for line in input_data.splitlines():
        digits = parse_norm_digits(line)
        total_sum += int(digits[0] + digits[-1])

    return total_sum


def test_get_first_digit():
    assert get_first_digit("a9c3") == "9"
    assert get_first_digit("02") == "0"


def test_parse_norm_digits():
    assert parse_norm_digits("oooneeee") == ["1"]
    assert parse_norm_digits("twothree") == ["2", "3"]
    assert parse_norm_digits("8aone9") == ["8", "1", "9"]


def test_part1_example():
    input_data = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
    assert solution_part1(input_data) == 142


def test_part2_example():
    input_data = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
    assert solution_part2(input_data) == 281


def main():
    input_data = load_input("day1")
    print(f"Answer to day 1 part 1: {solution_part1(input_data)}")
    print(f"Answer to day 1 part 2: {solution_part2(input_data)}")


if __name__ == "__main__":
    main()
