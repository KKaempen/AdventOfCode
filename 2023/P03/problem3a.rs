use std::fs;

fn main() {
    let data = fs::read_to_string("problem3.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n')
        .collect::<Vec<_>>();
    let mut sum = 0;
    for (i, line) in data.iter().enumerate() {
        let mut val = 0;
        let mut found_symbol = false;
        for (j, c) in line.chars().enumerate() {
            if c.is_numeric() {
                if val == 0 {
                    if j > 0 {
                        if i > 0 {
                            let c = data[i - 1].chars().collect::<Vec<_>>()[j - 1];
                            if !c.is_numeric() && c != '.' {
                                found_symbol = true;
                            }
                        }
                        if i < data.len() - 1 {
                            let c = data[i + 1].chars().collect::<Vec<_>>()[j - 1];
                            if !c.is_numeric() && c != '.' {
                                found_symbol = true;
                            }
                        }
                        let c = data[i].chars().collect::<Vec<_>>()[j - 1];
                        if !c.is_numeric() && c != '.' {
                            found_symbol = true;
                        }
                    }
                }
                if i > 0 {
                    let c = data[i - 1].chars().collect::<Vec<_>>()[j];
                    if !c.is_numeric() && c != '.' {
                        found_symbol = true;
                    }
                }
                if i < data.len() - 1 {
                    let c = data[i + 1].chars().collect::<Vec<_>>()[j];
                    if !c.is_numeric() && c != '.' {
                        found_symbol = true;
                    }
                }
                val = 10 * val + (c as u32 - '0' as u32);
            } else {
                if val > 0 {
                    if i > 0 {
                        let c = data[i - 1].chars().collect::<Vec<_>>()[j];
                        if !c.is_numeric() && c != '.' {
                            found_symbol = true;
                        }
                    }
                    if i < data.len() - 1 {
                        let c = data[i + 1].chars().collect::<Vec<_>>()[j];
                        if !c.is_numeric() && c != '.' {
                            found_symbol = true;
                        }
                    }
                    if !c.is_numeric() && c != '.' {
                        found_symbol = true;
                    }
                    if found_symbol {
                        sum += val;
                    }
                    found_symbol = false;
                    val = 0;
                }
            }
        }
        if found_symbol && val != 0 {
            sum += val;
        }
    }
    println!("{sum}");
}
