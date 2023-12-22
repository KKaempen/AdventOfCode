use std::fs;
use std::collections::HashMap;
use std::convert::TryInto;

fn crt(rems: &Vec<u128>, mods: &Vec<u128>) -> u128 {
    let mut big_mod: u128 = 1;
    let mut big_rem: i128 = 0;
    for (m, r_u) in mods.iter().zip(rems.iter()) {
        let r = *r_u as i128;
        let (s1, s2) = gcd_ext(&big_mod, &m);
        big_rem = big_rem * (*m as i128) * s2 + r * (big_mod as i128) * s1;
        big_mod *= m;
        while big_rem < 0 {
            big_rem += big_mod as i128;
        }
        big_rem %= big_mod as i128;
    }
    return big_rem.try_into().unwrap();
}

fn lcm(nums: &Vec<u128>) -> u128 {
    let mut lcm = 1;
    for v in nums {
        let g = gcd(&lcm, &v);
        lcm *= v;
        lcm /= g;
    }
    return lcm;
}

fn gcd(a: &u128, b: &u128) -> u128 {
    let mut m1 = *a;
    let mut m2 = *b;
    while m2 != 0 {
        let r = m1 % m2;
        m1 = m2;
        m2 = r;
    }
    return m1;
}

fn gcd_ext(a: &u128, b: &u128) -> (i128, i128) {
    let mut m1 = *a as i128;
    let mut m2 = *b as i128;
    let mut s1: i128 = 1;
    let mut s2: i128 = 0;
    let mut t1: i128 = 0;
    let mut t2: i128 = 1;
    while m2 != 0 {
        let q = m1 / m2;
        let r1 = m1 - m2 * q;
        let r2 = s1 - s2 * q;
        let r3 = t1 - t2 * q;
        m1 = m2;
        m2 = r1;
        s1 = s2;
        s2 = r2;
        t1 = t2;
        t2 = r3;
    }
    return (s1, t1);
}

fn main() {
    let data = fs::read_to_string("problem8.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let insts = data[0];
    let mut data_map = HashMap::<String, (String, String)>::new();
    let data = &data[2..];
    for line in data {
        let parts = line
            .split(" = ")
            .collect::<Vec<_>>();
        let key = parts[0].to_string();
        let l = parts[1].len();
        let l_r_vec = parts[1][1..l - 1]
            .split(", ")
            .collect::<Vec<_>>();
        let l = l_r_vec[0].to_string();
        let r = l_r_vec[1].to_string();
        data_map.insert(key, (l, r));
    }
    let mut rem_vec = Vec::<u128>::new();
    let mut mod_vec = Vec::<u128>::new();
    for (key, _) in &data_map {
        let c = key.chars().last().unwrap();
        if c != 'A' {
            continue;
        }
        let mut seen_states = HashMap::<(String, u32), u32>::new();
        let mut state_idx = 0;
        let mut curr_char = insts.chars().peekable();
        let mut inst_idx: u32 = 0;
        let mut z_idx = None;
        let mut curr = key;
        loop {
            let state_pair = (curr.clone(), inst_idx);
            match seen_states.get(&state_pair) {
                Some(idx) => {
                    let mod_val = state_idx - idx;
                    let rem_val = z_idx.expect("Error: Did not find an ending value within loop");
                    mod_vec.push(mod_val as u128);
                    rem_vec.push(rem_val as u128);
                    break;
                },
                None => { }
            }
            seen_states.insert(state_pair, state_idx);
            let c = curr.chars().last().unwrap();
            if c == 'Z' {
                if z_idx != None {
                    println!("Error: Found multiple states with char ending in Z");
                }
                z_idx = Some(state_idx);
            }
            state_idx += 1;
            inst_idx += 1;
            let inst_char = curr_char.next().expect("Error: Iterated past end of instructions");
            if curr_char.peek().is_none() {
                curr_char = insts.chars().peekable();
                inst_idx = 0;
            }
            let pair = data_map.get(curr);
            match pair {
                Some(s) => {
                    match inst_char {
                        'L' => {
                            curr = &s.0;
                        },
                        'R' => {
                            curr = &s.1;
                        },
                        _ => { println!("Error: {inst_char} is not L or R"); }
                    }
                },
                None => {
                    println!("Error: {curr} not found in data_map");
                }
            }
        }
    }
    let mut res = crt(&rem_vec, &mod_vec);
    let max = rem_vec.iter().max().expect("Error: rem_vec was empty");
    let lcm = lcm(&mod_vec);
    while res < *max {
        res += lcm;
    }
    println!("{res}");
}
