use std::fs;
use std::collections::HashMap;

fn main() {
    let data = fs::read_to_string("problem8.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let insts = data[0];
    let mut data_map = HashMap::<String, (String, String)>::new();
    let data = &data[2..];
    for line in data {
        let parts = line
            .split(" = ")
            .collect::<Vec<_>>();
        let key = parts[0];
        let l = parts[1].len();
        let l_r_vec = parts[1][1..l - 1]
            .split(", ")
            .collect::<Vec<_>>();
        let l = l_r_vec[0];
        let r = l_r_vec[1];
        data_map.insert((*key).to_string(), ((*l).to_string(), (*r).to_string()));
    }
    let mut curr_char = insts.chars();
    let mut curr = "AAA";
    let mut steps = 0;
    while curr != "ZZZ" {
        let pair = data_map.get(curr);
        match pair {
            Some(s) => {
                match curr_char.next() {
                    Some(c) => { 
                        match c {
                            'L' => { curr = &s.0; },
                            'R' => { curr = &s.1; },
                            _ => { println!("Error: {c} is not L or R"); }
                        }
                    },
                    None => {
                        curr_char = insts.chars();
                        continue;
                    }
                }
                steps += 1;
            },
            None => {
                println!("Error: {curr} not found in data_map");
            }
        }
    }
    println!("{steps}");
}
