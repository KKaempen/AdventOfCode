use std::fs;
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
    let inst_dir_arr = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ];
    
    let hex_chars = HashMap::<char, usize>::from([
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('a', 10),
        ('b', 11),
        ('c', 12),
        ('d', 13),
        ('e', 14),
        ('f', 15)
    ]);

    // Use a shoelace theorem to calculate area, then use Pick's
    // theorem A = i + b/2 - 1 to get that the interior + boundary
    // points is equal to i + b = A + b/2 + 1
    let mut area: i64 = 0;
    let mut boundary_points: i64 = 0;
    let mut curr_point = (0, 0);
    for (_, _, inst) in data {
        let mut char_iter = inst.chars();
        char_iter.next();
        char_iter.next();
        let mut dist_val: i64 = 0; 
        for _ in 0..5 {
            let c = char_iter.next().expect("Error: Ran out of characters in hex instruction early");
            dist_val = dist_val * 16 + (hex_chars[&c] as i64);
        }
        let c = char_iter.next().expect("Error: Ran out of characters in hex instruction early");
        let dir = inst_dir_arr[hex_chars[&c]];
        let dir = (dir.0 * dist_val, dir.1 * dist_val);
        let next_point = (curr_point.0 + dir.0, curr_point.1 + dir.1);
        boundary_points += dist_val;
        area += curr_point.0 * next_point.1 - curr_point.1 * next_point.0;
        curr_point = next_point;
    }
    area = (area / 2).abs();
    let total_points = area + boundary_points / 2 + 1;
    println!("{total_points}");
}
