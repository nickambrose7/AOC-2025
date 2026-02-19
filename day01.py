import math


def day_01():
    data = []
    with open("./day01.txt") as f:
        for line in f:
            if line[0] == "L":
                data.append(-1 * int(line[1:]))
            else:
                data.append(int(line[1:]))

    num_zeros_landed = 0
    num_zeros_clicked = 0
    pos = 50 

    for num in data:
        new_pos = pos + num

        num_zeros_clicked += abs(math.trunc(new_pos / 100))

        if pos != 0 and new_pos <= 0:
            num_zeros_clicked += 1
        
        pos = new_pos % 100

        if pos == 0:
            num_zeros_landed += 1

    print(num_zeros_landed)
    print(num_zeros_clicked)

day_01()