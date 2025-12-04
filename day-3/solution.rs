use std::fs;

fn find_max_joltage(bank: &str) -> i32 {
    let mut max_joltage = 0;
    let chars: Vec<char> = bank.chars().collect();
    
    // Try all pairs of positions (i, j) where i < j
    for i in 0..chars.len() {
        for j in (i + 1)..chars.len() {
            // Form the two-digit number using batteries at positions i and j
            let joltage_str = format!("{}{}", chars[i], chars[j]);
            if let Ok(joltage) = joltage_str.parse::<i32>() {
                max_joltage = max_joltage.max(joltage);
            }
        }
    }
    
    max_joltage
}

fn solve_escalator(input_string: &str) -> i64 {
    let banks: Vec<&str> = input_string.trim().split('\n').collect();
    let mut total_joltage: i64 = 0;
    
    for bank in banks {
        let bank = bank.trim();
        if !bank.is_empty() {
            let max_joltage = find_max_joltage(bank);
            total_joltage += max_joltage as i64;
            println!("Bank {}: max joltage = {}", bank, max_joltage);
        }
    }
    
    total_joltage
}

fn main() {
    let puzzle_input = fs::read_to_string("solution.csv")
        .expect("Failed to read solution.csv");
    
    let answer = solve_escalator(&puzzle_input);
    println!("\nThe total output joltage is: {}", answer);
}