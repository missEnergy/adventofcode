from aocd import get_data, submit

year = 2024
day = 12

data = get_data(year=year, day=day)
lines = data.splitlines()

# assumption 1: the input is a square
assert(len(lines) == len(lines[0]))
L = len(lines)

unexplored_coords = []
for i in range(L):
    for j in range(L):
        unexplored_coords.append((i, j))

plots = []
nxt = unexplored_coords[0]
flooding_plot = {"char": lines[nxt[0]][nxt[1]], "coords": {nxt}, "explored": {}}
unexplored_coords.remove(nxt)
while len(unexplored_coords) > 0:
    print(len(unexplored_coords))
    new_coords = set()
    for c in flooding_plot["coords"].difference(flooding_plot["explored"]):
        try_coords = [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)]
        for tc in try_coords:
            if tc in unexplored_coords:
                if lines[tc[0]][tc[1]] == flooding_plot["char"]:
                    new_coords.add(tc)
                    unexplored_coords.remove(tc)
    if len(new_coords) > 0:
        flooding_plot = {"char": flooding_plot["char"], "coords": flooding_plot["coords"].union(new_coords), "explored": flooding_plot["coords"]}
    else:
        plots.append(flooding_plot)
        nxt = unexplored_coords[0]
        flooding_plot = {"char": lines[nxt[0]][nxt[1]], "coords": {nxt}, "explored": {}}
        unexplored_coords.remove(nxt)
plots.append(flooding_plot)

# PART A
answer = 0
for p in plots:
    print(p["char"])
    area = len(p["coords"])
    perimeter = 0
    for c in p["coords"]:
        try_coords = [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)]
        for tc in try_coords:
            if tc not in p["coords"]:
                perimeter += 1
    print(area, perimeter, area * perimeter)
    answer += area * perimeter
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
answer = 0
for p in plots:
    print(p["char"])
    area = len(p["coords"])

    side_store = []
    for c in p["coords"]:
        # 0=up, 1=down, 2=right, 3=left
        try_coords = [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)]
        for i in range(4):
            if try_coords[i] not in p["coords"]:
                # 0=up, 1=down, 2=right, 3=left
                side_store.append({"dir": i, "c": c})
    print(side_store)

    sides = 0
    ups = [s["c"] for s in side_store if s["dir"] == 0]
    for c in ups:
        if not (c[0], c[1]+1) in ups:
            sides += 1

    downs = [s["c"] for s in side_store if s["dir"] == 1]
    for c in downs:
        if not (c[0], c[1] + 1) in downs:
            sides += 1

    rights = [s["c"] for s in side_store if s["dir"] == 2]
    for c in rights:
        if not (c[0]+1, c[1]) in rights:
            sides += 1

    lefts = [s["c"] for s in side_store if s["dir"] == 3]
    for c in lefts:
        if not (c[0] + 1, c[1]) in lefts:
            sides += 1

    print(area, sides, area * sides)
    answer += area * sides
print(answer)
# submit(answer, part="b", day=day, year=year)
