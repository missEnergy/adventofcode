from aocd import get_data, submit

year = 2024
day = 9

data = get_data(year=year, day=day)
print(data)

# PART A
diskmap = []
id = 0
is_free = False
for c in map(int, data):
    if not is_free:
        for _ in range(c):
            diskmap.append(id)
        id += 1
    else:
        for _ in range(c):
            diskmap.append(".")
    is_free = not is_free
# print(diskmap)

while "." in diskmap:
    move = diskmap.pop()
    try:
        diskmap.insert(diskmap.index('.'), move)
        diskmap.pop(diskmap.index('.'))
    except:
        print("the end!")
    # print(diskmap)

answer = 0
for i in range(len(diskmap)):
    answer += diskmap[i] * i
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
diskmap = []
id = 0
is_free = False
for c in map(int, data):
    if not is_free:
        diskmap.append({"is_free": is_free, "id": id, "len": c})
        id += 1
    else:
        diskmap.append({"is_free": is_free, "id": None, "len": c})
    is_free = not is_free

id -= 1

while id >= 0:
    move = [i for i in diskmap if i["id"] == id][0]
    move_index = diskmap.index(move)
    fit = [i for i in diskmap if i["is_free"] and i["len"] >= move["len"]]
    if len(fit) > 0:
        fit = fit[0]
        fit_index = diskmap.index(fit)
        if fit_index > move_index:
            id -= 1
            continue
        if fit["len"] > move["len"]:
            fit["len"] -= move["len"]
            diskmap[fit_index] = fit
            diskmap[move_index] = {"is_free": True, "id": None, "len": move["len"]}
            diskmap.insert(fit_index, move)
        else:
            diskmap[move_index] = {"is_free": True, "id": None, "len": move["len"]}
            diskmap[fit_index] = move
    id -= 1
    print(id)

print (diskmap)
answer = 0
index = 0
for i in diskmap:
    if i["is_free"]:
        index += i["len"]
    else:
        for _ in range(i["len"]):
            answer += i["id"] * index
            index += 1

print(answer)
# submit(answer, part="b", day=day, year=year)