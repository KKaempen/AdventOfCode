use std::fs;
use std::collections::HashMap;

fn main() {
    let data = fs::read_to_string("problem10.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n');
    let pipe_map = HashMap::<((i32, i32), char), (i32, i32)>::from([
        (((0, 1), '-'), (0, 1)),
        (((0, -1), '-'), (0, -1)),
        (((1, 0), '|'), (1, 0)),
        (((-1, 0), '|'), (-1, 0)),
        (((0, 1), 'J'), (-1, 0)),
        (((1, 0), 'J'), (0, -1)),
        (((0, -1), 'F'), (1, 0)),
        (((-1, 0), 'F'), (0, 1)),
        (((0, -1), 'L'), (-1, 0)),
        (((1, 0), 'L'), (0, 1)),
        (((0, 1), '7'), (1, 0)),
        (((-1, 0), '7'), (0, -1)),
    ]);
    let mut map = Vec::<Vec<char>>::new();
    for line in data {
        let mut map_row = Vec::<char>::new();
        for c in line.chars() {
            map_row.push(c);
        }
        map.push(map_row);
    }

    let mut start = None;
    for (i, line) in map.iter().enumerate() {
        for (j, c) in line.iter().enumerate() {
            if *c == 'S' {
                start = Some((i, j));
            }
        }
    }
    let start = start.expect("Error: Did not find starting point in grid");

    let (x, y) = start;
    let mut start_up = false;
    let mut start_down = false;
    let mut start_left = false;
    let mut start_right = false;
    let mut curr = None;
    let mut dir = None;
    if x < map.len() - 1 {
        match pipe_map.get(&((1, 0), map[x + 1][y])) {
            Some(d) => {
                start_down = true;
                curr = Some((x + 1, y));
                dir = Some(d);
            },
            None => { }
        }
    }
    if x > 0 {
        match pipe_map.get(&((-1, 0), map[x - 1][y])) {
            Some(d) => {
                start_up = true;
                curr = Some((x - 1, y));
                dir = Some(d);
            },
            None => { }
        }
    }
    if y < map[0].len() - 1 {
        match pipe_map.get(&((0, 1), map[x][y + 1])) {
            Some(d) => {
                start_right = true;
                curr = Some((x, y + 1));
                dir = Some(d);
            },
            None => { }
        }
    }
    if y > 0 {
        match pipe_map.get(&((0, -1), map[x][y - 1])) {
            Some(d) => {
                start_left = true;
                curr = Some((x, y - 1));
                dir = Some(d);
            },
            None => { }
        }
    }
    let mut curr = curr.expect("Error: Did not find path adjacent to starting point");
    let mut dir = dir.expect("Error: Did not find path adjacent to starting point");

    let mut reduced_map = Vec::<Vec<char>>::new();
    for row in map.iter() {
        let mut reduced_row = Vec::<char>::new();
        for _ in row.iter() {
            reduced_row.push('.');
        }
        reduced_map.push(reduced_row);
    }

    loop {
        reduced_map[curr.0][curr.1] = map[curr.0][curr.1];
        curr = (((curr.0 as i32) + dir.0) as usize, ((curr.1 as i32) + dir.1) as usize);
        match pipe_map.get(&(*dir, map[curr.0][curr.1])) {
            Some(d) => {
                dir = d;
            },
            None => {
                if curr == start {
                    break;
                } else {
                    println!("Error: Did not find path through {:?} from direction {:?}", curr, dir);
                }
            }
        }
    }

    reduced_map[x][y] = match (start_up, start_down, start_left, start_right) {
        (true, true, false, false) => { '|' },
        (true, false, true, false) => { 'J' },
        (true, false, false, true) => { 'L' },
        (false, true, true, false) => { '7' },
        (false, true, false, true) => { 'F' },
        (false, false, true, true) => { '-' },
        _ => { 
            println!("Error: Starting point led in three or more directions");
            'S'
        }
    };

    let mut num_internal = 0;
    for line in reduced_map {
        for (j, c) in line.iter().enumerate() {
            if *c != '.' || j == 0 {
                continue;
            }
            let mut num_crossings = 0;
            let mut last_bend = None;
            for k in (0..j).rev() {
                match line[k] {
                    '|' => {
                        num_crossings += 1;
                    },
                    'J' | '7' => {
                        if !last_bend.is_none() {
                            println!("Error: Encountered starting bend before closing bend, starting from index {j}");
                        }
                        last_bend = Some(line[k]);
                    },
                    'F' => {
                        match last_bend {
                            Some(bend_char) => {
                                if bend_char == 'J' {
                                    num_crossings += 1;
                                }
                                last_bend = None;
                            },
                            None => {
                                println!("Error: Encountered closing bend without preceding starting bend, starting from index {j}");
                            }
                        }
                    },
                    'L' => {
                        match last_bend {
                            Some(bend_char) => {
                                if bend_char == '7' {
                                    num_crossings += 1;
                                }
                                last_bend = None;
                            },
                            None => {
                                println!("Error: Encountered closing bend without preceding starting bend, starting from index {j}");
                            }
                        }
                    },
                    '-' => { },
                    _ => {
                        if !last_bend.is_none() {
                            println!("Error: Encountered non-path space before closing bend, starting from index {j}");
                        }
                        last_bend = None; 
                    }
                }
            }
            if num_crossings % 2 == 1 {
                num_internal += 1;
            }
        }
    }
    println!("{num_internal}");
}
