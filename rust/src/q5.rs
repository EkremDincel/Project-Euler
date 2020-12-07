use crate::divisors::lcms;

pub fn solution() -> i64 {
	lcms((1..20).collect::<Vec<_>>().iter())
}

#[test]
fn test() {
	assert_eq!(solution(), 232792560);
}