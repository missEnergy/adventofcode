from aocd import get_data, submit
import math

year, day = 2023, 6

# part A
data = get_data(year=year, day=day).split("\n")
race_data = []
for line in data:
    race_data.append(line.split()[1:])
w_s = []
for index, item in enumerate(race_data[0]):
    time = int(item)
    distance = int(race_data[1][index])
    winning_strategies = 0
    for i in range(time):
        potential_distance = i * (time - i)
        if potential_distance > distance:
            winning_strategies = winning_strategies + 1
    w_s.append(winning_strategies)
answer_a = math.prod(w_s)

# print(answer_a)
# submit(answer_a, part="a", day=day, year=year)

# part B
data = get_data(year=year, day=day).split("\n")
race_data = []
for line in data:
    race_data.append("".join(line.split()[1:]))
time = int(race_data[0])
distance = int(race_data[1])
winning_strategies = 0
for i in range(time):
    potential_distance = i * (time - i)
    if potential_distance > distance:
        winning_strategies = winning_strategies + 1
answer_b = winning_strategies

print(answer_b)
submit(answer_b, part="b", day=day, year=year)