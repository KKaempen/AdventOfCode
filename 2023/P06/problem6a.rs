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
            .parse::<i32>()
            .expect("Failed to parse")
        )
        .collect::<Vec<_>>();
    let distances = data[1]
        .split(": ")
        .collect::<Vec<_>>()[1]
        .split(" ")
        .filter(|&x| x != "")
        .map(|x| x
            .parse::<i32>()
            .expect("Failed to parse")
        )
        .collect::<Vec<_>>();
    let mut prod = 1;
    for (t, d) in times.iter().zip(distances.iter()) {
        let mid: f64 = *t as f64;
        let disc: f64 = ((t * t - 4 * d) as f64).sqrt();
        let lo = (mid - disc) / 2.0;
        let hi = (mid + disc) / 2.0;
        let lo: u32 = lo.ceil() as u32;
        let hi: u32 = hi.floor() as u32;
        prod *= hi - lo + 1;
    }
    println!("{prod}");
}
