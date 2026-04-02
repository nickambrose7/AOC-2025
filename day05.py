"""
Naive approach: add all numbers in the ranges to a set and check ids against that set. 

   3--5
          10----14
              12-------18
                   16----20

Another solution would be to keep track of all the ranges and just test if each number is within
the range directly. But this would take much more time since you'd have to iterate through all the ranges
for each id that you want to test. 

(5, 10)
(5,11)
(6,10)
(6,12) id = 15
(7,14)
(8, 27)
How do we know when we've looked at all the candidate ranges for a id? 


---
Part 2: 
- This is essentially asking how many numbers do the ranges encompass? 
- Again this could be done with a set but we can use less memory by mergine the ranges then subtracting
"""

def day_05():
    with open("./day05.txt") as f:
        ranges: list[tuple[int, int]] = []
        ids: list[int] = []
        lines = f.readlines()
        i = 0
        while lines[i] != "\n":
            line = lines[i].strip()
            start, stop = line.split("-")
            ranges.append((int(start), int(stop)))
            i += 1
        i += 1
        while i < len(lines):
            ids.append(int(lines[i].strip()))
            i += 1

    ranges.sort()
    ids.sort()
    range_pointer = 0

    fresh = 0
    for id in ids:
        start, end = ranges[range_pointer]

        while True:
            if id >= start and id <= end:
                fresh += 1
                break
            elif end < id and range_pointer < len(ranges) - 1:
                range_pointer += 1 
                start, end = ranges[range_pointer]
                continue
            else: 
                break

    print(fresh)

    merged_ranges: list[tuple[int, int]] = [] #[(3,5))]
    start, end = ranges[0] # 10, 20
    for r in ranges[1:]:
        cur_start, cur_end = r # 16, 20
        
        # if they overlap, set end = cur end. 
        if end >= cur_start:
            end = cur_end if cur_end > end else end
            continue

        # if they don't overlap, add start and end to merged_ranges and update start and end
        else:
            merged_ranges.append((start, end))
            start = cur_start
            end = cur_end
            continue
    
    merged_ranges.append((start, end))

    part_2_fresh = 0
    for r in merged_ranges:
        start, end = r
        part_2_fresh += (end - start) + 1
    
    print(part_2_fresh)



day_05()            