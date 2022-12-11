fn calc_score(opponent: char, me: char) -> u32 {
    let mut score = 0;
    score += match (opponent, me) {
        ('A', 'Z') | ('B', 'X') | ('C', 'Y') => 0,
        ('C', 'X') | ('A', 'Y') | ('B', 'Z') => 6,
        _ => 3,
    };

    score += match me {
        'X' => 1,
        'Y' => 2,
        'Z' => 3,
        _ => unreachable!(),
    };

    return score;
}

fn find_move(opponent: char, result: char) -> char {
    match (opponent, result) {
        (_, 'Y') => char::from_u32(opponent as u32 - 'A' as u32 + 'X' as u32).unwrap(),
        ('B', 'X') | ('C', 'Z') => 'X',
        ('C', 'X') | ('A', 'Z') => 'Y',
        ('A', 'X') | ('B', 'Z') => 'Z',
        _ => unreachable!(),
    }
}

fn solution_part1(text: String) -> u32 {
    text.lines()
        .filter(|g| g.len() == 3)
        .map(|g| {
            let mut chars = g.chars();
            calc_score(chars.next().unwrap(), chars.next_back().unwrap())
        })
        .sum()
}

fn solution_part2(text: String) -> u32 {
    text.lines()
        .filter(|g| g.len() == 3)
        .map(|g| {
            let mut chars = g.chars();
            let opponent = chars.next().unwrap();
            let me = find_move(opponent, chars.next_back().unwrap());
            calc_score(opponent, me)
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn answer_part1() {
        let input = fs::read_to_string("inputs/day_2.txt").unwrap();
        println!("Answer to part 1 of day 2: {:#?}", solution_part1(input));
    }

    #[test]
    fn answer_part2() {
        let input = fs::read_to_string("inputs/day_2.txt").unwrap();
        println!("Answer to part 2 of day 2: {:#?}", solution_part2(input));
    }
}
