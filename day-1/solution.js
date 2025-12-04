const fs = require('fs');

function solveDial(rotations) {
    let position = 50;
    let zeroCount = 0;
    
    for (const rotation of rotations) {
        const direction = rotation[0];
        const distance = parseInt(rotation.slice(1));
        
        if (direction === 'L') {
            position = (position - distance + 100) % 100;
        } else { // direction === 'R'
            position = (position + distance) % 100;
        }
        
        if (position === 0) {
            zeroCount++;
        }
    }
    
    return zeroCount;
}

// Read puzzle input
const puzzleInput = fs.readFileSync('solution.csv', 'utf8');
const rotations = puzzleInput.trim().split('\n').map(line => line.trim());

const password = solveDial(rotations);
console.log(`The password is: ${password}`);