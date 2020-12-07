#![allow(dead_code)]

use std::ops::Range;

trait Iterutils {
    fn cartesian_product() {}

    fn combinations() {}

    fn permutations() {}

    fn combinations_with_replacement() {}
}

impl<T: Iterator> Iterutils for T {}

pub struct NumberProducer {
    to: i64,
    a: i64,
    b: i64,
}

impl NumberProducer {
    // TODO: use range instead of two numbers
    pub fn new(range: Range<i64>) -> NumberProducer {
        NumberProducer {
            to: range.end,
            a: range.start,
            b: range.start - 1,
        }
    }
}

impl Iterator for NumberProducer {
    type Item = (i64, i64);

    fn next(&mut self) -> Option<Self::Item> {
        self.b += 1;
        if self.b > self.to {
            self.a += 1;
            self.b = self.a;
            if self.a > self.to {
                return None;
            }
        }

        Some((self.a, self.b))
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_number_procuder() {
        assert_eq!(
            NumberProducer::new(0..2).collect::<Vec<_>>(),
            vec![(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
        );
    }
}
