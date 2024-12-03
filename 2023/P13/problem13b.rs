use std::fs;
use std::cmp::min;

fn main() {
    let data = fs::read_to_string("problem13.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let data = data
        .split(|x| *x == "")
        .map(|grid| {
            let mut grid_vec = Vec::<Vec<char>>::new();
            for line in grid {
                let mut line_vec = Vec::<char>::new();
                for c in line.chars() {
                    line_vec.push(c);
                }
                grid_vec.push(line_vec);
            }
            grid_vec
        })
        .collect::<Vec<_>>();
    let mut sum = 0;
    'data_iter: for grid in data {
        for split_row in 1..grid.len() {
            let mut num_diffs = 0;
            for j in 0..min(split_row, grid.len() - split_row) {
                for (c1, c2) in grid[split_row - j - 1].iter().zip(grid[split_row + j].iter()) {
                    if c1 != c2 {
                        num_diffs += 1;
                    }
                }
            }
            if num_diffs == 1 {
                sum += 100 * (split_row as u32);
                continue 'data_iter;
            }
        }
        
        for split_row in 1..grid[0].len() {
            let mut num_diffs = 0;
            for j in 0..min(split_row, grid[0].len() - split_row) {
                for k in 0..grid.len() {
                    if grid[k][split_row - j - 1] != grid[k][split_row + j] {
                        num_diffs += 1;
                    }
                }
            }
            if num_diffs == 1 {
                sum += split_row as u32;
                continue 'data_iter;
            }
        }
    }
    println!("{sum}");
}