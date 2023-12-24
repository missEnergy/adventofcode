from aocd import get_data, submit
import copy

year, day = 2023, 22

# parse data
data = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""
data = get_data(year=year, day=day)
bricks = []
print(len(data.split("\n")))
for line in data.split("\n"):
    x0, y0, z0 = line.split("~")[0].split(",")
    x1, y1, z1 = line.split("~")[1].split(",")
    bricks.append([(int(x0), int(y0), int(z0)), (int(x1), int(y1), int(z1))])
for b in bricks:
    print(b)
print()


def sits_on_ground_or_other_brick(brick):
    # sits on ground
    if brick[0][2] == 1 or brick[1][2] == 1:
        return True

    z_to_look_for_obstacle = min(brick[0][2], brick[1][2]) - 1
    candidate_bricks_to_sit_on = [b for b in bricks if b[0][2] == z_to_look_for_obstacle or b[1][2] == z_to_look_for_obstacle]

    brick_x_ys = set()
    for x in range(min(brick[0][0], brick[1][0]), max(brick[0][0], brick[1][0]) + 1):
        for y in range(min(brick[0][1], brick[1][1]), max(brick[0][1], brick[1][1]) + 1):
            brick_x_ys.add((x, y))

    for b in candidate_bricks_to_sit_on:
        b_x_ys = set()
        for x in range(min(b[0][0], b[1][0]), max(b[0][0], b[1][0]) + 1):
            for y in range(min(b[0][1], b[1][1]), max(b[0][1], b[1][1]) + 1):
                b_x_ys.add((x, y))
        if len(b_x_ys.intersection(brick_x_ys)) > 0:
            return True

    return False


def supported_by(brick, all_bricks):
    support_bricks = []

    # sits on ground
    if brick[0][2] == 1 or brick[1][2] == 1:
        return support_bricks

    z_to_look_for_obstacle = min(brick[0][2], brick[1][2]) - 1
    candidate_bricks_to_sit_on = [b for b in all_bricks if b[0][2] == z_to_look_for_obstacle or b[1][2] == z_to_look_for_obstacle]

    brick_x_ys = set()
    for x in range(min(brick[0][0], brick[1][0]), max(brick[0][0], brick[1][0]) + 1):
        for y in range(min(brick[0][1], brick[1][1]), max(brick[0][1], brick[1][1]) + 1):
            brick_x_ys.add((x, y))

    for b in candidate_bricks_to_sit_on:
        b_x_ys = set()
        for x in range(min(b[0][0], b[1][0]), max(b[0][0], b[1][0]) + 1):
            for y in range(min(b[0][1], b[1][1]), max(b[0][1], b[1][1]) + 1):
                b_x_ys.add((x, y))
        if len(b_x_ys.intersection(brick_x_ys)) > 0:
            support_bricks.append(b)

    return support_bricks


# bring bricks to final position
print("Start bringing bricks to position.")
print()
no_change_count = 0
while True:
    brick = bricks[0]
    bricks.pop(0)

    change_count = 0
    while not sits_on_ground_or_other_brick(brick):
        change_count += 1
        brick = [(brick[0][0], brick[0][1], brick[0][2] - 1), (brick[1][0], brick[1][1], brick[1][2] - 1)]
    bricks.append(brick)

    no_change_count = no_change_count + 1 if change_count == 0 else 0
    # stop if you can't move any brick down anymore
    if no_change_count == len(bricks):
        break

# part A
print("start safely_disintegrateble calculation")
support_structure = []
for b in bricks:
    support_structure.append([b, supported_by(b, bricks)])

safely_disintegrateble = copy.deepcopy(bricks)
for b in support_structure:
    if len(b[1]) == 1:
        try:
            safely_disintegrateble.remove(b[1][0])
            print("can't disintegrate", b[1][0])
        except:
            print("can't disintegrate for multiple support", b[1][0])
print(len(safely_disintegrateble))
print()
# submit(len(safely_disintegrateble), part="a", day=day, year=year)

# part B
print("start fall paths calculation")
fallen_paths = []
for idx, b in enumerate(bricks):
    print(idx, b)
    fallen = [b]
    while True:
        new_fall = False
        for ss in support_structure:
            if ss[0] in fallen:
                continue
            append_checks = []
            for i in ss[1]:
                if i in fallen:
                    append_checks.append("yes")
                else:
                    append_checks.append("no")
            if set(append_checks) == {"yes"}:
                fallen.append(ss[0])
                new_fall = True
        if not new_fall:
            break
    fallen_paths.append(fallen)

answer_b = sum([len(i) - 1 for i in fallen_paths])
submit(answer_b, part="b", day=day, year=year)