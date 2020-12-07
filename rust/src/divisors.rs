#![allow(dead_code)]

// ebob
pub fn gcd(mut a: i64, mut b: i64) -> i64 {
	while b != 0 {
		let r = a;
		a = b;
		b = r % b;
	}
	a
}

// ekok
pub fn lcm(a: i64, b: i64) -> i64 {
	a*b / gcd(a, b)
}

pub fn lcms<'a, T>(nums: T) -> i64 
where T: 'a + Iterator<Item=&'a i64>
{
	nums.fold(1, |a, b| lcm(a, *b))
}

pub fn gcds<'a, T>(nums: T) -> i64 
where T: 'a + Iterator<Item=&'a i64>
{
	nums.fold(0, |a, b| gcd(a, *b))
}

#[cfg(test)]
mod test {
	use super::*;

	#[test]
	fn test_gcd() {
		assert_eq!(gcd(2, 5), 1);
		assert_eq!(gcd(6, 12), 6);
		assert_eq!(gcd(12, 3), 3);
		assert_eq!(gcd(1, 3), 1);
		assert_eq!(gcd(1, 1), 1);
	}

	#[test]
	fn test_lcm() {
		assert_eq!(lcm(2, 5), 10);
		assert_eq!(lcm(6, 12), 12);
		assert_eq!(lcm(12, 3), 12);
		assert_eq!(lcm(1, 3), 3);
		assert_eq!(lcm(1, 1), 1);
	}

	#[test] 
	fn test_gcds() {
		assert_eq!(gcds([3, 6, 9].iter()), 3);
		assert_eq!(gcds([2, 8, 12].iter()), 2);
		assert_eq!(gcds([1, 1, 1].iter()), 1);
		assert_eq!(gcds([2, 1, 1].iter()), 1);
		assert_eq!(gcds([5, 12, 34].iter()), 1);
		assert_eq!(gcds([10, 15, 25].iter()), 5);
		assert_eq!(gcds([].iter()), 0);
	}

	#[test] 
	fn test_lcms() {
		assert_eq!(lcms([3, 6, 9].iter()), 18);
		assert_eq!(lcms([1, 1, 1].iter()), 1);
		assert_eq!(lcms([2, 1, 1].iter()), 2);
		assert_eq!(lcms([5, 12, 34].iter()), 1020);
		assert_eq!(lcms([].iter()), 1);
	}
}