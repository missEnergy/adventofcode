from aocd import get_data, submit
import copy

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
start_direction = "u"
# assumption 2:
# assert(len(lines) == len(lines[0]))
length = len(lines)

grid = [[{"obstacle": False, "dir_prev_visit": []} for _ in range(length)] for _ in range(length)]
start_pos_guard = (0, 0)
for i in range(length):
    for j in range(length):
        if lines[i][j] == "#":
            grid[i][j]["obstacle"] = True
        if lines[i][j] == "^":
            start_pos_guard = (i, j)

def move_guard(pos, direction):
    if direction == "u":
        return (pos[0]-1, pos[1])
    if direction == "d":
        return (pos[0]+1, pos[1])
    if direction == "l":
        return (pos[0], pos[1]-1)
    if direction == "r":
        return (pos[0], pos[1]+1)

def new_direction(pos, direction, grid):
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
pos_guard = start_pos_guard
direction = start_direction
visited_coords.add(pos_guard)
while not moves_out_of_grid(pos_guard, direction):
    direction = new_direction(pos_guard, direction, grid)
    pos_guard = move_guard(pos_guard, direction)
    visited_coords.add(pos_guard)
    # print(pos_guard)
answer = len(visited_coords)
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
looping_obstacles = set()
visited_coords.remove(start_pos_guard)
count = 0
for c in visited_coords:
    count += 1

    # Create a new grid with the obstacle at c, and guard reset to start position
    pos_guard = start_pos_guard
    direction = start_direction
    grid_with_extra_obs = copy.deepcopy(grid)
    grid_with_extra_obs[pos_guard[0]][pos_guard[1]]["dir_prev_visit"].append(direction)
    grid_with_extra_obs[c[0]][c[1]]["obstacle"] = True

    # See if the guard gets in a loop
    while not moves_out_of_grid(pos_guard, direction):
        # keep on turning until we can move (no need for this in part A)
        while True:
            direction = new_direction(pos_guard, direction, grid_with_extra_obs)
            tmp_step = move_guard(pos_guard, direction)
            if not grid_with_extra_obs[tmp_step[0]][tmp_step[1]]["obstacle"]:
                break
        pos_guard = tmp_step

        if direction in grid_with_extra_obs[pos_guard[0]][pos_guard[1]]["dir_prev_visit"]:
            print(f"loop for {c}")
            print(count)
            looping_obstacles.add(c)
            break
        else:
            grid_with_extra_obs[pos_guard[0]][pos_guard[1]]["dir_prev_visit"].append(direction)

answer = len(looping_obstacles)
print(answer)
# submit(answer, part="b", day=day, year=year)