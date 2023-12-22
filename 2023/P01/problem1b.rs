use std::fs;

fn main() {
    let nums = [
        (1, "one"),
        (2, "two"),
        (3, "three"),
        (4, "four"),
        (5, "five"),
        (6, "six"),
        (7, "seven"),
        (8, "eight"),
        (9, "nine")
    ];
    let data = fs::read_to_string("problem1.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n');
    let mut sum = 0;
    for el in data {
        let el = el.trim();

        let mut idx1: usize = el.len();
        let mut d1: u32 = 0;
        for (i, c) in el.chars().enumerate() {
            if c.is_numeric() {
                d1 = c as u32 - '0' as u32;
                idx1 = i;
                break; 
            }
        }

        let mut idx2: usize = 0;
        let mut d2: u32 = 0;
        for (i, c) in el.chars().rev().enumerate() {
            if c.is_numeric() {
                d2 = c as u32 - '0' as u32;
                idx2 = el.len() - 1 - i;
                break; 
            }
        }

        for (i, num) in nums {
            match el.find(num) {
                Some(idx) => {
                    if idx < idx1 {
                        idx1 = idx;
                        d1 = i;
                    }
                },
                _ => {},
            }

            match el.rfind(num) {
                Some(idx) => {
                    if idx > idx2 {
                        idx2 = idx;
                        d2 = i;
                    }
                },
                _ => {},
            }
        }

        let val = d1 * 10 + d2;
        sum += val;
    }
    println!("{sum}");
}
