use std::fs;

fn main() {
    let data = fs::read_to_string("problem6.txt")
        .expect("Failed to read file");
    let data = data
        .trim()
        .split('\n')
        .collect::<Vec<_>>();
    let times = data[0]
        .split(": ")
        .collect::<Vec<_>>()[1]
        .split(" ")
        .filter(|&x| x != "")
        .map(|x| x
            .parse::<i64>()
            .expect("Failed to parse")
        )
        .collect::<Vec<_>>();
    let distances = data[1]
        .split(": ")
        .collect::<Vec<_>>()[1]
        .split(" ")
        .filter(|&x| x != "")
        .map(|x| x
            .parse::<i64>()
            .expect("Failed to parse")
        )
        .collect::<Vec<_>>();
    let mut big_t: i64 = 0;
    let mut big_d: i64 = 0;
    for t in times {
        let mut mult: i64 = 1;
        while mult < t {
            mult *= 10;
        }
        big_t *= mult;
        big_t += t;
    }
    for d in distances {
        let mut mult: i64 = 1;
        while mult < d {
            mult *= 10;
        }
        big_d *= mult;
        big_d += d;
    }
    let big_t: f64 = big_t as f64;
    let big_d: f64 = big_d as f64;
    let disc: f64 = (big_t * big_t - 4.0 * big_d).sqrt();
    let lo = (big_t - disc) / 2.0;
    let hi = (big_t + disc) / 2.0;
    let lo: u64 = lo.ceil() as u64;
    let hi: u64 = hi.floor() as u64;
    let prod = hi - lo + 1;
    println!("{prod}");
}
