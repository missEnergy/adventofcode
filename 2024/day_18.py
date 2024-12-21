from aocd import get_data, submit
import networkx as nx

year = 2024
day = 18

data = get_data(year=year, day=day)
grid_size = 70 + 1
nanosec = 1024

lines = data.splitlines()
blocked_nodes = set()
for line in lines[:nanosec]:
    y, x = map(int, line.split(","))
    blocked_nodes.add((y, x))

# PART A
G = nx.Graph()
for y in range(grid_size):
    for x in range(grid_size):
        if (y, x) in blocked_nodes:
            continue
        if (y, x+1) not in blocked_nodes and x+1 < grid_size:
            G.add_edge((y, x), (y, x+1), capacity=1)
        if (y+1, x) not in blocked_nodes and y+1 < grid_size:
            G.add_edge((y, x), (y+1, x), capacity=1)
print(G)

shortest_path = nx.shortest_path(G, source=(0, 0), target=(grid_size-1, grid_size-1))
print(shortest_path)
answer = len(shortest_path) - 1
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
has_path = True
while has_path:
    nanosec += 1
    line = lines[nanosec-1]
    y_block, x_block = map(int, line.split(","))
    blocked_nodes.add((y_block, x_block))

    G = nx.Graph()
    for y in range(grid_size):
        for x in range(grid_size):
            if (y, x) in blocked_nodes:
                continue
            if (y, x+1) not in blocked_nodes and x+1 < grid_size:
                G.add_edge((y, x), (y, x+1), capacity=1)
            if (y+1, x) not in blocked_nodes and y+1 < grid_size:
                G.add_edge((y, x), (y+1, x), capacity=1)
    try:
        shortest_path = nx.shortest_path(G, source=(0, 0), target=(grid_size-1, grid_size-1))
    except nx.NetworkXNoPath:
        has_path = False
        break
answer = f"{y_block},{x_block}"
print(answer)
# submit(answer, part="b", day=day, year=year)