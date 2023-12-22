use std::fs;
use std::collections::HashMap;

fn main() {
    let data = fs::read_to_string("problem14.txt")
        .expect("Failed to read file");
    let mut data = data
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
    let mut seen_arrangements = HashMap::<Vec<(usize, usize)>, usize>::new();
    let mut cycle_idx = 0;
    let mut sum = 0;
    loop {
        let mut new_arrangement = Vec::<(usize, usize)>::new();
        for (i, line) in data.iter().enumerate() {
            for (j, c) in line.iter().enumerate() {
                if *c == 'O' {
                    new_arrangement.push((i, j));
                }
            }
        }
        match seen_arrangements.get(&new_arrangement) {
            Some(idx) => {
                let mod_val = cycle_idx - idx;
                let billion_state = (1000000000 - idx) % mod_val + idx;
                for (state, cycle_val) in &seen_arrangements {
                    if *cycle_val == billion_state {
                        for (x, _) in state {
                            sum += data.len() - x;
                        }
                        break;
                    }
                }
                break;
            },
            None => {
                seen_arrangements.insert(new_arrangement, cycle_idx);
            }
        }
        for i in 0..data[0].len() {
            let mut slide_idx = 0;
            for j in 0..data.len() {
                if data[j][i] == '#' {
                    slide_idx = j + 1;
                } else if data[j][i] == 'O' {
                    data[j][i] = '.';
                    data[slide_idx][i] = 'O';
                    slide_idx += 1;
                }
            }
        }
        for i in 0..data.len() {
            let mut slide_idx = 0;
            for j in 0..data[0].len() {
                if data[i][j] == '#' {
                    slide_idx = j + 1;
                } else if data[i][j] == 'O' {
                    data[i][j] = '.';
                    data[i][slide_idx] = 'O';
                    slide_idx += 1;
                }
            }
        }
        for i in 0..data[0].len() {
            let mut slide_idx = data.len() - 1;
            for j in (0..data.len()).rev() {
                if data[j][i] == '#' {
                    if j > 0 {
                        slide_idx = j - 1;
                    }
                } else if data[j][i] == 'O' {
                    data[j][i] = '.';
                    data[slide_idx][i] = 'O';
                    if slide_idx > 0 {
                        slide_idx -= 1;
                    }
                }
            }
        }
        for i in 0..data.len() {
            let mut slide_idx = data[0].len() - 1;
            for j in (0..data[0].len()).rev() {
                if data[i][j] == '#' {
                    if j > 0 {
                        slide_idx = j - 1;
                    }
                } else if data[i][j] == 'O' {
                    data[i][j] = '.';
                    data[i][slide_idx] = 'O';
                    if slide_idx > 0 {
                        slide_idx -= 1;
                    }
                }
            }
        }
        cycle_idx += 1;
    }
    println!("{sum}");
}
