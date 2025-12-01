use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

/// Counts num of times dial points at 0 during rotation
fn count_zeros_during_rotation(start: i32, direction: char, distance: i32) -> i32 {
    let mut zero_count = 0;

    match direction {
        'L' => {
            for i in 1..=distance {
                let position = (start - i).rem_euclid(100);
                if position == 0 {
                    zero_count += 1;
                }
            }
        }
        'R' => {
            for i in 1..=distance {
                let position = (start + i).rem_euclid(100);
                if position == 0 {
                    zero_count += 1;
                }
            }
        }
        _ => panic!("Invalid direction"),
    }

    zero_count
}

/// Solves puzzle
fn solve_dial_puzzle_part2(rotations: Vec<String>) -> i32 {
    let mut position: i32 = 50;
    let mut total_zero_count: i32 = 0;

    for rotation in rotations {
        let direction = rotation.chars().next().unwrap();
        let distance: i32 = rotation[1..].parse().unwrap();

        // Counts zeros during rotation
        let zeros_during = count_zeros_during_rotation(position, direction, distance);
        total_zero_count += zeros_during;

        // Updates position
        position = match direction {
            'L' => (position - distance).rem_euclid(100),
            'R' => (position + distance).rem_euclid(100),
            _ => panic!("Invalid direction"),
        };
    }

    total_zero_count
}

/// Reads file lines into Vec<String>
fn read_lines<P>(filename: P) -> io::Result<Vec<String>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let buf = io::BufReader::new(file);
    Ok(buf.lines().filter_map(Result::ok).collect())
}

fn main() {
    let rotations = read_lines("solution.csv").expect("Failed to read solution.csv");

    let password = solve_dial_puzzle_part2(rotations);
    println!("The password is: {}", password);
}
