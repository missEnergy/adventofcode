from aocd import get_data, submit

year, day = 2023, 24

# parse data
data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
# data = get_data(year=year, day=day)

stones = []
for line in data.split("\n"):
    px, py, pz = line.split(" @ ")[0].split(", ")
    vx, vy, vz = line.split(" @ ")[1].split(", ")
    stones.append([(int(px), int(py), int(pz)), (int(vx), int(vy), int(vz))])

for i in range(0, len(stones) - 1):
    for j in range(i + 1, len(stones)):
        print(stones[i], stones[j])




# part A
answer_a = 0

# print(answer_a)
# submit(answer_a, part="a", day=day, year=year)

# part B
answer_b = 0

# print(answer_b)
# submit(answer_b, part="b", day=day, year=year)