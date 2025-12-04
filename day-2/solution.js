const fs = require('fs');

function isInvalidId(num) {
    const s = num.toString();
    const length = s.length;
    
    // Must have even length to be repeated twice
    if (length % 2 !== 0) {
        return false;
    }
    
    // Split in half and check if both halves are identical
    const mid = Math.floor(length / 2);
    const firstHalf = s.slice(0, mid);
    const secondHalf = s.slice(mid);
    
    return firstHalf === secondHalf;
}

function solveGiftShop(inputString) {
    const ranges = inputString.trim().split(',');
    let totalSum = 0n; // Use BigInt
    
    for (const rangeStr of ranges) {
        const trimmedRange = rangeStr.trim();
        if (!trimmedRange) continue;
        
        // Parse the range
        const parts = trimmedRange.split('-');
        if (parts.length !== 2) continue;
        
        const start = parseInt(parts[0]);
        const end = parseInt(parts[1]);
        
        // Check each ID in the range
        for (let num = start; num <= end; num++) {
            if (isInvalidId(num)) {
                totalSum += BigInt(num);
            }
        }
    }
    
    return totalSum;
}

// Read puzzle input
const puzzleInput = fs.readFileSync('solution.csv', 'utf8');
const answer = solveGiftShop(puzzleInput);
console.log(`The sum of all invalid IDs is: ${answer}`);