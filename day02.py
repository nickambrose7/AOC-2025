
"""
We only need to check even length numbers.

Part 2:
- We need to check chunks of numbers up to size len(num_string) // 2
    - set max_chunk_size = len(num_string) // 2
        - for chunk_size in range(max_chunk_size)
            - Don't want to do the pointer comparison because we would need to initialize a arbitrary amount of pointers. 
            - Need a way of slicing strings into chunks

"""

def chunk_string(s: str, chunk_size: int) -> list[str]:
    """Slice a string into chunks of size ``chunk_size``. 
    If the sting can't be sliced evenly, return an empty list.
    ex "1010"
    """
    if len(s) % chunk_size:
        return []
    
    chunks: list[str] = []
    start = 0
    end = chunk_size
    while end <= len(s):
        chunks.append(s[start:end])
        start = end
        end += chunk_size
    
    return chunks




def day_02():
    with open("./day02.txt") as f:
        data = [
        range(int(start), int(end) + 1)
        for start, end in (range.split("-", 1) for range in f.read().strip().split(","))
    ]
    
    part_1_answer = 0
    part_2_answer = 0

    for num_range in data:
        for num in num_range:
            num_string = str(num)

            for chunk_size in range(1, (len(num_string) // 2 + 1)):
                chunks = chunk_string(num_string, chunk_size)
                if chunks:
                    all_equal = all(s == chunks[0] for s in chunks)    
                    if all_equal:
                        part_2_answer += num
                        break

            
            if len(num_string) % 2:
                continue

            l, r = 0, len(num_string) // 2

            add_num = True
            while r < len(num_string):
                if num_string[l] == num_string[r]:
                    l += 1
                    r += 1
                    continue

                add_num = False
                break

            if add_num:
                part_1_answer += num
    
    print(part_1_answer)
    print(part_2_answer)

day_02()