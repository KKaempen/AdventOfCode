use std::fs;
use std::collections::HashMap;
use std::cmp::{Ordering, Ordering::{Greater, Less}};

fn main() {
    let data = fs::read_to_string("problem19.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let mut data = data.split(|x| *x == "");
    let label_map = HashMap::<char, usize>::from([
        ('x', 0),
        ('m', 1),
        ('a', 2),
        ('s', 3)
    ]);
    let workflows_vec = data
        .next()
        .expect("Error: problem with data split");
    let parts = data
        .next()
        .expect("Error: problem with data split second item");
    let mut workflows = HashMap::<String, Vec<(char, u32, Ordering, String)>>::new();
    for workflow in workflows_vec {
        let workflow = workflow
            .split('}')
            .next()
            .expect("Error: problem with workflow entry '}' split");
        let mut workflow = workflow
            .split('{');
        let label = workflow
            .next()
            .expect("Error: problem with workflow entry '{' split")
            .to_string();
        let preds = workflow
            .next()
            .expect("Error: problem with workflow entry '{' split second item");
        let mut workflow_vec = Vec::<(char, u32, Ordering, String)>::new();
        for pred in preds.split(',') {
            let pred = pred
                .split(':')
                .collect::<Vec<_>>();
            if pred.len() == 1 {
                workflow_vec.push((
                    'x',
                    0,
                    Greater,
                    pred[0].to_string()
                ));
            } else {
                let mut cmp_vec = pred[0]
                    .split('>')
                    .collect::<Vec<_>>();
                let mut cmp_val = Greater;
                if cmp_vec.len() == 1 {
                    cmp_vec = cmp_vec[0]
                        .split('<')
                        .collect::<Vec<_>>();
                    cmp_val = Less;
                }
                let check_char = cmp_vec[0].chars().last().unwrap();
                let check_val = cmp_vec[1]
                    .parse::<u32>()
                    .expect("Error: could not parse ineq value to integer"); 
                workflow_vec.push((
                    check_char,
                    check_val,
                    cmp_val,
                    pred[1].to_string()
                ));
            }
        }
        workflows.insert(label, workflow_vec);
    }
    let mut sum = 0;
    for part in parts {
        let part = part
            .split('}')
            .next()
            .expect("Error: problem with part entry '}' split");
        let part = part
            .split('{')
            .last()
            .expect("Error: problem with part entry '{' split");
        let mut vals = [0; 4]; 
        for eq in part.split(',') {
            let mut eq_vec = eq.split('=');
            let c = eq_vec
                .next()
                .expect("Error: problem with eq entry '=' split")
                .chars()
                .last()
                .unwrap();
            let v = eq_vec
                .next()
                .expect("Error: problem with eq entry '=' split second item")
                .parse::<u32>()
                .expect("Error: could not parse eq value to integer");
            let idx = label_map[&c];
            vals[idx] = v;
        }
        let mut curr_s = "in".to_string();
        loop {
            if curr_s == "A" {
                for v in vals {
                    sum += v;
                }
                break;
            } else if curr_s == "R" {
                break;
            }
            let workflow = &workflows[&curr_s];
            for (check_char, check_val, cmp_val, next) in workflow {
                let check_idx = label_map[&check_char];
                if vals[check_idx].cmp(&check_val) == *cmp_val {
                    curr_s = next.clone();
                    break;
                }
            }
        }
    }
    println!("{sum}");
}
