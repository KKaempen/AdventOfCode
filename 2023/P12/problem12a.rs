use std::fs;

fn main() {
    let data = fs::read_to_string("problem12.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .map(|line| {
            let mut chars = Vec::<char>::new();
            let split_line = line
                .split(' ')
                .collect::<Vec<_>>();
            for c in split_line[0].chars() {
                chars.push(c);
            }
            let blocks = split_line[1]
                .split(',')
                .map(|x| x
                    .parse::<usize>()
                    .expect("Could not parse value to integer")
                )
                .collect::<Vec<_>>();
            (chars, blocks)
        })
        .collect::<Vec<_>>();
    let mut total_sum = 0;
    for (chars, blocks) in &data[..30] {
        let mut poss_perms = 0;
        let mut perms = Vec::<Vec<usize>>::new();
        let mut stack = Vec::<(usize, usize, Vec<usize>)>::new();
        stack.push((0, 0, Vec::<usize>::new()));
        'main_loop: while let Some((
            char_idx,
            block_idx,
            storage_vec
        )) = stack.pop() {
            if block_idx >= blocks.len() {
                if char_idx >= chars.len() {
                    poss_perms += 1;
                    perms.push(storage_vec);
                } else if chars[char_idx] != '#' {
                    stack.push((
                        char_idx + 1,
                        block_idx,
                        storage_vec
                    ));
                }
                continue;                        
            }
            if char_idx >= chars.len() {
                continue;
            }

            let block_sum: usize = blocks[block_idx..].iter().sum::<usize>() + blocks.len() - block_idx - 1;
            if block_sum > chars.len() - char_idx {
                continue;
            }
            let mut new_vec = storage_vec.clone();
            if chars[char_idx] == '.' || chars[char_idx] == '?' {
                stack.push((
                    char_idx + 1,
                    block_idx,
                    storage_vec
                ));
            }
            if chars[char_idx] == '#' || chars[char_idx] == '?' {
                let curr_block_size = blocks[block_idx];
                for i in 0..curr_block_size {
                    if chars[char_idx + i] == '.' {
                        continue 'main_loop;
                    }
                }

                if block_idx == blocks.len() - 1 {
                    new_vec.push(char_idx);
                    stack.push((
                        char_idx + curr_block_size,
                        block_idx + 1,
                        new_vec
                    ));
                } else if chars[char_idx + curr_block_size] != '#' {
                    new_vec.push(char_idx);
                    stack.push((
                        char_idx + curr_block_size + 1,
                        block_idx + 1,
                        new_vec
                    ));
                }
            }
        }
        println!("chars {:?} and blocks {:?} have {poss_perms} possible perms", chars, blocks);
        println!("possible perms are {:?}", perms);
        total_sum += poss_perms;
    }
    println!("{total_sum}");
}
