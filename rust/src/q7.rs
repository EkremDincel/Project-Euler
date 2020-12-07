use crate::primes::Sieve;

pub fn solution() -> i64 {
    Sieve::new().nth(10001 - 2).unwrap()
}

#[test]
fn test() {
    assert_eq!(solution(), 104743);
}
