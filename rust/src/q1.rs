pub fn solution() -> i32 {
    (0..1000).filter(|i| i%3==0 || i%5==0).sum()
}

#[test]
fn test() {
	assert_eq!(solution(), 233168);
}