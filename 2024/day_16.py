from aocd import get_data, submit
import networkx as nx
from itertools import combinations

year = 2024
day = 16

data = get_data(year=year, day=day)
lines = data.splitlines()

for line in lines:
    print(line)
assert len(lines) == len(lines[0])
L = len(lines)

blocked_nodes = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            blocked_nodes.add((y, x))

G = nx.Graph()
for y in range(L):
    for x in range(L):
        if y % 2 == 0 or x % 2 == 0:
            continue # not a node
        elif (y, x) in blocked_nodes:
            continue # can't go here
        elif y == L-2 and x == 1: # S
            G.add_edge((y, x), (y, x+1), weight=1)
            G.add_edge((y, x), (y-1, x), weight=1001)
        elif y == 1 and x == L-2: # E
            G.add_edge((y, x-1), (y, x), weight=1)
            G.add_edge((y+1, x), (y, x), weight=1)
        else:
            # the boundary # will make sure we don't need to worry about consider nodes going outside of grid
            consider_nodes = {(y, x-1), (y-1, x), (y, x+1), (y+1, x)}
            consider_nodes = consider_nodes.difference(blocked_nodes)
            if len(consider_nodes) == 1:
                continue # dead end
            pairs = combinations(consider_nodes, 2)
            for pair in pairs:
                if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]:
                    # no turn
                    G.add_edge(pair[0], pair[1], weight=2)
                else:
                    # turn
                    G.add_edge(pair[0], pair[1], weight=1002)
print(G)

# PART A
print(nx.shortest_path(G, source=(L-2, 1), target=(1, L-2), weight="weight"))
answer = nx.shortest_path_length(G, source=(L-2, 1), target=(1, L-2), weight="weight")
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
all_s_paths = nx.all_shortest_paths(G, source=(L-2, 1), target=(1, L-2), weight="weight")
all_s_tiles = set()
for path in all_s_paths:
    full_path = [path[0]]
    for index, p in enumerate(path[1:-2]):
        full_path.append(p)
        if p[0] == path[index+2][0]:
            full_path.append((p[0], (p[1] + path[index+2][1])//2))
        elif p[1] == path[index+2][1]:
            full_path.append(((p[0] + path[index+2][0])//2, p[1]))
        else:
            option1 = (p[0], path[index+2][1])
            option2 = (path[index+2][0], p[1])
            if option1 not in blocked_nodes:
                full_path.append(option1)
            else:
                full_path.append(option2)
    full_path.append(path[-2])
    full_path.append(path[-1])
    all_s_tiles = all_s_tiles.union(set(full_path))
answer = len(all_s_tiles) 
print(answer)   

# for y in range(L):
#     for x in range(L):
#         if (y, x) in all_s_tiles:
#             print("O", end="")
#         elif (y, x) in blocked_nodes:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print('')

# submit(answer, part="b", day=day, year=year)