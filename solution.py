def solve_dial_puzzle(rotations):
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:  # direction == 'R'
            position = (position + distance) % 100
        
        if position == 0:
            zero_count += 1
    
    return zero_count

# Read your puzzle input
with open('solution.csv', 'r') as f:
    rotations = [line.strip() for line in f.readlines()]

password = solve_dial_puzzle(rotations)
print(f"The password is: {password}")