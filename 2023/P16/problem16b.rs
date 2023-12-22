use std::fs;
use std::collections::HashMap;

fn main() {
    let data = fs::read_to_string("problem16.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .map(|x| {
            let mut char_vec = Vec::<char>::new();
            for c in x.chars() {
                char_vec.push(c);
            }
            char_vec
        })
        .collect::<Vec<_>>();
    let dir_map = HashMap::<(i32, i32), usize>::from([
        ((0, 1), 0),
        ((0, -1), 1),
        ((1, 0), 2),
        ((-1, 0), 3)
    ]);
    let w = data.len() as i32;
    let h = data[0].len() as i32;

    let mut max_sum = 0;
    for initial_idx in 0..data.len() {
        for (initial_dir, initial_loc) in [
            ((0, 1), (initial_idx, 0)),
            ((0, -1), (initial_idx, data.len() - 1)),
            ((1, 0), (0, initial_idx)),
            ((-1, 0), (data.len() - 1, initial_idx))
        ] {
            let mut stack = Vec::<((i32, i32), (usize, usize))>::new();
            stack.push((initial_dir, initial_loc));
            let mut lit_tiles = Vec::<Vec<[bool; 4]>>::new();
            for line in data.iter() {
                let mut lit_row = Vec::<[bool; 4]>::new();
                for _ in line {
                    lit_row.push([false, false, false, false]);
                }
                lit_tiles.push(lit_row);
            }
            while let Some((
                dir,
                loc
            )) = stack.pop() {
                let lit_idx = dir_map[&dir];
                if lit_tiles[loc.0][loc.1][lit_idx] {
                    continue;
                }
                lit_tiles[loc.0][loc.1][lit_idx] = true;
                match data[loc.0][loc.1] {
                    '\\' => {
                        let new_dir = (dir.1, dir.0);
                        let (new_x, new_y) = ((loc.0 as i32) + new_dir.0, (loc.1 as i32) + new_dir.1);
                        match (new_x, new_y) {
                            (x, y) if (x >= 0 && y >= 0 && x < w && y < h) => {
                                let new_loc = (x as usize, y as usize);
                                stack.push((new_dir, new_loc));
                            },
                            _ => { }
                        }
                    },
                    '/' => {
                        let new_dir = (-dir.1, -dir.0);
                        let (new_x, new_y) = ((loc.0 as i32) + new_dir.0, (loc.1 as i32) + new_dir.1);
                        match (new_x, new_y) {
                            (x, y) if (x >= 0 && y >= 0 && x < w && y < h) => {
                                let new_loc = (x as usize, y as usize);
                                stack.push((new_dir, new_loc));
                            },
                            _ => { }
                        }
                    },
                    '|' => {
                        match dir.1 {
                            0 => {
                                let (new_x, new_y) = ((loc.0 as i32) + dir.0, (loc.1 as i32) + dir.1);
                                match (new_x, new_y) {
                                    (x, y) if (x >= 0 && y >= 0 && x < w && y < h) => {
                                        let new_loc = (x as usize, y as usize);
                                        stack.push((dir, new_loc));
                                    },
                                    _ => { }
                                }
                            },
                            _ => {
                                let dir1 = (-1, 0);
                                let dir2 = (1, 0);
                                for d in [dir1, dir2] {
                                    let (new_x, new_y) = ((loc.0 as i32) + d.0, (loc.1 as i32) + d.1);
                                    match (new_x, new_y) {
                                        (x, y) if (x >= 0 && y >= 0 && x < w && y < h) => {
                                            let new_loc = (x as usize, y as usize);
                                            stack.push((d, new_loc));
                                        },
                                        _ => { }
                                    }
                                }
                            }
                        }
                    },
                    '-' => {
                        match dir.0 {
                            0 => {
                                let (new_x, new_y) = ((loc.0 as i32) + dir.0, (loc.1 as i32) + dir.1);
                                match (new_x, new_y) {
                                    (x, y) if (x >= 0 && y >= 0 && x < w && y < h) => {
                                        let new_loc = (x as usize, y as usize);
                                        stack.push((dir, new_loc));
                                    },
                                    _ => { }
                                }
                            },
                            _ => {
                                let dir1 = (0, -1);
                                let dir2 = (0, 1);
                                for d in [dir1, dir2] {
                                    let (new_x, new_y) = ((loc.0 as i32) + d.0, (loc.1 as i32) + d.1);
                                    match (new_x, new_y) {
                                        (x, y) if (x >= 0 && y >= 0 && x < w && y < h) => {
                                            let new_loc = (x as usize, y as usize);
                                            stack.push((d, new_loc));
                                        },
                                        _ => { }
                                    }
                                }
                            }
                        }
                    },
                    _ => {
                        let (new_x, new_y) = ((loc.0 as i32) + dir.0, (loc.1 as i32) + dir.1);
                        match (new_x, new_y) {
                            (x, y) if (x >= 0 && y >= 0 && x < w && y < h) => {
                                let new_loc = (x as usize, y as usize);
                                stack.push((dir, new_loc));
                            },
                            _ => { }
                        }
                    }
                }
            }
            let mut sum = 0;
            for line in lit_tiles {
                for b_vec in line {
                    for b in b_vec {
                        if b {
                            sum += 1;
                            break;
                        }
                    }
                }
            }
            if sum > max_sum {
                max_sum = sum;
            }
        }
    }
    println!("{max_sum}");
}
