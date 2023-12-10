from aocd import get_data, submit

year, day = 2023, 10

# parse data
data = get_data(year=year, day=day)
grid = data.split("\n")


# part A
for idy, line in enumerate(grid):
    for idx, token in enumerate(line):
        if grid[idy][idx] == 'S':
            x, y = idx, idy

def next_position(x, y, token, last_direction):
    # | is a vertical pipe connecting north and south.
    if token == "|":
        if last_direction == "S":
            y += 1
        elif last_direction == "N":
            y -= 1

    # - is a horizontal pipe connecting east and west.
    elif token == "-":
        if last_direction == "E":
            x += 1
        elif last_direction == "W":
            x -= 1

    # L is a 90-degree bend connecting north and east.
    elif token == "L":
        if last_direction == "S":
            last_direction = "E"
            x += 1
        elif last_direction == "W":
            last_direction = "N"
            y -= 1

    # J is a 90-degree bend connecting north and west.
    elif token == "J":
        if last_direction == "S":
            last_direction = "W"
            x -= 1
        elif last_direction == "E":
            last_direction = "N"
            y -= 1

    # 7 is a 90-degree bend connecting south and west.
    elif token == "7":
        if last_direction == "N":
            last_direction = "W"
            x -= 1
        elif last_direction == "E":
            last_direction = "S"
            y += 1

    # F is a 90-degree bend connecting south and east.
    elif token == "F":
        if last_direction == "N":
            last_direction = "E"
            x += 1
        elif last_direction == "W":
            last_direction = "S"
            y += 1

    elif token == 'S':
        print('at S!')
    else:
        raise Exception("don't know this token!")
    # . is ground; there is no pipe in this tile.

    return x, y, last_direction


coordinates = [{"x": x, "y": y}]

# init S in grid
last_direction = 'E'
x += 1
token = '7'
coordinates.append({"x": x, "y": y})
steps = 1

while token != 'S':
    x, y, last_direction = next_position(x, y, token, last_direction)
    steps += 1
    token = grid[y][x]
    coordinates.append({"x": x, "y": y})

new_grid = []
for idy, line in enumerate(grid):
    new_line = ""
    for idx, token in enumerate(line):
        if {"x": idx, "y": idy} in coordinates:
            new_line += grid[idy][idx]
        else:
            new_line += '.'
    new_grid.append(new_line)

answer_a = int(steps/2)
# submit(answer_a, part="a", day=day, year=year)




# part B
def next_buitenkant(token, previous_token, buitenkant):
    # | is a vertical pipe connecting north and south.
    if token == "|":
        if "E" in buitenkant:
            return "E"
        elif "W" in buitenkant:
            return "W"

    # - is a horizontal pipe connecting east and west.
    elif token == "-":
        if "N" in buitenkant:
            return "N"
        elif "S" in buitenkant:
            return "S"

    # L is a 90-degree bend connecting north and east.
    elif token == "L":
        if buitenkant == "NE" or buitenkant == "SW":
            return buitenkant

        if buitenkant == "NW" and previous_token == "F":
            return "SW"
        if buitenkant == "NW" and previous_token == "J":
            return "NE"

        if buitenkant == "SE" and previous_token == "F":
            return "NE"
        if buitenkant == "SE" and previous_token == "J":
            return "SW"

        if "S" in buitenkant or "W" in buitenkant:
            return "SW"
        elif "N" in buitenkant or "E" in buitenkant:
            return "NE"

    elif token == "7":
        if buitenkant == "NE" or buitenkant == "SW":
            return buitenkant

        if buitenkant == "NW" and previous_token == "F":
            return "NE"
        if buitenkant == "NW" and previous_token == "J":
            return "SW"

        if buitenkant == "SE" and previous_token == "F":
            return "SW"
        if buitenkant == "SE" and previous_token == "J":
            return "NE"

        if "S" in buitenkant or "W" in buitenkant:
            return "SW"
        elif "N" in buitenkant or "E" in buitenkant:
            return "NE"

    # J is a 90-degree bend connecting north and west.
    elif token == "J":
        if buitenkant == "NW" or buitenkant == "SE":
            return buitenkant

        if buitenkant == "NE" and previous_token == "7":
            return "SE"
        if buitenkant == "NE" and previous_token == "L":
            return "NW"

        if buitenkant == "SW" and previous_token == "7":
            return "NW"
        if buitenkant == "SW" and previous_token == "L":
            return "SE"

        if "S" in buitenkant or "E" in buitenkant:
            return "SE"
        if "N" in buitenkant or "W" in buitenkant:
            return "NW"

    elif token == "F":
        if buitenkant == "NW" or buitenkant == "SE":
            return buitenkant

        if buitenkant == "NE" and previous_token == "7":
            return "NW"
        if buitenkant == "NE" and previous_token == "L":
            return "SE"

        if buitenkant == "SW" and previous_token == "7":
            return "SE"
        if buitenkant == "SW" and previous_token == "L":
            return "NW"

        if "S" in buitenkant or "E" in buitenkant:
            return "SE"
        if "N" in buitenkant or "W" in buitenkant:
            return "NW"

    elif token == 'S':
        print('at S!')
    else:
        raise Exception("don't know this token!")
    # . is ground; there is no pipe in this tile.


def mark_inside_hole(gr, buitenkant, token, x, y):
    # | is a vertical pipe connecting north and south.
    if token == "|":
        if "E" == buitenkant:
            if gr[y][x-1] == ".":
                gr[y] = gr[y][:x-1] + "`" + gr[y][x:]
        elif "W" == buitenkant:
            if gr[y][x+1] == ".":
                gr[y] = gr[y][:x+1] + "`" + gr[y][x+2:]

    # - is a horizontal pipe connecting east and west.
    elif token == "-":
        if "N" == buitenkant:
            if gr[y+1][x] == ".":
                gr[y+1] = gr[y+1][:x] + "`" + gr[y+1][x+1:]
        elif "S" == buitenkant:
            if gr[y - 1][x] == ".":
                gr[y - 1] = gr[y-1][:x] + "`" + gr[y-1][x + 1:]

    # L is a 90-degree bend connecting north and east.
    elif token == "L":
        if "NE" == buitenkant:
            if gr[y + 1][x] == ".":
                gr[y + 1] = gr[y + 1][:x] + "`" + gr[y + 1][x + 1:]
            if gr[y][x-1] == ".":
                gr[y] = gr[y][:x-1] + "`" + gr[y][x:]
            if gr[y+1][x-1] == ".":
                gr[y+1] = gr[y+1][:x - 1] + "`" + gr[y+1][x:]
        elif "SW" == buitenkant:
            if gr[y - 1][x+1] == ".":
                gr[y - 1] = gr[y - 1][:x+1] + "`" + gr[y - 1][x + 2:]

    elif token == "7":
        if "NE" == buitenkant:
            if gr[y + 1][x - 1] == ".":
                gr[y + 1] = gr[y + 1][:x - 1] + "`" + gr[y + 1][x:]
        elif "SW" == buitenkant:
            if gr[y - 1][x] == ".":
                gr[y - 1] = gr[y - 1][:x] + "`" + gr[y - 1][x + 1:]
            if gr[y][x+1] == ".":
                gr[y] = gr[y][:x+1] + "`" + gr[y][x+2:]
            if gr[y - 1][x+1] == ".":
                gr[y - 1] = gr[y - 1][:x+1] + "`" + gr[y - 1][x + 2:]

    # J is a 90-degree bend connecting north and west.
    elif token == "F":
        if "SE" == buitenkant:
            if gr[y - 1][x] == ".":
                gr[y - 1] = gr[y - 1][:x] + "`" + gr[y - 1][x + 1:]
            if gr[y][x-1] == ".":
                gr[y] = gr[y][:x-1] + "`" + gr[y][x:]
            if gr[y-1][x-1] == ".":
                gr[y-1] = gr[y-1][:x - 1] + "`" + gr[y-1][x:]
        elif "NW" == buitenkant:
            if gr[y + 1][x+1] == ".":
                gr[y + 1] = gr[y + 1][:x+1] + "`" + gr[y + 1][x + 2:]

    elif token == "J":
        if "SE" == buitenkant:
            if gr[y-1][x-1] == ".":
                gr[y-1] = gr[y-1][:x - 1] + "`" + gr[y-1][x:]

        elif "NW" == buitenkant:
            if gr[y + 1][x] == ".":
                gr[y + 1] = gr[y + 1][:x] + "`" + gr[y + 1][x + 1:]
            if gr[y][x+1] == ".":
                gr[y] = gr[y][:x+1] + "`" + gr[y][x+2:]
            if gr[y + 1][x+1] == ".":
                gr[y + 1] = gr[y + 1][:x+1] + "`" + gr[y + 1][x + 2:]

    elif token == 'S':
        print('at S!')
    else:
        raise Exception("don't know this token!")
    # . is ground; there is no pipe in this tile.

    return gr


# init S in grid
last_direction = 'E'
x += 1
token = '7'
buitenkant = "SW"

while token != 'S':
    x, y, last_direction = next_position(x, y, token, last_direction)
    steps += 1
    previous_token = token
    token = grid[y][x]
    buitenkant = next_buitenkant(token, previous_token, buitenkant)
    new_grid = mark_inside_hole(new_grid, buitenkant, token, x, y)


final_grid = []
for idy, line in enumerate(new_grid):
    new_line = ""
    for idx, token in enumerate(line):
        new_line += new_grid[idy][idx] + ";"
    final_grid.append(new_line)

for i in final_grid:
    print(i)

# import this grid to Excel and color the inner Island hole fully with `, then countif cells that are `
