fn p1(input: &[char], n:usize) -> usize {
    for (i, w) in input.windows(n).enumerate(){
        let s = HashSet::<char>::from_iter(w.iter());
        if s.len() == n{
            return i + n;
        }
    }
}
