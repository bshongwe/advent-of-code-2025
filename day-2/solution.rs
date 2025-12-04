use std::fs;

fn is_invalid_id(num: i32) -> bool {
    let s = num.to_string();
    let length = s.len();
    
    // Must have even length to be repeated twice
    if length % 2 != 0 {
        return false;
    }
    
    // Split in half and check if both halves are identical
    let mid = length / 2;
    let first_half = &s[..mid];
    let second_half = &s[mid..];
    
    first_half == second_half
}

fn solve_gift_shop(input_string: &str) -> i64 {
    let ranges: Vec<&str> = input_string.trim().split(',').collect();
    let mut total_sum: i64 = 0;
    
    for range_str in ranges {
        let range_str = range_str.trim();
        if range_str.is_empty() {
            continue;
        }
        
        // Parse the range
        let parts: Vec<&str> = range_str.split('-').collect();
        if parts.len() != 2 {
            continue;
        }
        
        let start: i32 = parts[0].parse().unwrap_or(0);
        let end: i32 = parts[1].parse().unwrap_or(0);
        
        // Check each ID in the range
        for num in start..=end {
            if is_invalid_id(num) {
                total_sum += num as i64;
            }
        }
    }
    
    total_sum
}

fn main() {
    let puzzle_input = fs::read_to_string("solution.csv")
        .expect("Failed to read solution.csv");
    
    let answer = solve_gift_shop(&puzzle_input);
    println!("The sum of all invalid IDs is: {}", answer);
}