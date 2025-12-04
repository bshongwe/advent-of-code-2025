const fs = require('fs');

function findMaxJoltage(bank) {
    let maxJoltage = 0;
    
    // Try all pairs of positions (i, j) where i < j
    for (let i = 0; i < bank.length; i++) {
        for (let j = i + 1; j < bank.length; j++) {
            // Form the two-digit number using batteries at positions i and j
            const joltage = parseInt(bank[i] + bank[j]);
            maxJoltage = Math.max(maxJoltage, joltage);
        }
    }
    
    return maxJoltage;
}

function solveEscalator(inputString) {
    const banks = inputString.trim().split('\n');
    let totalJoltage = 0;
    
    for (const bank of banks) {
        const trimmedBank = bank.trim();
        if (trimmedBank) {
            const maxJoltage = findMaxJoltage(trimmedBank);
            totalJoltage += maxJoltage;
            console.log(`Bank ${trimmedBank}: max joltage = ${maxJoltage}`);
        }
    }
    
    return totalJoltage;
}

// Read puzzle input
const puzzleInput = fs.readFileSync('solution.csv', 'utf8');
const answer = solveEscalator(puzzleInput);
console.log(`\nThe total output joltage is: ${answer}`);