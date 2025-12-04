use std::fs;

fn count_accessible_rolls(grid: &[String]) -> i32 {
    let rows = grid.len();
    if rows == 0 {
        return 0;
    }
    let cols = grid[0].len();
    let mut accessible_count = 0;
    
    // Directions for 8 adjacent positions (including diagonals)
    let directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ];
    
    for i in 0..rows {
        let row_chars: Vec<char> = grid[i].chars().collect();
        for j in 0..cols {
            // Check if current position has a roll of paper
            if j < row_chars.len() && row_chars[j] == '@' {
                // Count adjacent rolls
                let mut adjacent_rolls = 0;
                
                for (di, dj) in directions.iter() {
                    let ni = i as i32 + di;
                    let nj = j as i32 + dj;
                    
                    // Check if position is within bounds
                    if ni >= 0 && ni < rows as i32 && nj >= 0 && nj < cols as i32 {
                        let ni = ni as usize;
                        let nj = nj as usize;
                        
                        if ni < grid.len() && nj < grid[ni].len() {
                            let neighbor_chars: Vec<char> = grid[ni].chars().collect();
                            if nj < neighbor_chars.len() && neighbor_chars[nj] == '@' {
                                adjacent_rolls += 1;
                            }
                        }
                    }
                }
                
                // A roll is accessible if it has fewer than 4 adjacent rolls
                if adjacent_rolls < 4 {
                    accessible_count += 1;
                }
            }
        }
    }
    
    accessible_count
}

fn main() {
    let puzzle_input = fs::read_to_string("solution.csv")
        .expect("Failed to read solution.csv");
    
    let grid: Vec<String> = puzzle_input
        .lines()
        .map(|line| line.trim().to_string())
        .filter(|line| !line.is_empty())
        .collect();
    
    let result = count_accessible_rolls(&grid);
    println!("Number of accessible rolls: {}", result);
}