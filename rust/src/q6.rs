pub fn solution() -> i64 {
	((1..=100).map(|i: i64| i.pow(2)).sum::<i64>()  as i64 - (1..=100).sum::<i64>().pow(2) as i64).abs()
}

#[test]
fn test() {
	assert_eq!(solution(), 25164150);
}