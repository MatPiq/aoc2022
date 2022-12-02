use std::collections::BinaryHeap;

fn main() {
    let input = include_str!("../input");
    solve_one(input);
    solve_two(input);
}

fn solve_one(input: &str) {
    println!(
        "{}",
        input.split("\n\n").fold(0, |a, s| {
            a.max(s.lines().map(|n| n.parse::<u32>().unwrap()).sum())
        })
    );
}

fn solve_two(input: &str) {
    let mut heap = BinaryHeap::new();
    input
        .split("\n\n")
        .map(|s| s.lines().map(|n| n.parse::<u32>().unwrap()).sum::<u32>())
        .for_each(|s| heap.push(s));

    println!("{}", (0..3).fold(0, |a, _| a + heap.pop().unwrap()));
}
