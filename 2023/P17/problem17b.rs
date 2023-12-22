use std::fs;
use std::collections::{BinaryHeap, HashMap};
use std::cmp::Reverse;

fn main() {
    let data = fs::read_to_string("problem17.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .map(|line| {
            let mut line_digits = Vec::<u32>::new();
            for c in line.chars() {
                line_digits.push((c as u32) - ('0' as u32));
            }
            line_digits
        })
        .collect::<Vec<Vec<u32>>>();

    let dir_index_map = HashMap::<(i32, i32), usize>::from([
        ((-1, 0), 0),
        ((1, 0), 1),
        ((0, -1), 2),
        ((0, 1), 3),
    ]);

    let mut visited = Vec::<Vec<[bool; 40]>>::new();
    for line in data.iter() {
        let mut visited_row = Vec::<[bool; 40]>::new();
        for _ in line {
            visited_row.push([false; 40]);
        }
        visited.push(visited_row);
    }

    let w = data.len() as i32;
    let h = data[0].len() as i32;

    let mut heap = BinaryHeap::new();
    let start_v_right = data[0][1];
    let start_v_down = data[1][0];
    heap.push((Reverse(start_v_right), (0, 1), (0, 1), 1));
    heap.push((Reverse(start_v_down), (1, 0), (1, 0), 1));
    let mut total_dist = 0;
    while let Some((
        Reverse(curr_dist),
        loc,
        dir,
        num_straight
    )) = heap.pop() {
        let visited_idx = dir_index_map[&dir] * 10 + num_straight - 1;
        if visited[loc.0][loc.1][visited_idx] {
            continue;
        }
        visited[loc.0][loc.1][visited_idx] = true;
        if loc.0 == data.len() - 1 && loc.1 == data[0].len() - 1 {
            if num_straight >= 4 {
                total_dist = curr_dist;
                break;
            }
        }
        for new_dir in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
            if new_dir == (-dir.0, -dir.1) {
                continue;
            }
            let mut new_num_straight = 1;
            if new_dir == dir {
                if num_straight == 10 {
                    continue;
                }
                new_num_straight = num_straight + 1;
            } else {
                if num_straight < 4 {
                    continue;
                }
            }
            let (new_x, new_y) = ((loc.0 as i32) + new_dir.0, (loc.1 as i32) + new_dir.1);
            match (new_x, new_y) {
                (x, y) if (x >= 0 && y >= 0 && x < w && y < h) => {
                    let new_loc = (x as usize, y as usize);
                    let new_dist = curr_dist + data[new_loc.0][new_loc.1];
                    heap.push((Reverse(new_dist), new_loc, new_dir, new_num_straight));
                },
                _ => { }
            }
        }
    }
    println!("{total_dist}");
}
