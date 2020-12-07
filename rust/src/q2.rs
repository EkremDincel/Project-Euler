use crate::fibonacci;

pub fn solution() -> i64 {
    fibonacci::Fibonacci::new()
        .into_iter()
        .take_while(|&i| i < 4_000_000)
        .filter(|i| i % 2 == 0)
        .sum()
}

#[test]
fn test() {
    assert_eq!(solution(), 4613732);
}
