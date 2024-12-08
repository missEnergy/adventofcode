from aocd import get_data, submit
from itertools import combinations

year = 2024
day = 8

data = get_data(year=year, day=day)
lines = data.splitlines()
for line in lines:
    print(line)

# assumption 1: the input is a square
assert(len(lines) == len(lines[0]))
L = len(lines)

frq_antenna_dict = dict()
for i in range(L):
    for j in range(L):
        if lines[i][j] != '.':
            if lines[i][j] not in frq_antenna_dict:
                frq_antenna_dict[lines[i][j]] = []
            frq_antenna_dict[lines[i][j]].append((i, j))

# PART A
antinodes = set()
for frq in frq_antenna_dict.keys():
    antennas = frq_antenna_dict[frq]
    print(frq, antennas)
    pairs = combinations(antennas, 2)
    for pair in pairs:
        print(pair)
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        antinode1 = (x1 - (x2-x1), y1 - (y2-y1))
        if antinode1[0] >= 0 and antinode1[0] < L and antinode1[1] >= 0 and antinode1[1] < L:
            antinodes.add(antinode1)

        antinode2 = (x2 + (x2 - x1), y2 + (y2 - y1))
        if antinode2[0] >= 0 and antinode2[0] < L and antinode2[1] >= 0 and antinode2[1] < L:
            antinodes.add(antinode2)
answer = len(antinodes)
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
antinodes = set()
for frq in frq_antenna_dict.keys():
    antennas = frq_antenna_dict[frq]
    print(frq, antennas)
    pairs = combinations(antennas, 2)
    for pair in pairs:
        print(pair)
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        xn, yn = x1, y1
        while xn >= 0 and xn < L and yn >= 0 and yn < L:
            antinodes.add((xn, yn))
            xn -= (x2 - x1)
            yn -= (y2 - y1)

        xn, yn = x2, y2
        while xn >= 0 and xn < L and yn >= 0 and yn < L:
            antinodes.add((xn, yn))
            xn += (x2 - x1)
            yn += (y2 - y1)

answer = len(antinodes)
print(answer)
# submit(answer, part="b", day=day, year=year)