from aocd import get_data, submit

year, day = 2023, 21

# parse data
data = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
data = get_data(year=year, day=day)
grid = []
for line in data.split("\n"):
    grid.append([i for i in list(line)])
for i in grid:
    print(i)


for idy, line in enumerate(grid):
    for idx, token in enumerate(line):
        if grid[idy][idx] == 'S':
            x, y = idx, idy
            grid[idy][idx] = '.'

directions = {
    "1N": [0, -1],
    "1S": [0, 1],
    "1E": [1, 0],
    "1W": [-1, 0]
}


def walk_to_neighbors(node):
    result = []
    for d in directions.keys():
        current_x = node[0] + directions[d][0]
        current_y = node[1] + directions[d][1]
        if 0 <= current_x < len(grid[0]) and 0 <= current_y < len(grid) and grid[current_y][current_x] == ".":
            result.append((current_x, current_y))
    return set(result)


exploration = walk_to_neighbors((x, y))

for steps in range(1, 64):
    print(steps)
    new_exploration = set()
    for next_to_explore in exploration:
        new_exploration = new_exploration.union(walk_to_neighbors(next_to_explore))
    exploration = new_exploration

print(len(exploration))
# submit(len(exploration), part="a", day=day, year=year)
