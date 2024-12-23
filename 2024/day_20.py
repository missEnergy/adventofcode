from aocd import get_data, submit
import networkx as nx
from itertools import combinations

year = 2024
day = 20

data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
data = get_data(year=year, day=day)
lines = data.splitlines()

for line in lines:
    print(line)
assert len(lines) == len(lines[0])
L = len(lines)

S = (0, 0)
E = (0, 0)
blocked_nodes = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            blocked_nodes.add((y, x))
        elif c == 'S':
            S = (y, x)
        elif c == 'E':
            E = (y, x)

G = nx.Graph()
for y in range(L):
    for x in range(L):
        if (y, x) in blocked_nodes:
            continue # can't go here
        consider_nodes = {(y, x-1), (y-1, x), (y, x+1), (y+1, x)}
        consider_nodes = consider_nodes.difference(blocked_nodes)
        for node in consider_nodes:
            G.add_edge((y, x), node)
shortest_path_len = nx.shortest_path_length(G, source=S, target=E)
shortest_path_nodes = nx.shortest_path(G, source=S, target=E)
print(shortest_path_len)

# # PART A
# answer = 0
# print(f"total blocked nodes: {len(blocked_nodes)}")
# for index, bn in enumerate(blocked_nodes):
#     print(index)
#     cheat_blocked_nodes = blocked_nodes.difference({bn})
#     G = nx.Graph()
#     for y in range(L):
#         for x in range(L):
#             if (y, x) in cheat_blocked_nodes:
#                 continue # can't go here
#             consider_nodes = {(y, x-1), (y-1, x), (y, x+1), (y+1, x)}
#             consider_nodes = consider_nodes.difference(cheat_blocked_nodes)
#             for node in consider_nodes:
#                 G.add_edge((y, x), node)
#     shortest_path_cheat_len = nx.shortest_path_length(G, source=S, target=E)
#     if shortest_path_len - shortest_path_cheat_len >= 100:
#         answer += 1
# print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
# all nodes that are not blocked are used in the race, so we only need to check all >= 100 (+2 given cheat takes at least 2 steps)
# node jumps on that path and see if they are possible
minimum_save = 100 # 50 for example
max_cheat = 20
answer = 0

print(f"options = {pow(len(shortest_path_nodes) - (minimum_save+2), 2)}")
count = 0
# cheats = [0 for i in range(shortest_path_len)] # for debugging, getting the example answer

for i in range(len(shortest_path_nodes) - (minimum_save + 2) ):
    for j in range(i + (minimum_save + 2), len(shortest_path_nodes)):
        count += 1
        print(count)

        node_i = shortest_path_nodes[i] # start cheat
        node_j = shortest_path_nodes[j] # end cheat

        if abs(node_i[0] - node_j[0]) + abs(node_i[1] - node_j[1]) <= max_cheat:
            if (j-i) - (abs(node_i[0] - node_j[0]) + abs(node_i[1] - node_j[1])) >= minimum_save:
                # cheats[(j-i) - (abs(node_i[0] - node_j[0]) + abs(node_i[1] - node_j[1]))] += 1
                answer += 1

# # for debugging
# for i in range(minimum_save, shortest_path_len):
#     print(i, cheats[i])
# print('\nref') # amount of saves in example of >= 50 saved picosecs
# print(32+31+29+39+25+23+20+19+12+14+12+22+4+3)

print('answer')
print(answer)
submit(answer, part="b", day=day, year=year)