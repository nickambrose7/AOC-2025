"""
Split: The beam hits a "^"

- There are never two ^ next to eachother ex.) ^^. This means we will always get a clean split, new beam on the left and new beam on the right.

Data: Need to keep track of the indicies of the beams and of the splitters for the current line. 
- I think storing these as sets makes the most sense. That way we can find the intersection easily. 

Algo: 
- Find overlap between beams and splitter sets.
- incremnt total counter based on numbers that intersect between the two sets
- remove all those numbers, and add the two numbers on either side of the number that is removed, for each number in the intersection.
- Move on to the next line.

Time:
- Have to go through each spot in the grid. 
O(n)

"""

def num_splits(grid: list[str], beams: set[int]) -> int:
    """
    grid: grid of splitters and open space.
    beams: a set representing the indicies of all the beams
    that are traveling through the grid. 
    """
    total_splits = 0

    for line in grid:
        splitters = {i for i, char in enumerate(line) if char == "^"}
        intersection = beams & splitters # 5
        total_splits += len(intersection)
        beams = beams - intersection
        
        for num in intersection:
            beams.add(num - 1)
            beams.add(num + 1)
    
    return total_splits


def num_timelines(grid: list[str], beam: int, cache: dict[tuple[int, int], int]) -> int:
    if not grid:
        return 1

    if beam < 0 or beam >= len(grid[0]):
        return 0

    current_line = grid[0]

    key = (beam, len(grid))

    if key in cache:
        return cache[key]
    
    if current_line[beam] != "^":
        cache[key] = num_timelines(grid[1:], beam, cache)
        return cache[key]

    cache[key] = num_timelines(grid[1:], beam - 1, cache) + num_timelines(grid[1:], beam + 1, cache)
    return cache[key]
    

def day_07() -> None:
    with open("./day07.txt") as f:
        first_line = f.readline().strip()
        rest = [line.strip() for line in f]

    beams = {first_line.index("S")}

    total_splits = num_splits(rest, beams.copy())
    
    print(total_splits)

    beam_index = first_line.index("S")

    print(num_timelines(rest, beam_index, {}))




day_07()
