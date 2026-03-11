
"""
Part 1: 
Go through each cell, if it's an @, check all it's neighbors to see if more than 4 are @'s (in a helper function).

What would be the most useful format for the data? 
- Probably a 2d array 
"""

"""
Part 2:
- The only real modifcation I see is that:
    1. We need to modify the grid to remove a '@' if the check neighbors function returns a 1
    2. We need to modify the original loop to continue looping until we don't remove any more '@' symbols.
    3. separate part 1 and part 2 counters. 
"""

def check_neighbors(grid: list[list[str]], row: int, col: int):
    """Check the 8 neighbors of the current position for '@' symbols. If three or fewer
    neighbors are '@', return 1, else return 0.
    -1, -1
    -1, 0
    -1, 1
    0, 
    """
    total = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0: 
                continue
            
            # check in bounds
            y = row + dy
            x = col + dx

            if y < 0 or y >= len(grid):
                continue
            if x < 0 or x >= len(grid[row]):
                continue
            
            if grid[y][x] == "@":
                total += 1
    
    return 1 if total <= 3 else 0



def day_04_part_1():
    with open("./day04.txt") as f:
        grid = [list(line.strip()) for line in f]

    total = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                total += check_neighbors(grid, row, col)
    
    print(total)


def day_04_part_2():
    with open("./day04.txt") as f:
        grid = [list(line.strip()) for line in f]

    total_part_2 = 0

    removed = True
    iteration_number = 0

    while removed:
        removed = False
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    can_remove = check_neighbors(grid, row, col)
                    
                    if can_remove:
                        removed = True
                        grid[row][col] = "."
                    
                    total_part_2 += can_remove
        
        iteration_number += 1

    print(total_part_2)

day_04_part_1()
day_04_part_2()

