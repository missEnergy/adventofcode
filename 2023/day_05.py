from aocd import get_data, submit

year, day = 2023, 5

# parse data
data = get_data(year=year, day=day).split("\n\n")
seeds = [int(i) for i in data[0].split()[1:]]
print(seeds)
maps = []
for map in data[1:]:
    map = map.split('\n')[1:]
    tmp_map = []
    for m in map:
        tmp_map.append({"dest": int(m.split()[0]), "source": int(m.split()[1]), "length": int(m.split()[2])})
    maps.append(tmp_map)

# part A
# find the lowest location number that corresponds to any of the initial seeds.
# locations = []
# for s in seeds:
#     for m in maps:
#         for r in m:
#             if r["source"] <= s < r["source"] + r["length"]:
#                 s = r["dest"] + s - r["source"]
#                 break
#     locations.append(s)
# locations.sort()

# submit(locations[0], part="a", day=day, year=year)

# part B
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append({"seed_start": seeds[i], "seed_range": seeds[i+1]})

# find the lowest location number that corresponds to any of the initial seeds.
locations = []
for s_r in seed_ranges:
    seed_start = s_r["seed_start"]
    seed_range = s_r["seed_range"]
    for m in maps:
        for r in m:
            if r["source"] <= seed_start < r["source"] + r["length"]:
                if r["source"] <= seed_start + seed_range - 1 < r["source"] + r["length"]:
                    seed_start = r["dest"] + seed_start - r["source"]
                    break
                else:
                    raise Exception("doesn't fit in range")
    locations.append(seed_start)
locations.sort()

# submit(answer_b, part="b", day=day, year=year)