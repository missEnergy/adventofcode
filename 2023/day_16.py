from aocd import get_data, submit

year, day = 2023, 16

# parse data
data = get_data(year=year, day=day).split("\n")
nice_data = []
for line in data:
    nice_line = ""
    for c in line:
        if c == "\\":
            nice_line += "`"
        else:
            nice_line += c
    nice_data.append(list(nice_line))

def beam_to_next_position(beam, tile):
    idx, idy, direction = beam["idx"], beam["idy"], beam["direction"]
    idx2, idy2, direction2 = None, None, None

    if tile == ".":
        if direction == "N":
            idy -= 1
        elif direction == "S":
            idy += 1
        elif direction == "E":
            idx += 1
        elif direction == "W":
            idx -= 1

    elif tile == "`":
        if direction == "N":
            direction = "W"
            idx -= 1
        elif direction == "S":
            direction = "E"
            idx += 1
        elif direction == "E":
            direction = "S"
            idy += 1
        elif direction == "W":
            direction = "N"
            idy -= 1

    elif tile == "/":
        if direction == "N":
            direction = "E"
            idx += 1
        elif direction == "S":
            direction = "W"
            idx -= 1
        elif direction == "E":
            direction = "N"
            idy -= 1
        elif direction == "W":
            direction = "S"
            idy += 1

    elif tile == "|":
        if direction == "N":
            idy -= 1
        elif direction == "S":
            idy += 1
        elif direction == "E" or direction == "W":
            idx2, idy2, direction2 = idx, idy, direction
            # 1 beam to north
            direction = "N"
            idy -= 1
            # 1 beam to south
            direction2 = "S"
            idy += 1

    elif tile == "-":
        if direction == "E":
            idx += 1
        elif direction == "W":
            idx -= 1
        elif direction == "N" or direction == "S":
            idx2, idy2, direction2 = idx, idy, direction
            # 1 beam to east
            direction = "E"
            idx += 1
            # 1 beam to west
            direction2 = "W"
            idx -= 1

    if idx < 0 or idy < 0 or idx >= len(nice_data[0]) or idy >= len(nice_data):
        beam1 = None
    else:
        beam1 = {"idx": idx, "idy": idy, "direction": direction}

    if idx2 is None:
        return [beam1]
    else:
        if idx2 < 0 or idy2 < 0 or idx2 >= len(nice_data[0]) or idy2 >= len(nice_data):
            beam2 = None
        else:
            beam2 = {"idx": idx2, "idy": idy2, "direction": direction2}
        return [beam1, beam2]


def find_energized_tiles_for_start(start_beam):
    finished_beams = []
    energized_tiles = [[] for i in range(len(nice_data))]

    beams_to_finish = [start_beam]
    energized_tiles[start_beam["idy"]].append(start_beam["idx"])

    while len(beams_to_finish) > 0:
        current_beam = beams_to_finish[0]
        current_tile = nice_data[current_beam["idy"]][current_beam["idx"]]
        beams_to_finish.pop(0)
        finished_beams.append(current_beam)
        new_beams = beam_to_next_position(current_beam, current_tile)
        for new_beam in new_beams:
            if new_beam is None:
                continue
            energized_tiles[new_beam["idy"]].append(new_beam["idx"])
            if new_beam not in finished_beams:
                beams_to_finish.append(new_beam)

    total = 0
    for i in energized_tiles:
        total += len(set(i))
    return total

# part A
answer_a = find_energized_tiles_for_start({"idx": 0, "idy": 0, "direction": "E"})
print(answer_a)
submit(answer_a, part="a", day=day, year=year)

# part B
answer_b = 0
potential_starts = []
for i in range(len(nice_data[0])):
    potential_starts.append({"idx": i, "idy": 0, "direction": "S"})
    potential_starts.append({"idx": i, "idy": len(nice_data) - 1, "direction": "N"})
for i in range(len(nice_data)):
    potential_starts.append({"idx": 0, "idy": i, "direction": "E"})
    potential_starts.append({"idx": len(nice_data[0]) - 1, "idy": i, "direction": "W"})

for i in potential_starts:
    new_answer = find_energized_tiles_for_start(i)
    print(new_answer)
    answer_b = max(answer_b, new_answer)

print(answer_b)
# submit(answer_b, part="b", day=day, year=year)