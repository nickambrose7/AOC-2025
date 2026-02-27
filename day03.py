"""

We want to find the largest 10's place number, since that will 
have the most impact on the size of the number. 
- Once we've found the index of the largest number, we want to find the largest 
number to the right of that index. 


Initial Thought: 
- Explore all numbers except the last number (since that one won't ever be a candidate since it can't have another digit)
    - Do this in reverse order so that when we are looking for the one's place number, 
    we will have the most options for digits to pick from. 
    - Once we've found the number and its index, search for the largest number in that range. 

"""


"""
Part 2:
- We still care most about getting the largest number to the left. 
    - And we want to do this recursively, where once we've found that largest number to the
    left, we want to look in that range, and find the next largest number to the left. 
    - We also still want to never look at numbers that won't leave us enough digits. 

"""
def day_03(num_digits_allowed: int):
    with open("./day03.txt") as f:
        banks = f.read().splitlines()

    total = 0
    for bank in banks: 
        start_range = -1 
        number_str = "" 
        
        for num_digits_to_exclude in range(num_digits_allowed, 0, -1):
            end_range = len(bank) - num_digits_to_exclude
            largest_num, start_range = find_first_largest(bank, start_range, end_range)
            number_str += str(largest_num)
        
        total += int(number_str)
    
    print(total)


def find_first_largest(s: str, start_range: int, end_range: int):
    """This function finds the first occurance of the largest number 
    between `start_range` and `end_range` in the string of digits.  
    It returns the number itself and the index of that number.
    """
    largest_num, largest_num_index = 0, 0
    for i in range(end_range, start_range, -1):
        num = int(s[i])
        if num >= largest_num:
            largest_num = num
            largest_num_index = i

    return largest_num, largest_num_index

day_03(2)
day_03(12)