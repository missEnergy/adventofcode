from aocd import get_data, submit

year, day = 2023, 11

# part A
# expansion_factor = 1
# part B
expansion_factor = 999999

space = get_data(year=year, day=day).split('\n')

galaxies = []
empty_rows = []
empty_columns = []

for idy, row in enumerate(space):
    for idx, item in enumerate(row):
        if item == "#":
            galaxies.append({"x": idx, "y": idy})
    if set(row) == {'.'}:
        empty_rows.append(idy)

for idx in range(len(space[0])):
    column = ""
    for idy in range(len(space)):
        column += space[idy][idx]
    if set(column) == {'.'}:
        empty_columns.append(idx)

total_path = 0
for i in range(0, len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        g1, g2 = galaxies[i], galaxies[j]
        if g1['x'] <= g2['x']:
            x1, x2 = g1['x'], g2['x']
        else:
            x1, x2 = g2['x'], g1['x']

        shortest_path = (
            abs(g1['y'] - g2['y'])
            + abs(g1['x'] - g2['x'])
            + expansion_factor * len([c for c in empty_columns if x1 < c < x2])
            + expansion_factor * len([r for r in empty_rows if g1['y'] < r < g2['y']])
        )
        total_path += shortest_path

print(total_path)
# submit(total_path, part="a", day=day, year=year)
# submit(total_path, part="b", day=day, year=year)
