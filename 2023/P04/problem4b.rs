use std::fs;

fn main() {
    let data = fs::read_to_string("problem4.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n')
        .collect::<Vec<_>>();
    let mut copies: Vec<i64> = Vec::new();
    for _ in &data {
        copies.push(1);
    }
    let mut sum = 0;
    for (i, line) in data.iter().enumerate() {
        sum += copies[i];
        let card = line.split(": ").collect::<Vec<_>>()[1];
        let vec = card.split(" | ").collect::<Vec<_>>();
        let wins = vec[0].split(" ").collect::<Vec<_>>();
        let wins = wins.iter().filter(|&&x| x != "").collect::<Vec<_>>();
        let mine = vec[1];
        let mut num_matches = 0;
        for v in mine.split(" ") {
            match wins.iter().find(|&&x| x == &v) {
                Some(_) => {
                    num_matches += 1;
                },
                None => {}
           }
        }
        for j in 0..num_matches {
            copies[i + 1 + j] += copies[i];
        }
    }
    println!("{sum}");
}
