import math

from aocd import get_data, submit

year, day = 2023, 4

# parse data
data = get_data(year=year, day=day).split("\n")

# part A
answer_a = 0
for line in data:
    winning_numbers = line.split("|")[0].split()[2:]
    my_numbers = line.split("|")[1].split()

    matches = 0
    for i in my_numbers:
        if i in winning_numbers:
            matches = matches + 1
    if matches > 0:
        answer_a = answer_a + math.pow(2, matches - 1)

answer_a = int(answer_a)
# print(answer_a)
# submit(answer_a, part="a", day=day, year=year)

# part B
answer_b = 0
copies = [1] * len(data)

for idx, line in enumerate(data):
    winning_numbers = line.split("|")[0].split()[2:]
    my_numbers = line.split("|")[1].split()

    matches = 0
    for i in my_numbers:
        if i in winning_numbers:
            matches = matches + 1

    if matches > 0:
        for i in range(1, matches + 1):
            copies[idx + i] = copies[idx + i] + copies[idx]

answer_b = int(math.fsum(copies))

print(answer_b)
submit(answer_b, part="b", day=day, year=year)