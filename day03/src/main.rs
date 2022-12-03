use std::collections::HashSet;

fn main() {
    let input = include_str!("../input");
    p1(input);
    p2(input);
}

fn ch_to_int(ch: char) -> i16 {
    if ch.is_uppercase() {
        ch.to_ascii_lowercase() as i16 - 70
    } else {
        ch as i16 - 96
    }
}

fn p1(input: &str) {
    println!(
        "{}",
        input.lines().fold(0, |a, ch| {
            let (l, r) = ch.split_at(ch.len() / 2);
            let l = HashSet::<char>::from_iter(l.chars());

            a + ch_to_int(r.chars().find(|c| l.contains(c)).unwrap())
        })
    );
}

fn p2(input: &str) {
    println!(
        "{}",
        input
            .lines()
            .collect::<Vec<&str>>()
            .chunks(3)
            .fold(0, |a, l| {
                let sets = vec![
                    HashSet::<char>::from_iter(l[0].chars()),
                    HashSet::<char>::from_iter(l[1].chars()),
                ];

                a + ch_to_int(
                    l[2].chars()
                        .find(|c| sets.iter().all(|s| s.contains(c)))
                        .unwrap(),
                )
            })
    );
}
