use std::fs;
use std::collections::HashMap;
use std::cmp::Ordering;

fn main() {
    let data = fs::read_to_string("problem7.txt")
        .expect("Failed to read file");
    let card_to_val = HashMap::<char, u32>::from([
        ('2', 0),
        ('3', 1),
        ('4', 2),
        ('5', 3),
        ('6', 4),
        ('7', 5),
        ('8', 6),
        ('9', 7),
        ('T', 8),
        ('J', 9),
        ('Q', 10),
        ('K', 11),
        ('A', 12),
    ]);
    let mut data = data
        .trim()
        .split('\n')
        .map(|x| {
            let v = x
                .split(" ")
                .collect::<Vec<_>>();
            (v[0], v[1].parse::<u32>().expect("Couldn't parse to int"))
        })
        .collect::<Vec<_>>();
    data.sort_by(|ta, tb| {
        let a = ta.0;
        let b = tb.0;    
        let mut a_map = HashMap::<char, u32>::new();
        let mut b_map = HashMap::<char, u32>::new();
        for c in a.chars() {
            a_map.insert(c, match a_map.get(&c) {
                Some(num) => { num + 1 },
                None => { 1 }
            });
        }
        for c in b.chars() {
            b_map.insert(c, match b_map.get(&c) {
                Some(num) => { num + 1 },
                None => { 1 }
            });
        }
        let mut a_vec = Vec::<(char, u32)>::new();
        let mut b_vec = Vec::<(char, u32)>::new();
        for (c, num) in a_map {
            a_vec.push((c, num));
        }
        for (c, num) in b_map {
            b_vec.push((c, num));
        }
        a_vec.sort_by(|a, b| {
            match b.1.cmp(&a.1) {
                Ordering::Equal => { card_to_val
                    .get(&b.0)
                    .expect("Didn't find character in card_to_val")
                    .cmp(
                        card_to_val
                            .get(&a.0)
                            .expect("Didn't find character in card_to_val")
                    )
                },
                x => x
            }
        });
        b_vec.sort_by(|a, b| {
            match b.1.cmp(&a.1) {
                Ordering::Equal => { card_to_val
                    .get(&b.0)
                    .expect("Didn't find character in card_to_val")
                    .cmp(
                        card_to_val
                            .get(&a.0)
                            .expect("Didn't find character in card_to_val")
                    )
                },
                x => x
            }
        });
        let a_num_diff = a_vec.len();
        let b_num_diff = b_vec.len();
        if a_num_diff < b_num_diff {
            return Ordering::Greater;
        } else if b_num_diff < a_num_diff {
            return Ordering::Less;
        }
        if a_vec[0].1 > b_vec[0].1 {
            return Ordering::Greater;
        } else if b_vec[0].1 > a_vec[0].1 {
            return Ordering::Less;
        }
        for (a_char, b_char) in a.chars().zip(b.chars()) {
            match card_to_val
                .get(&a_char)
                .expect("Didn't find character {a_char} in card_to_val")
                .cmp(
                    card_to_val
                        .get(&b_char)
                        .expect("Didn't find character {b_char} in card_to_val")
                ) {
                Ordering::Equal => {},
                x => { return x }
            }
        }
        return Ordering::Equal;
    });
    let mut sum = 0;
    for (i, (_, val)) in data.iter().enumerate() {
        sum += (i + 1) as u32 * val;
    }
    println!("{sum}");
}
