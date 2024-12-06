from aocd import get_data, submit

year = 2024
day = 6

data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
data = get_data(year=year, day=day)
lines = data.splitlines()

# INIT
# assumption 1: guard always starts in up direction
direction = "u"
# assumption 2:
# assert(len(lines) == len(lines[0]))
length = len(lines)
grid = [[{"obstacle": False} for _ in range(length)] for _ in range(length)]
pos_guard = (0, 0)
for i in range(length):
    for j in range(length):
        if lines[i][j] == "#":
            grid[i][j]["obstacle"] = True
        if lines[i][j] == "^":
            pos_guard = (i, j)
print(pos_guard)

def move_guard(pos, direction):
    if direction == "u":
        return (pos[0]-1, pos[1])
    if direction == "d":
        return (pos[0]+1, pos[1])
    if direction == "l":
        return (pos[0], pos[1]-1)
    if direction == "r":
        return (pos[0], pos[1]+1)

def new_direction(pos, direction):
    new_direction = direction
    pos_cont = move_guard(pos, direction)
    if grid[pos_cont[0]][pos_cont[1]]["obstacle"]:
        if direction == "u":
            new_direction = "r"
        if direction == "r":
            new_direction = "d"
        if direction == "d":
            new_direction = "l"
        if direction == "l":
            new_direction = "u"
    return new_direction


def moves_out_of_grid(pos, direction):
    new_pos = move_guard(pos, direction)
    if new_pos[0] < 0 or new_pos[0] >= length:
        return True
    if new_pos[1] < 0 or new_pos[1] >= length:
        return True
    return False


# PART A
visited_coords = set()
visited_coords.add(pos_guard)
while not moves_out_of_grid(pos_guard, direction):
    direction = new_direction(pos_guard, direction)
    pos_guard = move_guard(pos_guard, direction)
    visited_coords.add(pos_guard)
    print(pos_guard)
answer = len(visited_coords)
print(answer)
submit(answer, part="a", day=day, year=year)

# PART B
# submit(answer, part="b", day=day, year=year)