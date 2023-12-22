use std::fs;

fn main() {
    let data = fs::read_to_string("problem9.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .map(|line| line
            .split(' ')
            .map(|x| x
                .parse::<i32>()
                .expect("Error: Could not parse {x}")
            )
            .collect::<Vec<_>>()
        );
    let mut sum = 0;
    for line in data {
        let mut diff_lists = Vec::<Vec<i32>>::new();
        let mut first_diff = Vec::<i32>::new();
        for v in line {
            first_diff.push(v);
        }
        diff_lists.push(first_diff);
        loop {
            let mut next_diff = Vec::<i32>::new();
            let mut all_zeros = true;
            let last_vec = diff_lists
                .last()
                .expect("Error: previous diff_list was empty after creation");
            for (prev, next) in last_vec.iter().zip(last_vec.iter().skip(1)) {
                let diff_val = next - prev;
                if diff_val != 0 {
                    all_zeros = false;
                }
                next_diff.push(diff_val);
            }
            diff_lists.push(next_diff);
            if all_zeros {
                let mut val = 0;
                for diff_list in diff_lists.iter().rev() {
                    val = diff_list[0] - val;
                }
                sum += val;
                break;
            }
        }
    }
    println!("{sum}");
}
