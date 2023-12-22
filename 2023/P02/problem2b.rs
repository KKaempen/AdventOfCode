use std::fs;
use std::cmp;

fn main() {
    let data = fs::read_to_string("problem2.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n');
    let mut sum = 0;
    for el in data {
        let games = el.trim().split(": ").collect::<Vec<_>>()[1];
        let mut r_max = 0;
        let mut g_max = 0;
        let mut b_max = 0;
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
                                r_max = cmp::max(r_max, num);
                            },
                            "green" => {
                                g_max = cmp::max(g_max, num);
                            },
                            "blue" => {
                                b_max = cmp::max(b_max, num);
                            },
                            _ => {}
                        }
                    },
                    _ => {}
                }
            }
        }
        sum += r_max * g_max * b_max;
    }
    println!("{sum}");
}
