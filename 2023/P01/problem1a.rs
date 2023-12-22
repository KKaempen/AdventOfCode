use std::fs;

fn main() {
    let data = fs::read_to_string("problem1.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n');
    let mut sum = 0;
    for el in data {
        let el = el.trim();
        let mut d1: u32 = 0;
        let mut d2: u32 = 0;
        for c in el.chars() {
            if c.is_numeric() {
                d1 = c as u32 - '0' as u32;
                break; 
            }
        }
        for c in el.chars().rev() {
            if c.is_numeric() {
                d2 = c as u32 - '0' as u32;
                break; 
            }
        }
        let val = d1 * 10 + d2;
        sum += val;
    }
    println!("{sum}");
}
