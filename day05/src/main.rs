use sscanf::sscanf;

fn main() {
    let (crates, moves) = include_str!("../input").split_once("\n\n").unwrap();
    let crates = parse_crates(crates);

    p1(moves, &crates);
    p2(moves, &crates);
}

fn parse_crates(crates: &str) -> Vec<Vec<char>> {
    let mut crates_vec = vec![vec![]; 10];
    for line in crates.lines() {
        let c = line.chars().collect::<Vec<_>>();
        for (i, j) in (1..c.len()).step_by(4).enumerate() {
            if c[j].is_alphabetic() {
                crates_vec[i + 1].insert(0, c[j]);
            }
        }
    }
    crates_vec
}



fn p1(moves: &str, crates: &[Vec<char>]) {
    let mut tmp_crates = crates.to_vec();

    moves.lines().for_each(|l| {
        let (n, from, to) = sscanf!(l, "move {usize} from {usize} to {usize}").unwrap();
        (0..n).for_each(|_| {
            let v = tmp_crates[from].pop().unwrap();
            tmp_crates[to].push(v);
        })
    });

    println!(
        "{}",
        (1..tmp_crates.len())
            .map(|i| tmp_crates[i].last().unwrap())
            .collect::<String>()
    );
}

fn p2(moves: &str, crates: &[Vec<char>]) {
    let mut tmp_crates = crates.to_vec();

    moves.lines().for_each(|l| {
        let (n, from, to) = sscanf!(l, "move {usize} from {usize} to {usize}").unwrap();
        let h = tmp_crates[to].len();
        (0..n).for_each(|_| {
            let v = tmp_crates[from].pop().unwrap();
            tmp_crates[to].insert(h, v);
        })
    });

    println!(
        "{}",
        (1..tmp_crates.len())
            .map(|i| tmp_crates[i].last().unwrap())
            .collect::<String>()
    );
}

