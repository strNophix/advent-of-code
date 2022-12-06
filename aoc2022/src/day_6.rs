use std::collections::HashSet;

fn is_unique_string(chars: &str) -> bool {
    let mut set: HashSet<char> = HashSet::with_capacity(chars.len());
    set.extend(chars.chars());
    return set.len() == chars.len();
}

fn solution(sequence: String, sub_len: usize) -> usize {
    for i in 0..(sequence.len() - sub_len) {
        let sub = &sequence[i..i + sub_len];
        if is_unique_string(sub.try_into().unwrap()) {
            return i + sub_len;
        }
    }

    return 0;
}

#[cfg(test)]
mod tests {
    use std::fs;

    use super::*;

    #[test]
    fn basic_example() {
        let input = "bvwbjplbgvbhsrlpgdmjqwftvncz".to_string();
        assert_eq!(solution(input, 4), 5);
        let input = "nppdvjthqldpwncqszvftbrmjlhg".to_string();
        assert_eq!(solution(input, 4), 6);
        let input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg".to_string();
        assert_eq!(solution(input, 4), 10);
        let input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw".to_string();
        assert_eq!(solution(input, 4), 11);
    }

    #[test]
    fn answer_part1() {
        let input = fs::read_to_string("inputs/day_5.txt").unwrap();
        println!("Answer to part 1 of day 6: {:#?}", solution(input, 4));
    }

    #[test]
    fn answer_part2() {
        let input = fs::read_to_string("inputs/day_5.txt").unwrap();
        println!("Answer to part 2 of day 6: {:#?}", solution(input, 14));
    }
}
