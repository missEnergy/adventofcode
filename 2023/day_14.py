from aocd import get_data, submit
import re
year, day = 2023, 14

# parse data
platform = get_data(year=year, day=day).split("\n")

# Part A
platform_start = []
for idx in range(len(platform[0])):
    column = ""
    for idy in range(len(platform)):
        column += platform[idy][len(platform[0]) - idx - 1]
    platform_start.append(column)

def move_stones(platform):
    new_platform = []
    for col in platform:
        col = "".join(col)
        sorted_O_and_dots = []
        for between_square_rocks in re.split(r'#+', col):
            sorted_O_and_dots += sorted(between_square_rocks, reverse=True)
        sorted_col = []
        position = 0
        for i in col:
            if i != "#":
                sorted_col.append(sorted_O_and_dots[position])
                position += 1
            else:
                sorted_col.append(i)
        new_platform.append(sorted_col)
    return new_platform

answer_a = 0
for i in move_stones(platform_start):
    i.reverse()
    for idj, j in enumerate(i):
        if j == "O":
            answer_a += idj + 1
print(answer_a)
# submit(answer_a, part="a", day=day, year=year)


def make_circle(platform):
    new_platform = platform
    for i in range(4):
        new_platform = move_stones(new_platform)
        tmp_platform = []
        for j in range(len(new_platform[0])):
            tmp_row = []
            for k in range(len(new_platform)):
                tmp_row.append(new_platform[len(new_platform) - k - 1][j])
            tmp_platform.append(tmp_row)
        new_platform = tmp_platform
    return new_platform

# Part B
all_platforms = []
nxt_platform = platform_start
for i in range(1, 300):
    nxt_platform = make_circle(nxt_platform)
    if nxt_platform in all_platforms:
        break
    all_platforms.append(nxt_platform)

more_circles = (1000000000 - i) % (i - (all_platforms.index(nxt_platform) + 1))

for i in range(more_circles):
    nxt_platform = make_circle(nxt_platform)

answer_b = 0
for i in nxt_platform:
    i.reverse()
    for idj, j in enumerate(i):
        if j == "O":
            answer_b += idj + 1
print(answer_b)
submit(answer_b, part="b", day=day, year=year)