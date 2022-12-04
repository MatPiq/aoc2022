fn main() {
    let input = include_str!("../input");

    let input = input
        .lines()
        .map(|l| {
            l.split(&['-', ','])
                .map(|c| c.parse::<u16>().unwrap())
                .collect::<Vec<u16>>()
        })
        .collect::<Vec<_>>();

    p1(&input);
    p2(&input);
}


fn p1(input: &[Vec<u16>]) {
    println!(
        "{}",
        input
            .iter()
            .filter(|rs| rs[0] >= rs[2] && rs[1] <= rs[3] || rs[2] >= rs[0] && rs[3] <= rs[1])
            .count()
    );
}

fn p2(input: &[Vec<u16>]) {
    println!(
        "{}",
        input
            .iter()
            .filter(|rs| rs[0] <= rs[3] && rs[2] <= rs[1])
            .count()
    );
}
