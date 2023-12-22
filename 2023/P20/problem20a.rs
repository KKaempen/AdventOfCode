use std::fs;
use std::collections::{BinaryHeap, HashMap};

fn main() {
    let data = fs::read_to_string("problem20.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n');
    let modules = HashMap::<String, (
}
