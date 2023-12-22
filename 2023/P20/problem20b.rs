use std::fs;

fn main() {
    let data = fs::read_to_string("problem20.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n');
}
