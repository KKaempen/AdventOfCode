use std::fs;

fn main() {
    let data = fs::read_to_string("problem3.txt")
        .expect("Failed to read file");
    let data = data.trim()
        .split('\n')
        .collect::<Vec<_>>();
    let mut sum: u64 = 0;
    for (i, line) in data.iter().enumerate() {
        let mut find_idx = 0;
        loop {
            match line[find_idx..].find('*') {
                Some(tmp) => {
                    let line = line.chars().collect::<Vec<_>>();
                    let mut num1 = 0;
                    let mut num2 = 0;
                    let j = find_idx + tmp;
                    find_idx = j + 1;
                    if i > 0 {
                        let prev_line = data[i - 1].chars().collect::<Vec<_>>();
                        let mut prevval1 = 0;
                        let mut prevval2 = 0;
                        if j > 0 && j < prev_line.len() - 1 {
                            if !prev_line[j].is_numeric()
                                && prev_line[j - 1].is_numeric()
                                && prev_line[j + 1].is_numeric() {
                                let mut idx1 = j - 1;
                                let mut idx2 = j + 1;
                                while idx1 > 0 && prev_line[idx1 - 1].is_numeric() {
                                    idx1 -= 1;
                                }

                                while idx1 < prev_line.len() && prev_line[idx1].is_numeric() {
                                    prevval1 = prevval1 * 10 + (prev_line[idx1] as u32 - '0' as u32);
                                    idx1 += 1;
                                }
                                while idx2 < prev_line.len() && prev_line[idx2].is_numeric() {
                                    prevval2 = prevval2 * 10 + (prev_line[idx2] as u32 - '0' as u32);
                                    idx2 += 1;
                                }
                            }
                        }
                        if prevval1 == 0 {
                            let mut idx = if j > 0 && prev_line[j - 1].is_numeric() {
                                j - 1
                            } else if prev_line[j].is_numeric() {
                                j
                            } else if j < prev_line.len() - 1 && prev_line[j + 1].is_numeric() {
                                j + 1
                            } else {
                                prev_line.len()
                            };
                            if idx != prev_line.len() {
                                while idx > 0 && prev_line[idx - 1].is_numeric() {
                                    idx -= 1;
                                }

                                while idx < prev_line.len() && prev_line[idx].is_numeric() {
                                    prevval1 = prevval1 * 10 + (prev_line[idx] as u32 - '0' as u32);
                                    idx += 1;
                                }
                            }
                        }
                        num1 = prevval1;
                        num2 = prevval2;
                    }
                    if i < data.len() {
                        let next_line = data[i + 1].chars().collect::<Vec<_>>();
                        let mut nextval1 = 0;
                        let mut nextval2 = 0;
                        if j > 0 && j < next_line.len() - 1 {
                            if !next_line[j].is_numeric()
                                && next_line[j - 1].is_numeric()
                                && next_line[j + 1].is_numeric() {
                                let mut idx1 = j - 1;
                                let mut idx2 = j + 1;
                                while idx1 > 0 && next_line[idx1 - 1].is_numeric() {
                                    idx1 -= 1;
                                }

                                while idx1 < next_line.len() && next_line[idx1].is_numeric() {
                                    nextval1 = nextval1 * 10 + (next_line[idx1] as u32 - '0' as u32);
                                    idx1 += 1;
                                }
                                while idx2 < next_line.len() && next_line[idx2].is_numeric() {
                                    nextval2 = nextval2 * 10 + (next_line[idx2] as u32 - '0' as u32);
                                    idx2 += 1;
                                }
                            }
                        }
                        if nextval1 == 0 {
                            let mut idx = if j > 0 && next_line[j - 1].is_numeric() {
                                j - 1
                            } else if next_line[j].is_numeric() {
                                j
                            } else if j < next_line.len() - 1 && next_line[j + 1].is_numeric() {
                                j + 1
                            } else {
                                next_line.len()
                            };
                            if idx != next_line.len() {
                                while idx > 0 && next_line[idx - 1].is_numeric() {
                                    idx -= 1;
                                }

                                while idx < next_line.len() && next_line[idx].is_numeric() {
                                    nextval1 = nextval1 * 10 + (next_line[idx] as u32 - '0' as u32);
                                    idx += 1;
                                }
                            }
                        }
                        if num2 != 0 {
                            if nextval1 != 0 {
                                continue;
                            }
                        } else if num1 != 0 {
                            if nextval2 != 0 {
                                continue;
                            } else {
                                num2 = nextval1;
                            }
                        } else {
                            num1 = nextval1;
                            num2 = nextval2;
                        }
                    }
                    if j > 0 && line[j - 1].is_numeric() {
                        let mut idx = j - 1;
                        while idx > 0 && line[idx - 1].is_numeric() {
                            idx -= 1;
                        }

                        let mut val = 0;
                        while idx < line.len() && line[idx].is_numeric() {
                            val = val * 10 + (line[idx] as u32 - '0' as u32);
                            idx += 1;
                        }

                        if num1 == 0 {
                            num1 = val;
                        } else if num2 == 0 {
                            num2 = val;
                        } else {
                            continue;
                        }
                    }
                    if j < line.len() - 1 && line[j + 1].is_numeric() {
                        let mut idx = j + 1;
                        let mut val = 0;
                        while idx < line.len() && line[idx].is_numeric() {
                            val = val * 10 + (line[idx] as u32 - '0' as u32);
                            idx += 1;
                        }

                        if num1 == 0 {
                            num1 = val;
                        } else if num2 == 0 {
                            num2 = val;
                        } else {
                            continue;
                        }
                    }
                    sum += (num1 * num2) as u64;
                },
                None => {
                    break;
                }
            }
        }
    }
    println!("{sum}");
}
