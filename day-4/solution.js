const fs = require('fs');

function countAccessibleRolls(grid) {
    const rows = grid.length;
    if (rows === 0) return 0;
    
    const cols = grid[0].length;
    let accessibleCount = 0;
    
    // Directions for 8 adjacent positions (including diagonals)
    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];
    
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            // Check if current position has a roll of paper
            if (grid[i][j] === '@') {
                // Count adjacent rolls
                let adjacentRolls = 0;
                
                for (const [di, dj] of directions) {
                    const ni = i + di;
                    const nj = j + dj;
                    
                    // Check if position is within bounds
                    if (ni >= 0 && ni < rows && nj >= 0 && nj < cols) {
                        if (grid[ni][nj] === '@') {
                            adjacentRolls++;
                        }
                    }
                }
                
                // A roll is accessible if it has fewer than 4 adjacent rolls
                if (adjacentRolls < 4) {
                    accessibleCount++;
                }
            }
        }
    }
    
    return accessibleCount;
}

// Read puzzle input
const puzzleInput = fs.readFileSync('solution.csv', 'utf8');
const grid = puzzleInput.trim().split('\n').map(line => line.trim()).filter(line => line.length > 0);

const result = countAccessibleRolls(grid);
console.log(`Number of accessible rolls: ${result}`);