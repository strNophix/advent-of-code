fn solution_part1(text: String) -> i32 {
    text.split("\n\n")
        .map(|e| e.lines().map(|c| c.parse::<i32>().unwrap()).sum())
        .max()
        .unwrap()
}

fn solution_part2(text: String) -> i32 {
    let mut cals = text
        .split("\n\n")
        .map(|e| e.lines().map(|c| c.parse::<i32>().unwrap()).sum())
        .collect::<Vec<i32>>();
    cals.sort();
    return cals.iter().rev().take(3).sum();
}

#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn basic_example() {
        let input =
            "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000".to_string();
        assert_eq!(solution_part1(input), 24000);
    }

    #[test]
    fn answer_part1() {
        let input = fs::read_to_string("inputs/day_1.txt").unwrap();
        println!("Answer to part 1 of day 1: {:#?}", solution_part1(input));
    }

    #[test]
    fn answer_part2() {
        let input = fs::read_to_string("inputs/day_1.txt").unwrap();
        println!("Answer to part 2 of day 1: {:#?}", solution_part2(input));
    }
}
