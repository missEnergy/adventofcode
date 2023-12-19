from aocd import get_data, submit

year, day = 2023, 18

# parse data
data = get_data(year=year, day=day).split("\n")
# print(data)

# SET THIS ONE TO LAST INSTRUCTION
last_direction = "U"

x, y = 0, 0
instructions = []
for line in data:
    instr = line.split()

    # PART A
    # steps = int(instr[1])
    # # PART B
    steps = int(instr[2][2:-2], 16)

    # PART A
    # direction = instr[0]

    # # PART B
    direction = None
    if instr[2][-2] == '0':
        direction = 'R'
    elif instr[2][-2] == '1':
        direction = 'D'
    elif instr[2][-2] == '2':
        direction = 'L'
    elif instr[2][-2] == '3':
        direction = 'U'

    print(f"x {x}, y {y}")
    if direction == "R":
        if last_direction == "U":
            corner_coordinate = [x - 0.5, y - 0.5]
        elif last_direction == "D":
            corner_coordinate = [x + 0.5, y - 0.5]
        x += steps

    elif direction == "L":
        if last_direction == "U":
            corner_coordinate = [x - 0.5, y + 0.5]
        elif last_direction == "D":
            corner_coordinate = [x + 0.5, y + 0.5]
        x -= steps

    elif direction == "U":
        if last_direction == "R":
            corner_coordinate = [x - 0.5, y - 0.5]
        elif last_direction == "L":
            corner_coordinate = [x - 0.5, y + 0.5]
        y -= steps

    elif direction == "D":
        if last_direction == "R":
            corner_coordinate = [x + 0.5, y - 0.5]
            print(corner_coordinate)
        elif last_direction == "L":
            corner_coordinate = [x + 0.5, y + 0.5]
        y += steps

    else:
        raise Exception("can't be!")

    last_direction = direction
    instructions.append({"direction": direction, "steps": steps, "corner_coordinate": corner_coordinate})
print(len(instructions))

# https://en.wikipedia.org/wiki/Shoelace_formula
area = 0
for index, i in enumerate(instructions):
    try:
        area += i["corner_coordinate"][1] * (instructions[index - 1]["corner_coordinate"][0] - instructions[index + 1]["corner_coordinate"][0])
    except:
        # final instruction case
        area += i["corner_coordinate"][1] * (instructions[index - 1]["corner_coordinate"][0] - instructions[0]["corner_coordinate"][0])
area = area / 2
print(area)
