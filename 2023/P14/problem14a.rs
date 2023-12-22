use std::fs;

fn main() {
    let data = fs::read_to_string("problem14.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .map(|line| {
            let mut char_vec = Vec::<char>::new();
            for c in line.chars() {
                char_vec.push(c);
            }
            char_vec
        })
        .collect::<Vec<Vec<char>>>();
    let mut sum = 0;
    for i in 0..data[0].len() {
        let mut slide_idx = 0;
        for j in 0..data.len() {
            if data[j][i] == '#' {
                slide_idx = j + 1;
            } else if data[j][i] == 'O' {
                sum += data.len() - slide_idx;
                slide_idx += 1;
            }
        }
    }
    println!("{sum}");
}
