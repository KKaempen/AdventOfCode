use std::fs;

fn main() {
    let data = fs::read_to_string("problem15.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let data = data[0]
        .split(',');
    let mut boxes = Vec::<Vec<(String, usize)>>::new();
    for _ in 0..256 {
        let curr_box = Vec::<(String, usize)>::new();
        boxes.push(curr_box);
    }
    for s in data {
        let inst = s.split('=').collect::<Vec<_>>();
        let (label, focal_length) = if inst.len() == 2 {
            (inst[0].to_string(), Some(inst[1].parse::<usize>().expect("Could not parse integer")))
        } else {
            let inst = inst[0].split('-').collect::<Vec<_>>();
            (inst[0].to_string(), None)
        };
        let mut hash = 0;
        for c in label.chars() {
            hash = ((hash + (c as usize)) * 17) % 256;
        }
        match focal_length {
            Some(foc_len) => 'match_block: {
                let curr_box = &mut boxes[hash];
                for (i, (l, _)) in curr_box.iter().enumerate() {
                    if *l == label {
                        curr_box[i] = (label, foc_len);
                        break 'match_block;
                    }
                }
                curr_box.push((label, foc_len));
            },
            None => {
                let curr_box = &mut boxes[hash];
                let mut match_idx = None;
                for (i, (l, _)) in curr_box.iter().enumerate() {
                    if *l == label {
                        match_idx = Some(i);
                        break;
                    }
                }
                match match_idx {
                    Some(idx) => {
                        for i in idx..curr_box.len() - 1 {
                            curr_box[i] = curr_box[i + 1].clone();
                        }
                        curr_box.pop();
                    },
                    None => { }
                }
            }
        }
    }
    let mut sum: u64 = 0;
    for (i, curr_box) in boxes.iter().enumerate() {
        for (j, (_, f_p)) in curr_box.iter().enumerate() {
            sum += ((i + 1) * (j + 1) * f_p) as u64;
        }
    }
    println!("{sum}");
}
