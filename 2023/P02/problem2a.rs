use std::fs;

fn main() {
    let data = fs::read_to_string("problem2.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n');
    let mut sum = 0;
    'main: for (i, el) in data.enumerate() {
        let games = el.trim().split(": ").collect::<Vec<_>>()[1];
        for g in games.split("; ") {
            let vals = g.split(", ");
            for v_col in vals {
                let vec = v_col.split(" ").collect::<Vec<_>>();
                let v = vec[0];
                let col = vec[1]; 
                match v.parse::<u32>() {
                    Ok(num) => {
                        match col {
                            "red" => {
                                if num > 12 {
                                    continue 'main;
                                }
                            },
                            "green" => {
                                if num > 13 {
                                    continue 'main;
                                }
                            },
                            "blue" => {
                                if num > 14 {
                                    continue 'main;
                                }
                            },
                            _ => {}
                        }
                    },
                    _ => {}
                }
            }
        }
        sum += i + 1;
    }
    println!("{sum}");
}
