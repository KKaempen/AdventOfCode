use std::fs;
use std::collections::VecDeque;

fn main() {
    let data = fs::read_to_string("problem21.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let data = data
        .iter()
        .map(|line| {
            let mut char_vec = Vec::<char>::new();
            for c in line.chars() {
                char_vec.push(c);
            }
            char_vec
        })
        .collect::<Vec<_>>();
    let mut visited = Vec::<Vec<Option<u32>>>::new();
    for line in data.iter() {
        let mut visited_vec = Vec::<Option<u32>>::new();
        for _ in line {
            visited_vec.push(None);
        }
        visited.push(visited_vec);
    }
    let mut start_point = None;
    for i in 0..data.len() {
        for j in 0..data[0].len() {
            if data[i][j] == 'S' {
                start_point = Some((i, j));
            }
        }
    }
    let start_point = start_point.expect("Error: Couldn't find S in grid");
    let mut q = VecDeque::<(u32, (usize, usize))>::new();
    q.push_back((0, start_point));
    while let Some((
        dist,
        curr_pos
    )) = q.pop_front() {
        if visited[curr_pos.0][curr_pos.1] != None {
            continue;
        }
        visited[curr_pos.0][curr_pos.1] = Some(dist);
        for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)] {
            let next_pos = ((curr_pos.0 as i32) + dir.0, (curr_pos.1 as i32) + dir.1);
            match next_pos {
                (x, y) if (x >= 0
                    && x < data.len() as i32
                    && y >= 0
                    && y < data.len() as i32
                    && data[x as usize][y as usize] != '#') => {
                    q.push_back((dist + 1, (x as usize, y as usize)));
                },
                _ => { }
            }
        }
    }
    let mut sum = 0;
    for line in visited {
        for v in line {
            match v {
                Some(x) if x % 2 == 0 && x <= 64 => {
                    sum += 1;
                },
                _ => { }
            }
        }
    }
    println!("{sum}");
}
