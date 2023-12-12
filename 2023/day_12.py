from aocd import get_data, submit
import re

year, day = 2023, 12

# parse data
data = get_data(year=year, day=day).split("\n")

# part A


def determine_damaged_springs(springs):
    return [len(i) for i in re.split(r'[.]', springs) if len(i) > 0]


def binary_combinations(n):
    combis= []
    for i in range(1 << n):
        # Convert the current number to a binary string of length n
        combis.append(format(i, '0' + str(n) + 'b'))
    return combis


def replace_by_binary(springs, binary):
    binary_position = 0
    for i in range(len(springs)):
        if springs[i] == "?":
            if binary[binary_position] == '0':
                x = '.'
            elif binary[binary_position] == '1':
                x = '#'
            springs = springs[:i] + x + springs[i+1:]
            binary_position += 1
    return springs


possible_arrangements = 0
for line in data:
    springs = line.split(' ')[0]
    actual_damaged_springs = [int(i) for i in line.split(' ')[1].split(',')]
    n = len([i for i in springs if i == "?"])
    for binary in binary_combinations(n):
        option = replace_by_binary(springs, binary)
        if determine_damaged_springs(option) == actual_damaged_springs:
            possible_arrangements += 1
print(possible_arrangements)
# submit(possible_arrangements, part="a", day=day, year=year)

# part B
answer_b = 0

# print(answer_b)
# submit(answer_b, part="b", day=day, year=year)