#![allow(dead_code)]

pub struct Fibonacci {
    x: i64,
    y: i64,
}

impl Fibonacci {
    pub fn new() -> Fibonacci {
        Fibonacci { x: 0, y: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = i64;

    fn next(&mut self) -> Option<Self::Item> {
        let z = self.x;
        self.x = self.y;
        self.y += z;
        Some(z)
    }
}

#[test]
fn test() {
    assert_eq!(
        Fibonacci::new().take(10).collect::<Vec<_>>(),
        vec![0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    );
}
