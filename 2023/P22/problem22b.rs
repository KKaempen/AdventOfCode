use std::fs;
use std::cmp::{min, max};

fn main() {
    let data = fs::read_to_string("problem22.txt")
        .expect("Failed to read file");
    let mut data = data
        .trim()
        .split('\n')
        .map(|line| {
            let two_points = line
                .split('~')
                .collect::<Vec<_>>();
            let p1 = two_points[0];
            let p2 = two_points[1];
            let p1 = p1
                .split(',')
                .map(|v| {
                    v.parse::<usize>().expect("Error: Could not parse value to usize")
                })
                .collect::<Vec<_>>();
            let p2 = p2
                .split(',')
                .map(|v| {
                    v.parse::<usize>().expect("Error: Could not parse value to usize")
                })
                .collect::<Vec<_>>();
            let p1_tup = (p1[0], p1[1], p1[2]);
            let p2_tup = (p2[0], p2[1], p2[2]);
            if p2_tup.0 > p1_tup.0 || p2_tup.1 > p1_tup.1 || p2_tup.2 > p1_tup.2 {
                (p1_tup, p2_tup)
            } else {
                (p2_tup, p1_tup)
            }
        })
        .collect::<Vec<_>>();
    data.sort_by(|a, b| {
        min(&a.0.2, &a.1.2).cmp(min(&b.0.2, &b.1.2))
    });
    let mut max_x = 0;
    let mut max_y = 0;
    let mut max_z = 0;
    for (_, p2) in data.iter() {
        max_x = max(max_x, p2.0);
        max_y = max(max_y, p2.1);
        max_z = max(max_z, p2.2);
    }
    let mut grid = Vec::<Vec<Vec<Option<usize>>>>::new();
    for _ in 0..max_x + 1 {
        let mut slice = Vec::<Vec<Option<usize>>>::new();
        for _ in 0..max_y + 1 {
            let mut row = Vec::<Option<usize>>::new();
            for _ in 0..max_z + 2 {
                row.push(None);
            }
            slice.push(row);
        }
        grid.push(slice);
    }
    for i in 0..max_x + 1 {
        for j in 0..max_y + 1 {
            grid[i][j][0] = Some(data.len());
        }
    }
    let mut new_points = Vec::<((usize, usize, usize), (usize, usize, usize))>::new();
    for (i, (p1, p2)) in data.iter().enumerate() {
        let (mut dx, mut dy, mut dz) = (0, 0, 0);
        let size;
        if p1.0 != p2.0 {
            dx = 1;
            size = p2.0 - p1.0;
        } else if p1.1 != p2.1 {
            dy = 1;
            size = p2.1 - p1.1;
        } else {
            dz = 1;
            size = p2.2 - p1.2;
        }
        let mut new_z_idx = 0;
        for idx in (1..p1.2 + 1).rev() {
            let can_go_below = if dz == 1 {
                match grid[p1.0][p1.1][idx - 1] {
                    Some(_) => { false },
                    None => { true }
                }
            } else {
                let mut val = true;
                for diff in 0..size + 1 {
                    match grid[p1.0 + dx * diff][p1.1 + dy * diff][idx - 1] {
                        Some(_) => { val = false; },
                        None => { }
                    }
                }
                val
            };
            if !can_go_below {
                new_z_idx = idx;
                break;
            }
        }
        for diff in 0..size + 1 {
            grid[p1.0 + dx * diff][p1.1 + dy * diff][new_z_idx + dz * diff] = Some(i);
        }
        new_points.push(((p1.0, p1.1, new_z_idx), (p2.0, p2.1, new_z_idx + dz * size)));
    }
    let mut sum = 0;
    'main_loop: for (i, (p1, p2)) in new_points.iter().enumerate() {
        let (mut dx, mut dy, mut dz) = (0, 0, 0);
        let size;
        if p1.0 != p2.0 {
            dx = 1;
            size = p2.0 - p1.0;
        } else if p1.1 != p2.1 {
            dy = 1;
            size = p2.1 - p1.1;
        } else {
            dz = 1;
            size = p2.2 - p1.2;
        }
        if dz == 1 {
            let above = grid[p2.0][p2.1][p2.2 + 1];
            match above {
                None => {
                    sum += 1;
                    continue 'main_loop;
                },
                Some(upper_idx) => {
                    let (q1, q2) = new_points[upper_idx];
                    let (mut q_dx, mut q_dy, mut q_dz) = (0, 0, 0);
                    let q_size;
                    if q1.0 != q2.0 {
                        q_dx = 1;
                        q_size = q2.0 - q1.0;
                    } else if q1.1 != q2.1 {
                        q_dy = 1;
                        q_size = q2.1 - q1.1;
                    } else {
                        q_dz = 1;
                        q_size = q2.2 - q1.2;
                    }
                    if q_dz == 1 {
                        continue 'main_loop;
                    }
                    for diff in 0..q_size + 1 {
                        match grid[q1.0 + q_dx * diff][q1.1 + q_dy * diff][q1.2 - 1] {
                            Some(supp_idx) if supp_idx != i => {
                                sum += 1;
                                continue 'main_loop;
                            },
                            _ => { }
                        }
                    }
                }
            }
        } else {
            'inner_loop: for diff in 0..size + 1 {
                let above = grid[p1.0 + dx * diff][p1.1 + dy * diff][p1.2 + 1];
                match above {
                    None => { },
                    Some(upper_idx) => {
                        let (q1, q2) = new_points[upper_idx];
                        let (mut q_dx, mut q_dy, mut q_dz) = (0, 0, 0);
                        let q_size;
                        if q1.0 != q2.0 {
                            q_dx = 1;
                            q_size = q2.0 - q1.0;
                        } else if q1.1 != q2.1 {
                            q_dy = 1;
                            q_size = q2.1 - q1.1;
                        } else {
                            q_dz = 1;
                            q_size = q2.2 - q1.2;
                        }
                        if q_dz == 1 {
                            continue 'main_loop;
                        }
                        for q_diff in 0..q_size + 1 {
                            match grid[q1.0 + q_dx * q_diff][q1.1 + q_dy * q_diff][q1.2 - 1] {
                                Some(supp_idx) if supp_idx != i => {
                                    continue 'inner_loop;
                                },
                                _ => { }
                            }
                        }
                        continue 'main_loop;
                    }
                }
            }
            sum += 1;
        }
    }
    println!("{sum}");
}
