from aocd import get_data, submit
import re

year = 2024
day = 4

data = get_data(year=year, day=day)
lines = data.splitlines()
for line in lines:
    print(line)

assert(len(lines) == len(lines[0]))
length = len(lines)

# PART A
horizontals = lines

verticals = []
for i in range(length):
    new_str = ""
    for j in range(length):
        new_str += lines[j][i]
    verticals.append(new_str)

def make_diagonals(lines):
    diags = []
    for i in range(length):
        new_str = ""
        for j in range(i+1):
            new_str += lines[i-j][j]
        diags.append(new_str)
    for i in range(length-1):
        new_str = ""
        for j in range(i+1):
            new_str += lines[length-1-(i-j)][length-1-j]
        diags.append(new_str)
    return diags

diagonals_horizontal = make_diagonals(horizontals)

hori_back = []
for line in horizontals:
    hori_back.append(line[::-1])
diagonals_hori_back = make_diagonals(hori_back)


def find_all_XMAS(lines):
    x = 0
    for line in lines:
        print(line)
        x += len(re.findall("XMAS", line))
        x += len(re.findall("XMAS", line[::-1]))
    return x


answer = (
        find_all_XMAS(horizontals)
        + find_all_XMAS(verticals)
        + find_all_XMAS(diagonals_horizontal)
        + find_all_XMAS(diagonals_hori_back)
)
print(answer)
# submit(answer, part="a", day=day, year=year)

# # PART B
horizontals = lines
hori_back = []
for line in horizontals:
    hori_back.append(line[::-1])


def make_forw_diags(lines):
    diags = []
    for i in range(length):
        new_str = ""
        for j in range(i+1):
            new_str += lines[i-j][j]
        diags.append({"str": new_str, "start_line": i, "start_pos": 0})
    for i in range(length-1):
        new_str = ""
        for j in range(i+1):
            new_str += lines[length-1-(i-j)][length-1-j]
        new_str = new_str[::-1]
        diags.append({"str": new_str, "start_line": length - 1, "start_pos": length - 1 - i})
    return diags


def make_back_diags(lines):
    diags = []
    for i in range(length):
        new_str = ""
        for j in range(i+1):
            new_str += lines[i-j][j]
        new_str = new_str[::-1]
        diags.append({"str": new_str, "start_line": 0, "start_pos": length - 1 - i})
    for i in range(length-1):
        new_str = ""
        for j in range(i+1):
            new_str += lines[length-1-(i-j)][length-1-j]
        diags.append({"str": new_str, "start_line": length - 1 - i, "start_pos": 0})
    return diags

forw_diags = make_forw_diags(horizontals)
back_diags = make_back_diags(hori_back)


def find_all_MAS_A_coordinates_forw(diags):
    coordinates = []
    for line in diags:
        for x in re.finditer(r"(?=(?:MAS|SAM))", line['str']):
            coordinates.append((line['start_line']-x.start()-1, line['start_pos']+x.start()+1))
    return coordinates


def find_all_MAS_A_coordinates_back(diags):
    coordinates = []
    for line in diags:
        for x in re.finditer(r"(?=(?:MAS|SAM))", line['str']):
            coordinates.append((line['start_line']+x.start()+1, line['start_pos']+x.start()+1))
    return coordinates

coor_A_forw = find_all_MAS_A_coordinates_forw(forw_diags)
coor_A_back = find_all_MAS_A_coordinates_back(back_diags)

A_X = [a for a in coor_A_forw if a in coor_A_back]
print(A_X)
answer = len(A_X)
print(answer)
# submit(answer, part="b", day=day, year=year)