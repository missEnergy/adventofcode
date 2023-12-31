from aocd import get_data, submit
import networkx as nx

year, day = 2023, 25

# parse data
data = get_data(year=year, day=day)

G = nx.Graph()
for line in data.split("\n"):
    left = line.split(": ")[0]
    for right in line.split(": ")[1].split(" "):
        G.add_edge(left, right, capacity=1)

# Solution algo = https://en.wikipedia.org/wiki/Minimum_cut
print(G)
min_cut = nx.minimum_cut(G, "kzb", "sfh")  # picked 2 random nodes till found cutsize = 3
print(min_cut)
answer = len(min_cut[1][0]) * len(min_cut[1][1])
print(answer)
