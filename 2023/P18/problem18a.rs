use std::fs;
use std::cmp::{max, min};
use std::collections::HashMap;

fn main() {
    let data = fs::read_to_string("problem18.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .map(|line| {
            let split_inst = line.split(' ').collect::<Vec<_>>();
            let dig_inst = (
                split_inst[0]
                    .chars()
                    .last()
                    .expect("Error: Instruction string has empty direction"),
                split_inst[1]
                    .parse::<usize>()
                    .expect("Could not parse integer"),
                split_inst[2]
            );
            dig_inst
        })
        .collect::<Vec<_>>();
    let inst_dir_map = HashMap::<char, (i32, i32)>::from([
        ('U', (-1, 0)),
        ('D', (1, 0)),
        ('L', (0, -1)),
        ('R', (0, 1))
    ]);
    let mut max_x_val = 0;
    let mut min_x_val = 0;
    let mut max_y_val = 0;
    let mut min_y_val = 0;
    let mut curr_x_val = 0;
    let mut curr_y_val = 0;
    for inst in data.iter() {
        match inst.0 {
            'U' => {
                curr_x_val -= inst.1 as i32;
                min_x_val = min(min_x_val, curr_x_val);
            },
            'D' => {
                curr_x_val += inst.1 as i32;
                max_x_val = max(max_x_val, curr_x_val);
            },
            'L' => {
                curr_y_val -= inst.1 as i32;
                min_y_val = min(min_y_val, curr_y_val);
            },
            'R' => {
                curr_y_val += inst.1 as i32;
                max_y_val = max(max_y_val, curr_y_val);
            },
            _ => {
                println!("Error: Found instruction character that isn't UDLR: {}", inst.0);
            }
        }
    }
    let mut curr_pos = (-min_x_val as usize, -min_y_val as usize);
    let mut map = Vec::<Vec<bool>>::new();
    for _ in min_x_val..max_x_val + 1 {
        let mut map_row = Vec::<bool>::new();
        for _ in min_y_val..max_y_val + 1 {
            map_row.push(false);
        }
        map.push(map_row);
    }
    map[curr_pos.0][curr_pos.1] = true;
    for inst in data {
        for _ in 0..inst.1 {
            let dir = inst_dir_map[&inst.0];
            curr_pos = (((curr_pos.0 as i32) + dir.0) as usize, ((curr_pos.1 as i32) + dir.1) as usize);
            map[curr_pos.0][curr_pos.1] = true;
        }
    }
    let mut internal_pos = None;
    'big_loop: for (i, line) in map.iter().enumerate() {
        for j in 0..line.len() - 1 {
            if line[j] && !line[j + 1] && (j == 0 || !line[j - 1]) {
                internal_pos = Some((i, j + 1));
                break 'big_loop;
            }
        }
    }
    let start_pos = internal_pos.expect("Could not find point internal to border");
    let mut stack = Vec::<(usize, usize)>::new();
    stack.push(start_pos);
    while let Some(curr_pos) = stack.pop() {
        if map[curr_pos.0][curr_pos.1] {
            continue;
        }
        map[curr_pos.0][curr_pos.1] = true;
        for (_, dir) in inst_dir_map.iter() {
            let (new_x, new_y) = ((curr_pos.0 as i32) + dir.0, (curr_pos.1 as i32) + dir.1);
            if new_x < 0
                || new_x >= map.len() as i32
                || new_y < 0
                || new_y >= map[0].len() as i32
            {
                continue;
            }
            stack.push((new_x as usize, new_y as usize));
        }
    }
    let mut sum = 0;
    for line in map.iter() {
        for b in line {
            if *b {
                sum += 1;
            }
        }
    }
 
//    for line in map {
//        for b in line {
//            if b {
//                print!("#");
//            } else {
//                print!(".");
//            }
//        }
//        println!("");
//    }
    println!("{sum}");
}
