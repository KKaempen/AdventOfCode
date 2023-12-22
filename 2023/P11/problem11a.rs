use std::fs;

fn main() {
    let data = fs::read_to_string("problem11.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n');
    let mut map = Vec::<Vec<char>>::new();
    for line in data {
        let mut map_row = Vec::<char>::new();
        for c in line.chars() {
            map_row.push(c);
        }
        map.push(map_row);
    }
    let mut empty_cols = Vec::<usize>::new();
    let mut empty_rows = Vec::<usize>::new();
    for (i, row) in map.iter().enumerate() {
        let mut is_empty = true;
        for c in row {
            if *c == '#' {
                is_empty = false;
            }
        }
        if is_empty {
            empty_rows.push(i);
        }
    }
    for j in 0..map[0].len() {
        let mut is_empty = true;
        for i in 0..map.len() {
            if map[i][j] == '#' {
                is_empty = false;
            }
        }
        if is_empty {
            empty_cols.push(j);
        }
    }
    let mut adj_map = Vec::<Vec<char>>::new();
    let mut row_idx = 0;
    for (i, row) in map.iter().enumerate() {
        let mut adj_row = Vec::<char>::new();
        let mut col_idx = 0;
        for (j, c) in row.iter().enumerate() {
            adj_row.push(*c);
            if col_idx < empty_cols.len() && empty_cols[col_idx] == j {
                adj_row.push('.');
                col_idx += 1;
            }
        }
        adj_map.push(adj_row);
        if row_idx < empty_rows.len() && empty_rows[row_idx] == i {
            let row_len = map[0].len() + empty_cols.len();
            let mut empty_row = Vec::<char>::new();
            for _ in 0..row_len {
                empty_row.push('.');
            }
            adj_map.push(empty_row);
            row_idx += 1;
        }
    }
    let mut galaxy_locs = Vec::<(i32, i32)>::new();
    for (i, row) in adj_map.iter().enumerate() {
        for (j, c) in row.iter().enumerate() {
            if *c == '#' {
                galaxy_locs.push((i as i32, j as i32));
            }
        }
    }
    let mut sum = 0;
    for (i, (x1, y1)) in galaxy_locs.iter().enumerate() {
        for (x2, y2) in galaxy_locs[i + 1..].iter() {
            sum += (x2 - x1).abs() + (y2 - y1).abs();
        }
    }
    println!("{sum}");
}
