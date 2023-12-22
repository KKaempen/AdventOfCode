use std::fs;

fn main() {
    let data = fs::read_to_string("problem1.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n');
    let mut max = 0;
    let mut accum = 0;
    for el in data {
        match el.trim().parse::<u32>() {
            Ok(num) => {
                accum += num;
            },
            Err(_) => {
                max = if accum > max { accum } else { max };
                accum = 0;
                continue;
            },
        }
    }
    println!("{max}");
}
