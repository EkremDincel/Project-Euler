#![allow(dead_code)]

pub struct Sieve {
	primes: Vec<i64>,
}

impl Sieve {
	pub fn new() -> Sieve {
		Sieve {
			primes: vec![2],
		}
	}

	pub fn extend(&mut self, to: i64) {
		for i in (self.primes.last().unwrap() + 1)..to {
			let mut index = 0;
			let mut cond = true;
			while index < self.primes.len() {
				let j = unsafe { self.primes.get_unchecked(index) };
				if i%j == 0 {
					cond = false;
					break;
				}
				index += 1;
			}
			if cond {
				self.primes.push(i);
			}
		}
	}

	pub fn is_prime(&mut self, num: i64) -> bool {
		self.extend(num);
		let to = (num as f64).sqrt() as i64;
		for &i in &self.primes {
			if i > to { break };
			if num%i == 0 {
				return false;
			}
		}
		true
	}
}

impl Iterator for Sieve {
	type Item = i64;

	fn next(&mut self) -> Option<Self::Item> {
		for i in (self.primes.last().unwrap() + 1).. {
			let mut index = 0;
			let mut cond = true;
			while index < self.primes.len() {
				let j = unsafe { self.primes.get_unchecked(index) };
				if i%j == 0 {
					cond = false;
					break;
				}
				index += 1;
			}
			if cond {
				self.primes.push(i);
				return Some(i)
			}
		}
		None
	}
}

pub fn largest_prime_factor(mut num: i64) -> i64 {
	let mut i = 2;
	while i < num {
		if num%i == 0 {
			num /= i;
		} else {
			i += 1;
		}
	}

	i
}

#[cfg(test)]
mod test {
	use super::*;

	#[test]
	fn test_sieve_extend() {
		let mut sieve = Sieve::new();
		sieve.extend(12);
		assert_eq!(sieve.primes, vec![2, 3, 5, 7, 11]);
	}

	#[test]
	fn test_sieve_is_prime() {
		let mut sieve = Sieve::new();
		assert_eq!(sieve.is_prime(2), true);
		assert_eq!(sieve.is_prime(3), true);
		assert_eq!(sieve.is_prime(4), false);
		assert_eq!(sieve.is_prime(41), true);
		assert_eq!(sieve.is_prime(12), false);
	}

	#[test]
	fn test_largest_prime_factor() {
		assert_eq!(largest_prime_factor(2), 2);
		assert_eq!(largest_prime_factor(10), 5);
		assert_eq!(largest_prime_factor(4), 2);
		assert_eq!(largest_prime_factor(9), 3);
		assert_eq!(largest_prime_factor(51), 17);
		assert_eq!(largest_prime_factor(11), 11);
	}
}