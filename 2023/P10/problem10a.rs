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
    let mut curr = None;
    let mut dir = None;
    if x < map.len() - 1 {
        match pipe_map.get(&((1, 0), map[x + 1][y])) {
            Some(d) => {
                curr = Some((x + 1, y));
                dir = Some(d);
            },
            None => { }
        }
    }
    if x > 0 {
        match pipe_map.get(&((-1, 0), map[x - 1][y])) {
            Some(d) => {
                curr = Some((x - 1, y));
                dir = Some(d);
            },
            None => { }
        }
    }
    if y < map[0].len() - 1 {
        match pipe_map.get(&((0, 1), map[x][y + 1])) {
            Some(d) => {
                curr = Some((x, y + 1));
                dir = Some(d);
            },
            None => { }
        }
    }
    if y > 0 {
        match pipe_map.get(&((0, -1), map[x][y - 1])) {
            Some(d) => {
                curr = Some((x, y - 1));
                dir = Some(d);
            },
            None => { }
        }
    }
    let mut curr = curr.expect("Error: Did not find path adjacent to starting point");
    let mut dir = dir.expect("Error: Did not find path adjacent to starting point");
    let mut path_len = 1;
    loop {
        path_len += 1;
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
    println!("{}", path_len / 2);
}
