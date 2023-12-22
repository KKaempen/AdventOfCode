use std::fs;

fn main() {
    let data = fs::read_to_string("problem5.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let seeds = data[0]
        .split(": ")
        .collect::<Vec<_>>()[1];
    let tmp_seeds = seeds
        .split(" ")
        .map(|x|
            x.parse::<u64>()
            .expect("Failed to parse initial seeds")
        )
        .collect::<Vec<_>>();
    let mut seeds: Vec<(u64, u64)> = Vec::<(u64, u64)>::new();
    for i in 0..tmp_seeds.len() / 2 {
        seeds.push((tmp_seeds[i * 2], tmp_seeds[i * 2 + 1]));
    }
    let mut maps: Vec<Vec<(u64, u64, u64)>> = Vec::<Vec<(u64, u64, u64)>>::new();
    let mut data_iter = data.iter();
    let mut idx = data_iter.position(|&x| x.trim() == "").expect("Did not find");
    for _ in 0..7 {
        let idx_diff = match data_iter.position(|&x| x.trim() == "") {
            Some(d) => { d },
            None => { data.len() - 1 - idx }
        };
        let mut map: Vec<(u64, u64, u64)> = Vec::<(u64, u64, u64)>::new();
        for j in idx + 2..idx + 1 + idx_diff {
            let row = data[j]
                .split(" ")
                .map(|x|
                    x.parse::<u64>()
                    .expect("Failed to parse map row")
                )
                .collect::<Vec<_>>();
            let row: (u64, u64, u64) = (row[0], row[1], row[2]);
            map.push(row);
        }
        map.sort_by(|x, y| x.1.cmp(&y.1));
        maps.push(map);
        idx += 1 + idx_diff;
    }
    for map in maps {
        let mut next_seeds: Vec<(u64, u64)> = Vec::<(u64, u64)>::new();
        let min_val = map[0].1;
        'seed_loop: for (v, l) in seeds.iter() {
            let mut val: u64 = *v;
            let mut len: u64 = *l;
            if val + len <= min_val {
                next_seeds.push((val, len));
                continue 'seed_loop;
            } else if val < min_val {
                next_seeds.push((val, min_val - val));
                len -= min_val - val;
                val = min_val;
            }
            for tup in map.iter() {
                if val >= tup.1 && val < tup.1 + tup.2 {
                    let new_val = val - tup.1 + tup.0;
                    if val + len <= tup.1 + tup.2 {
                        next_seeds.push((new_val, len));
                        continue 'seed_loop;
                    } else {
                        next_seeds.push((new_val, tup.1 + tup.2 - val));
                        len -= tup.1 + tup.2 - val;
                        val = tup.1 + tup.2;
                    }
                }
            }
            next_seeds.push((val, len));
        }
        seeds = next_seeds;
    }
    match seeds.iter().min() {
        Some(m) => { println!("{}", m.0) },
        None => { println!("Something went horribly wrong") }
    }
}
