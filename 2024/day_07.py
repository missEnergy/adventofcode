from aocd import get_data, submit

year = 2024
day = 7

data = get_data(year=year, day=day)
lines = data.splitlines()


def is_valid_eq_partA(remain, numbers):
    if len(numbers) == 1:
        return remain == numbers[0]
    elif remain % numbers[0] == 0:
        return is_valid_eq_partA(remain // numbers[0], numbers[1:]) or is_valid_eq_partA(remain - numbers[0], numbers[1:])
    else:
        return is_valid_eq_partA(remain - numbers[0], numbers[1:])


def is_valid_eq_partB(remain, numbers):
    if len(numbers) == 1:
        return remain == numbers[0]

    if len(numbers) == 2:
        if str(remain).endswith(str(numbers[0])):
            if str(remain)[0:len(str(remain)) - len(str(numbers[0]))] == str(numbers[1]):
                return True
        if remain % numbers[0] == 0:
            return (is_valid_eq_partB(remain // numbers[0], numbers[1:])
                    or is_valid_eq_partB(remain - numbers[0], numbers[1:]))
        return is_valid_eq_partB(remain - numbers[0], numbers[1:])

    # more than 2 numbers left
    if remain % numbers[0] == 0 and str(remain).endswith(str(numbers[0])):
        return (is_valid_eq_partB(remain // numbers[0], numbers[1:])
                or is_valid_eq_partB(remain - numbers[0], numbers[1:])
                or is_valid_eq_partB(int(str(remain)[0:len(str(remain)) - len(str(numbers[0]))]), numbers[1:]))
    if remain % numbers[0] == 0:
        return (is_valid_eq_partB(remain // numbers[0], numbers[1:])
                or is_valid_eq_partB(remain - numbers[0], numbers[1:]))
    if str(remain).endswith(str(numbers[0])):
        return (is_valid_eq_partB(remain - numbers[0], numbers[1:])
                or is_valid_eq_partB(int(str(remain)[0:len(str(remain)) - len(str(numbers[0]))]), numbers[1:]))
    return is_valid_eq_partB(remain - numbers[0], numbers[1:])


answer = 0
for line in lines:
    test_value, numbers = line.split(": ")
    test_value = int(test_value)
    numbers = list(map(int, numbers.split(" ")))[::-1]

    print(test_value, numbers)
    # if is_valid_eq_partA(test_value, numbers):
    if is_valid_eq_partB(test_value, numbers):
        print('valid!')
        answer += test_value
print(answer)

# submit(answer, part="a", day=day, year=year)
# submit(answer, part="b", day=day, year=year)
