from aocd import get_data, submit

year, day = 2023, 15

# parse data
data = get_data(year=year, day=day)
data = data.split("\n")[0].split(",")


def hash(label):
    current_value = 0
    for c in label:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

# part A
total = 0
for label in data:
    total += hash(label)
print(total)
# submit(total, part="a", day=day, year=year)

# part B
boxes = [[] for i in range(256)]
for label in data:
    if label[-1] == "-":
        label = label[:-1]
        hash_value = hash(label)
        labels = [i[:-2] for i in boxes[hash_value]]
        if label in labels:
            idx = labels.index(label)
            boxes[hash_value].pop(idx)
    elif label[-2] == "=":
        focal_length = label[-1]
        label = label[:-2]
        hash_value = hash(label)
        labels = [i[:-2] for i in boxes[hash_value]]
        if label in labels:
            idx = labels.index(label)
            boxes[hash_value][idx] = label + " " + focal_length
        else:
            boxes[hash_value].append(label + " " + focal_length)

total = 0
for idx, box in enumerate(boxes):
    for idy, lens in enumerate(box):
        total += (idx+1) * (idy+1) * int(lens[-1])
print(total)
# submit(total, part="b", day=day, year=year)