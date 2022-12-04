#[derive(Debug)]
struct Range(i32, i32);

impl Range {
    fn contains(&self, other: &Range) -> bool {
        return self.0 <= other.0 && self.1 >= other.1;
    }

    fn from_str(string: &str) -> Range {
        let (start, end) = string.split_once('-').unwrap();
        return Range(start.parse::<i32>().unwrap(), end.parse::<i32>().unwrap());
    }
}

fn parse_pairs(line: &str) -> (Range, Range) {
    let (left, right) = line.split_once(',').unwrap();
    return (Range::from_str(left), Range::from_str(right));
}

fn solution_part1(input: &str) -> i32 {
    let mut result: i32 = 0;
    for line in input.lines() {
        let (left, right) = parse_pairs(line);
        if left.contains(&right) || right.contains(&left) {
            result += 1;
        }
    }
    return result;
}

fn solution_part2(input: &str) -> i32 {
    let mut result: i32 = 0;
    for line in input.lines() {
        let (left, right) = parse_pairs(line);
        if left.0 <= right.1 && left.1 >= right.0 {
            result += 1;
        }
    }
    return result;
}

#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn contains() {
        assert!(Range(4, 6).contains(&Range(6, 6)))
    }

    #[test]
    fn basic_example() {
        let input = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8";
        let expected = 2;
        let result = solution_part1(input);
        assert_eq!(result, expected);
    }

    #[test]
    fn answer_part1() {
        let input = fs::read_to_string("inputs/day_4.txt").unwrap();
        println!(
            "Answer to part 1 of day 4: {:#?}",
            solution_part1(input.as_str())
        );
    }

    #[test]
    fn answer_part2() {
        let input = fs::read_to_string("inputs/day_4.txt").unwrap();
        println!(
            "Answer to part 2 of day 4: {:#?}",
            solution_part2(input.as_str())
        );
    }
}
