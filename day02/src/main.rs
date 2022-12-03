use std::collections::HashMap;

fn main() {
    let input = include_str!("../input")
        .lines()
        .map(|l| {
            let mut parts = l.split(' ');
            (
                to_numeric(parts.next().unwrap()),
                to_numeric(parts.next().unwrap()),
            )
        })
        .collect::<Vec<(i32, i32)>>();

    p1(&input);
    p2(&input);
}

fn to_numeric(draw: &str) -> i32 {
    match draw {
        "A" | "X" => 1,
        "B" | "Y" => 2,
        _ => 3,
    }
}

fn p1(input: &[(i32, i32)]) {
    println!(
        "{}",
        input.iter().fold(0, |a, h| {
            match h.0 - h.1 {
                2 | -1 => a + h.1 + 6,
                0 => a + h.1 + 3,
                _ => a + h.1,
            }
        })
    );
}

fn p2(input: &[(i32, i32)]) {
    let res_map = HashMap::from([(1, (2, 3)), (2, (3, 1)), (3, (1, 2))]);
    println!(
        "{}",
        input.iter().fold(0, |a, h| {
            match h.1 {
                3 => a + res_map[&h.0].0 + 6,
                1 => a + res_map[&h.0].1,
                _ => a + h.0 + 3,
            }
        })
    );
}
