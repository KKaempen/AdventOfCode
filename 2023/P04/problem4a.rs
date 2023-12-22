use std::fs;

fn main() {
    let data = fs::read_to_string("problem4.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n')
        .collect::<Vec<_>>();
    let mut sum = 0;
    for line in data {
        let card = line.split(": ").collect::<Vec<_>>()[1];
        let vec = card.split(" | ").collect::<Vec<_>>();
        let wins = vec[0].split(" ").collect::<Vec<_>>();
        let wins = wins.iter().filter(|&&x| x != "").collect::<Vec<_>>();
        let mine = vec[1];
        let mut val = 0;
        for v in mine.split(" ") {
            match wins.iter().find(|&&x| x == &v) {
                Some(_) => {
                    if val == 0 {
                        val = 1;
                    } else {
                        val *= 2;
                    }
                },
                None => {}
           }
        }
        sum += val;
    }
    println!("{sum}");
}
