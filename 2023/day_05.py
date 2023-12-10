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
locations = []
for s in seeds:
    for m in maps:
        for r in m:
            if r["source"] <= s < r["source"] + r["length"]:
                s = r["dest"] + s - r["source"]
                break
    locations.append(s)
locations.sort()

submit(locations[0], part="a", day=day, year=year)

# part B
# GOOGLE SHEET BABY!
