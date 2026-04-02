
def day_06():
    input_list: list[list[str]] = []
    operators: list[str] = []

    with open("./day06.txt") as f:
        lines = f.readlines()
        for line in lines[:-1]:
            input_list.append([num for num in line.split()])
        
        operators = lines[-1].split()


    total = 0
    for col in range(len(input_list[0])):
        problem_result = 0
        operator = operators[col]
        
        for row in range(len(input_list)):
            num = int(input_list[row][col])
            if operator == "*":
                if row == 0:
                    problem_result = num
                else:
                    problem_result *= num
            if operator == "+":
                problem_result += num
        
        total += problem_result


    print(total)


def day_06_part2():
    with open("./day06.txt") as f:
        lines = [line.rstrip("\n") for line in f]

    total = 0
    num_group: list[int] = []
    operator = ""

    for col in range(len(lines[0])):
        num = ""

        for row in range(len(lines)):
            char = lines[row][col]
            if char == " ":
                continue
            if char in "+*":
                operator = char
                continue
            num += char

        if num:
            num_group.append(int(num))
        else:
            if num_group:
                if operator == "+":
                    total += sum(num_group)
                else:
                    group_total = 1
                    for n in num_group:
                        group_total *= n
                    total += group_total
                num_group = []

    # flush final group
    if num_group:
        if operator == "+":
            total += sum(num_group)
        else:
            group_total = 1
            for n in num_group:
                group_total *= n
            total += group_total

    print(total)

        
day_06()
day_06_part2()
