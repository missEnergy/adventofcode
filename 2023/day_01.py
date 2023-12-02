from aocd import get_data, submit

year = 2023
day = 1

data = get_data(year=year, day=day)

lines = data.split("\n")
answer = 0
for line in lines:
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    value = int(f'{digits[0]}{digits[-1]}')
    answer = answer + value

print(answer)

# submit(answer, part="a", day=day, year=year)


def return_digit(line_part):
    # print(line_part)
    if 'one' in line_part:
        return 1
    elif 'two' in line_part:
        return 2
    elif 'three' in line_part:
        return 3
    elif 'four' in line_part:
        return 4
    elif 'five' in line_part:
        return 5
    elif 'six' in line_part:
        return 6
    elif 'seven' in line_part:
        return 7
    elif 'eight' in line_part:
        return 8
    elif 'nine' in line_part:
        return 9
    elif '1' in line_part:
        return 1
    elif '2' in line_part:
        return 2
    elif '3' in line_part:
        return 3
    elif '4' in line_part:
        return 4
    elif '5' in line_part:
        return 5
    elif '6' in line_part:
        return 6
    elif '7' in line_part:
        return 7
    elif '8' in line_part:
        return 8
    elif '9' in line_part:
        return 9
    else:
        return 0


answer = 0
for line in lines:
    print(line)
    left_digit = 0
    right_digit = 0
    for i in range(len(line)):
        left_digit = return_digit(line[:i+1])
        if left_digit > 0:
            break
    for i in range(len(line)):
        right_digit = return_digit(line[-1-i:])
        if right_digit > 0:
            break

    value = int(f'{left_digit}{right_digit}')
    print(value)
    answer = answer + value

print(answer)

# submit(answer, part="b", day=day, year=year)

