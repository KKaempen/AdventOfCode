use std::fs;

fn main() {
    let data = fs::read_to_string("problem15.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let data = data[0]
        .split(',');
    let mut sum = 0;
    for s in data {
        let mut v = 0;
        for c in s.chars() {
            v = ((v + (c as u32)) * 17) % 256;
        }
        sum += v;
    }
    println!("{sum}");
}
