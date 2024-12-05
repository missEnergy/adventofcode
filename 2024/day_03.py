from aocd import get_data, submit
import re

year = 2024
day = 3

data = get_data(year=year, day=day)

# PART A
# valid_muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
# answer = 0
# for mul in valid_muls:
#     a, b = map(int, mul[4:-1].split(","))
#     answer += a * b
# submit(answer, part="a", day=day, year=year)

# PART B
valid_muls = re.findall(r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", data)
answer = 0
do = True
for mul in valid_muls:
    if mul == "do()":
        do = True
        continue
    if mul == "don't()":
        do = False
        continue
    a, b = map(int, mul[4:-1].split(","))
    if do:
        answer += a * b
submit(answer, part="b", day=day, year=year)