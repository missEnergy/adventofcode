import math

from aocd import get_data, submit

year, day = 2023, 8

# parse data
instructions = get_data(year=year, day=day).split("\n\n")[0]
maps = {}
for line in get_data(year=year, day=day).split("\n\n")[1].split('\n'):
    point, L, R = line[:3], line[7:10], line[12:15]
    maps[point] = {'L': L, 'R': R}

# part A
steps, location = 0, 'AAA'
while not location == 'ZZZ':
    direction = instructions[steps % len(instructions)]
    location = maps[location][direction]
    steps = steps + 1
# submit(steps, part="a", day=day, year=year)

# part B
cycle_steps = []
for loc in [i for i in maps.keys() if i[2] == 'A']:
    steps = 0
    while loc[2] != 'Z':
        direction = instructions[steps % len(instructions)]
        loc = maps[loc][direction]
        steps = steps + 1
    cycle_steps.append(steps)
import math
# submit(math.lcm(*cycle_steps), part="b", day=day, year=year)