use crate::iterutils::NumberProducer;

pub fn solution() -> u64 {

	match NumberProducer::new(1..500).map(|(a, b)| 
				(a as u64, b as u64, 
					{
						let c = ((a.pow(2) + b.pow(2)) as f64).sqrt();
						if c.fract() == 0.0 { c } else { 0.0 }
					} as u64
				)
			)
			.find(|(a, b, c)| a+b+c == 1000).unwrap() 
		{
			(a, b, c) => a*b*c
		}
}

#[test]
fn test() {
	assert_eq!(solution(), 31875000);
}