use std::fs;
use std::cmp::min;
use std::collections::HashMap;

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
            let mut blocks = split_line[1]
                .split(',')
                .map(|x| x
                    .parse::<usize>()
                    .expect("Could not parse value to integer")
                )
                .collect::<Vec<usize>>();

            let char_length = chars.len();
            let block_length = blocks.len();
            for _ in 0..4 {
                chars.push('?');
                for j in 0..char_length {
                    chars.push(chars[j]);
                }
                for j in 0..block_length {
                    blocks.push(blocks[j]);
                }
            }
            let char_blocks = chars
                .split(|x| *x == '.')
                .filter(|vec| vec.len() != 0)
                .map(|x| Vec::<char>::from(x))
                .collect::<Vec<Vec<char>>>();
            (char_blocks, blocks)
        })
        .collect::<Vec<_>>();
    let mut total_sum: u64 = 0;
    for (char_blocks, blocks) in data.iter() {
        // Each partition will, at index i, store the upper limit (not inclusive)
        // of the blocks that will be included in the char block at index i.
        let mut partitions = Vec::<Vec<usize>>::new();
        // Each state needs to include a partially constructed partition vector
        // Would help to also have a sum of remaining available character block sizes
        let mut part_stack = Vec::<(Vec<usize>, usize)>::new();
        let mut char_block_sum = 0;
        for char_block in char_blocks {
            char_block_sum += char_block.len();
        }
        part_stack.push((Vec::<usize>::new(), char_block_sum));
        while let Some((
            partition,
            rem_size
        )) = part_stack.pop() {
            let block_idx = match partition.last() {
                Some(idx) => { *idx },
                None => { 0 }
            };
            if block_idx >= blocks.len() {
                let mut vec_cpy = partition.clone();
                while vec_cpy.len() < char_blocks.len() {
                    vec_cpy.push(block_idx);
                }
                partitions.push(vec_cpy);
                continue;
            }
            let char_block_idx = partition.len();
            let new_rem_size = rem_size - char_blocks[char_block_idx].len();
            // Find out how much space the rest of the block elements would require
            // if they were put in the char blocks after the current one.
            let needed_space = blocks[block_idx..].iter().sum::<usize>()
                + (blocks.len() - block_idx - 1)
                - min(char_blocks.len() - char_block_idx - 1, blocks.len() - block_idx - 1);
            let mut next_block_idx = block_idx;
            let mut curr_used_space = 0;
            while curr_used_space < needed_space && needed_space - curr_used_space > new_rem_size {
                curr_used_space += blocks[next_block_idx] + 1;
                next_block_idx += 1;
            }
            for c in &char_blocks[char_block_idx] {
                if *c == '#' && curr_used_space == 0 {
                    curr_used_space += blocks[next_block_idx] + 1;
                    next_block_idx += 1;
                }
            }
            while curr_used_space == 0 || curr_used_space - 1 <= char_blocks[char_block_idx].len() {
                let mut vec_cpy = partition.clone();
                vec_cpy.push(next_block_idx);
                part_stack.push((vec_cpy, new_rem_size));
                if next_block_idx >= blocks.len() {
                    break;
                }
                curr_used_space += blocks[next_block_idx] + 1;
                next_block_idx += 1;
            }
        }

        for partition in partitions {
            let mut poss_perms: u64 = 1;
            let mut lo_idx = 0;
            let mut map = HashMap::<(String, (usize, usize)), u64>::new();
            for (hi_idx, char_block) in partition.iter().zip(char_blocks.iter()) {
                let mut curr_perms: u64 = 0;
                let mut stack = Vec::<(usize, usize)>::new();
                stack.push((0, lo_idx));
                while let Some((
                    char_idx,
                    block_idx
                )) = stack.pop() {
                    if block_idx >= *hi_idx {
                        if char_idx >= char_block.len() {
                            curr_perms += 1;
                        } else if char_block[char_idx] != '#' {
                            stack.push((
                                char_idx + 1,
                                block_idx
                            ));
                        }
                        continue;                        
                    }
                    if char_idx >= char_block.len() {
                        continue;
                    }

                    let block_sum: usize = blocks[block_idx..*hi_idx].iter().sum::<usize>() + *hi_idx - block_idx - 1;
                    if block_sum > char_block.len() - char_idx {
                        continue;
                    }
                    if char_block[char_idx] == '?' {
                        stack.push((
                            char_idx + 1,
                            block_idx
                        ));
                    }
                    if char_block[char_idx] == '#' || char_block[char_idx] == '?' {
                        let curr_block_size = blocks[block_idx];

                        if block_idx == hi_idx - 1 {
                            stack.push((
                                char_idx + curr_block_size,
                                block_idx + 1
                            ));
                        } else if char_block[char_idx + curr_block_size] != '#' {
                            stack.push((
                                char_idx + curr_block_size + 1,
                                block_idx + 1
                            ));
                        }
                    }
                }
                if curr_perms == 0 {
                    poss_perms = 0;
                    break;
                }
                lo_idx = *hi_idx;
                poss_perms *= curr_perms;
            }
            total_sum += poss_perms;
        }
    }
    println!("{total_sum}");
}
