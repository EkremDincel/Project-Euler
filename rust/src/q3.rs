use crate::primes;

pub fn solution() -> i64 {
    primes::largest_prime_factor(600851475143)
}

#[test]
fn test() {
    assert_eq!(solution(), 6857);
}
