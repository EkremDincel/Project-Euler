use crate::iterutils;

pub fn solution() -> i64 {
	iterutils::NumberProducer::new(100..999)
		.map(|(i, j)| i*j)
		.filter(|i| 
			(|a: String| a == a.chars().rev().collect::<String>())
				(i.to_string())
		)
		.max().unwrap()
}

#[test] 
fn test() {
		assert_eq!(solution(), 906609);
}
