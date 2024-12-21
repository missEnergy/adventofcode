from aocd import get_data, submit

year = 2024
day = 15

data = get_data(year=year, day=day)

# PART A
# tmp1, tmp2 = data.split('\n\n')
# grid = []
# for line in tmp1.splitlines():
#     grid.append(list(line))
# # assumption 1: the input is a square
# assert(len(grid) == len(grid[0]))
# L = len(grid)
#
# moves = []
# for line in tmp2.splitlines():
#     moves += list(line)
#
# robot_coord = (0, 0)
# for i in range(L):
#     for j in range(L):
#         if grid[i][j] == '@':
#             robot_coord = (i, j)
# grid[robot_coord[0]][robot_coord[1]] = '.'
#
#
# def move(c, move):
#     if move == '^':
#         c = (c[0] - 1, c[1])
#     elif move == 'v':
#         c = (c[0] + 1, c[1])
#     elif move == '<':
#         c = (c[0], c[1] - 1)
#     elif move == '>':
#         c = (c[0], c[1] + 1)
#     return c
#
#
# def bring_boxes_in_place_and_return_robot_coord(coords, boxes):
#     for _ in range(boxes):
#         c = coords.pop()
#         grid[c[0]][c[1]] = 'O'
#     rc = coords.pop()
#     grid[rc[0]][rc[1]] = '.'
#     for c in coords:
#         grid[c[0]][c[1]] = '.'
#     return rc
#
#
# def print_grid():
#     for i in range(L):
#         line = ''.join(grid[i])
#         if i == robot_coord[0]:
#             line = line[:robot_coord[1]] + '@' + line[robot_coord[1]+1:]
#         print(line)
#
#
# for m in moves:
#     print(f"move: {m}")
#     new_coord = move(robot_coord, m)
#     if grid[new_coord[0]][new_coord[1]] == '.':
#         robot_coord = new_coord
#     elif grid[new_coord[0]][new_coord[1]] == '#':
#         pass
#     elif grid[new_coord[0]][new_coord[1]] == 'O':
#         hit_wall = False
#         boxes = 1
#         coords = [robot_coord, new_coord]
#         while not hit_wall:
#             new_coord = move(new_coord, m)
#             if grid[new_coord[0]][new_coord[1]] == '#':
#                 hit_wall = True
#             elif grid[new_coord[0]][new_coord[1]] == '.':
#                 coords.append(new_coord)
#                 break # we are done
#             elif grid[new_coord[0]][new_coord[1]] == 'O':
#                 boxes += 1
#                 coords.append(new_coord)
#
#         robot_coord = bring_boxes_in_place_and_return_robot_coord(coords, boxes)
#     print_grid()
#
# answer = 0
# for i in range(L):
#     for j in range(L):
#         if grid[i][j] == 'O':
#             answer += i * 100 + j
# print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
tmp1, tmp2 = data.split('\n\n')
grid = []
robot_coord = (0, 0)
tmp1 = tmp1.splitlines()
for i in range(len(tmp1)):
    tmp = []
    for j in range(len(tmp1[i])):
        c = tmp1[i][j]
        if c == "#" or c == ".":
            tmp.append(c)
            tmp.append(c)
        elif c == "O":
            tmp.append("[")
            tmp.append("]")
        elif c == "@":
            tmp.append(".")
            tmp.append(".")
            robot_coord = (i, j*2)
            print(robot_coord)
    grid.append(tmp)

moves = []
for line in tmp2.splitlines():
    moves += list(line)


def move(c, move):
    if move == '^':
        c = (c[0] - 1, c[1])
    elif move == 'v':
        c = (c[0] + 1, c[1])
    elif move == '<':
        c = (c[0], c[1] - 1)
    elif move == '>':
        c = (c[0], c[1] + 1)
    return c


def bring_boxes_in_place_and_return_robot_coord_lr(move, coords, boxes):
    # this function is only for left or right movement
    assert move in ['<', '>']
    for _ in range(boxes):
        c = coords.pop()
        if move == '<':
            grid[c[0]][c[1]] = '['
        else:
            grid[c[0]][c[1]] = ']'
        c = coords.pop()
        if move == '<':
            grid[c[0]][c[1]] = ']'
        else:
            grid[c[0]][c[1]] = '['
    rc = coords.pop()
    grid[rc[0]][rc[1]] = '.'
    for c in coords:
        grid[c[0]][c[1]] = '.'
    return rc


def print_grid():
    for i in range(len(grid)):
        line = ''.join(grid[i])
        if i == robot_coord[0]:
            line = line[:robot_coord[1]] + '@' + line[robot_coord[1] + 1:]
        print(line)


for m in moves:
    print(f"move: {m}")
    new_coord = move(robot_coord, m)
    if grid[new_coord[0]][new_coord[1]] == '.':
        robot_coord = new_coord
    elif grid[new_coord[0]][new_coord[1]] == '#':
        pass
    elif grid[new_coord[0]][new_coord[1]] in ['[', ']'] and m in ['<', '>']:
        hit_wall = False
        boxes = 1
        coords = [robot_coord, new_coord]
        new_coord = move(new_coord, m) # move to end of box
        coords.append(new_coord)
        while not hit_wall:
            new_coord = move(new_coord, m)
            if grid[new_coord[0]][new_coord[1]] == '#':
                hit_wall = True
            elif grid[new_coord[0]][new_coord[1]] == '.':
                coords.append(new_coord)
                break  # we are done
            elif grid[new_coord[0]][new_coord[1]] in ['[', ']']:
                boxes += 1
                coords.append(new_coord)
                new_coord = move(new_coord, m)  # move to end of box
                coords.append(new_coord)
        robot_coord = bring_boxes_in_place_and_return_robot_coord_lr(m, coords, boxes)
    elif grid[new_coord[0]][new_coord[1]] in ['[', ']'] and m in ['^', 'v']:
        hit_wall = False
        steps = 0
        if grid[new_coord[0]][new_coord[1]] == '[':
            boxes = [(new_coord, (new_coord[0], new_coord[1] + 1))]
        else:
            boxes = [((new_coord[0], new_coord[1] - 1), new_coord)]
        outer_coords = [boxes[0][0], boxes[0][1]]

        while not hit_wall:
            new_coords = []
            for c in set(outer_coords):
                new_coords.append(move(c, m))
            new_symbols = [grid[c[0]][c[1]] for c in new_coords]
            if '#' in new_symbols:
                hit_wall = True
            elif len(new_symbols) == len([x for x in new_symbols if x == '.']):
                break  # we are done, we can move all boxes
            else: # more boxes
                outer_coords = []
                for c in new_coords:
                    if grid[c[0]][c[1]] == '[':
                        boxes.append((c, (c[0], c[1] + 1)))
                        outer_coords.append(c)
                        outer_coords.append((c[0], c[1] + 1))
                    elif grid[c[0]][c[1]] == ']':
                        boxes.append(((c[0], c[1] - 1), c))
                        outer_coords.append(c)
                        outer_coords.append((c[0], c[1] - 1))
        if not hit_wall:
            for b in boxes[::-1]:
                grid[b[0][0]][b[0][1]] = '.'
                grid[b[1][0]][b[1][1]] = '.'
                if m == '^':
                    grid[b[0][0] - 1][b[0][1]] = '['
                    grid[b[1][0] - 1][b[1][1]] = ']'
                elif m == 'v':
                    grid[b[0][0] + 1][b[0][1]] = '['
                    grid[b[1][0] + 1][b[1][1]] = ']'
            if m == '^':
                robot_coord = (robot_coord[0] - 1, robot_coord[1])
            elif m == 'v':
                robot_coord = (robot_coord[0] + 1, robot_coord[1])
    # print_grid()

answer = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '[':
            answer += i * 100 + j
print(answer)
# submit(answer, part="b", day=day, year=year)