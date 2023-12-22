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
    let mut galaxy_locs = Vec::<(usize, usize)>::new();
    for (i, row) in map.iter().enumerate() {
        for (j, c) in row.iter().enumerate() {
            if *c == '#' {
                galaxy_locs.push((i, j));
            }
        }
    }
    let mut sum: i64 = 0;
    for (i, (x1, y1)) in galaxy_locs.iter().enumerate() {
        for (x2, y2) in galaxy_locs[i + 1..].iter() {
            sum += (*x2 as i64 - *x1 as i64).abs() + (*y2 as i64 - *y1 as i64).abs();
            let row_val_1 = match empty_rows.binary_search(x1) {
                Ok(v) => {
                    println!("Error: Row {x1} containing galaxy was found as empty");
                    v as i64
                },
                Err(v) => { v as i64 }
            };
            let row_val_2 = match empty_rows.binary_search(x2) {
                Ok(v) => {
                    println!("Error: Row {x2} containing galaxy was found as empty");
                    v as i64
                },
                Err(v) => { v as i64 }
            };
            let col_val_1 = match empty_cols.binary_search(y1) {
                Ok(v) => {
                    println!("Error: Row {y1} containing galaxy was found as empty");
                    v as i64
                },
                Err(v) => { v as i64 }
            };
            let col_val_2 = match empty_cols.binary_search(y2) {
                Ok(v) => {
                    println!("Error: Row {y2} containing galaxy was found as empty");
                    v as i64
                },
                Err(v) => { v as i64 }
            };
            sum += (row_val_1 - row_val_2).abs() * 999999;
            sum += (col_val_1 - col_val_2).abs() * 999999;
        }
    }
    println!("{sum}");
}
