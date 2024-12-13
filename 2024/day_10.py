from aocd import get_data, submit

year = 2024
day = 10

data = get_data(year=year, day=day)
lines = data.splitlines()

# assumption 1: the input is a square
assert(len(lines) == len(lines[0]))
L = len(lines)

grid = []
zeros = []
for i in range(L):
    grid_line = []
    for j in range(L):
        grid_line.append(int(lines[i][j]))
        if int(lines[i][j]) == 0:
            zeros.append((i, j))
    grid.append(grid_line)
print(grid)
print(zeros)

# PART A
answer = 0
for zero in zeros:
    next_height = 1
    valid_paths = set()
    valid_paths.add(zero)
    while next_height <= 9:
        next_paths = set()
        for path in valid_paths:
            try_tiles = [(path[0] + 1, path[1]), (path[0] - 1, path[1]), (path[0], path[1] + 1), (path[0], path[1] - 1)]
            try_tiles = [t for t in try_tiles if t[0] >= 0 and t[0] < L and t[1] >= 0 and t[1] < L]
            for t in try_tiles:
                if grid[t[0]][t[1]] == next_height:
                    next_paths.add(t)
        valid_paths = next_paths
        next_height += 1
    answer += len(valid_paths)
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
answer = 0
for zero in zeros:
    next_height = 1
    valid_paths = []
    valid_paths.append(zero)
    while next_height <= 9:
        next_paths = []
        for path in valid_paths:
            try_tiles = [(path[0] + 1, path[1]), (path[0] - 1, path[1]), (path[0], path[1] + 1), (path[0], path[1] - 1)]
            try_tiles = [t for t in try_tiles if t[0] >= 0 and t[0] < L and t[1] >= 0 and t[1] < L]
            for t in try_tiles:
                if grid[t[0]][t[1]] == next_height:
                    next_paths.append(t)
        valid_paths = next_paths
        next_height += 1
    answer += len(valid_paths)
print(answer)
# submit(answer, part="b", day=day, year=year)