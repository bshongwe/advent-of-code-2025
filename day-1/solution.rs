use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn solve_dial_puzzle(rotations: Vec<String>) -> i32 {
    let mut position: i32 = 50;
    let mut zero_count: i32 = 0;

    for rotation in rotations {
        let direction = rotation.chars().next().unwrap();
        let distance: i32 = rotation[1..].parse().unwrap();

        position = match direction {
            'L' => (position - distance).rem_euclid(100),
            'R' => (position + distance).rem_euclid(100),
            _ => panic!("Invalid direction"),
        };

        if position == 0 {
            zero_count += 1;
        }
    }

    zero_count
}

fn read_lines<P>(filename: P) -> io::Result<Vec<String>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let buf = io::BufReader::new(file);
    Ok(buf.lines().filter_map(Result::ok).collect())
}

fn main() {
    let rotations = read_lines("solution.csv").expect("Failed to read file");

    let password = solve_dial_puzzle(rotations);
    println!("The password is: {}", password);
}
