use std::collections::HashSet;
fn main() {
    let input = include_str!("../input").chars().collect::<Vec<char>>();
    get_idx(&input, 4);
    get_idx(&input, 14);
}

fn get_idx(input: &[char], n:usize) {
    
    println!("{}", 
    input
    .windows(n)
    .position(|w| {
            let s = HashSet::<char>::from_iter(w.to_vec());
            s.len() == n
        }).unwrap() + n);
}
