from aocd import get_data, submit
import math

year, day = 2023, 23

# parse data
data = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
data = get_data(year=year, day=day)

# parse data
grid = []
for line in data.split("\n"):
    grid.append([i for i in list(line)])
print(len(grid), len(grid[0]))
for i in grid:
    print(i)

y_start = 0
x_start = grid[y_start].index(".")

y_end = len(grid) - 1
x_end = grid[y_end].index(".")

directions = {
    "^": [0, -1],
    "v": [0, 1],
    ">": [1, 0],
    "<": [-1, 0]
}


def find_new_paths(node):
    node_xy = node
    paths_to_walk = []

    # first check which new directions we can go from this junction node
    for k, v in directions.items():
        current_x = node_xy[0] + v[0]
        current_y = node_xy[1] + v[1]
        # it should not be outside the grid
        if 0 <= current_x < len(grid[0]) and 0 <= current_y < len(grid):
            # it should be on a possible tile
            if grid[current_y][current_x] in [".", "^", "v", "<", ">"]:
                # it should be on a non-visited tile of the graph we are building
                to_consider = True
                try:
                    for edge in graph[str((node_xy[0], node_xy[1]))]:
                        if (current_x, current_y) in edges[edge]["nodes"]:
                            to_consider = False
                except:
                    to_consider = True
                if to_consider:
                    paths_to_walk.append([node_xy, (current_x, current_y)])

    # walk the paths until you are at a junction again
    dead_end_indexes = []
    final_paths_walked = []
    for index, ptw in enumerate(paths_to_walk):
        while True:
            possible_next_steps = []
            for k, v in directions.items():
                current_x = ptw[-1][0] + v[0]
                current_y = ptw[-1][1] + v[1]
                if 0 <= current_x < len(grid[0]) and 0 <= current_y < len(grid):
                    # it should be on a possible tile
                    if grid[current_y][current_x] in [".", "^", "v", "<", ">"]:
                        # it should be on a non-visited tile
                        if (current_x, current_y) not in ptw:
                            possible_next_steps.append((current_x, current_y))

            if len(possible_next_steps) > 1:
                # on a junction node, stop path
                break
            elif len(possible_next_steps) == 1:
                ptw.append(possible_next_steps[0])
            else:
                if ptw[-1] == (x_end, y_end):
                    # is path to end node!
                    break
                else:
                    print("dead end")
                    # dead end, don't consider this path further!
                    dead_end_indexes.append(index)
                    break
        if index not in dead_end_indexes:
            final_paths_walked.append(ptw)

    # add the edges to the graph and edges mapping
    for ptw in final_paths_walked:
        path_nodes = set(ptw)
        if path_nodes in [i["nodes"] for i in edges]:
            new_edge = [i["nodes"] for i in edges].index(path_nodes)
        else:
            new_edge = len(edges)
            edges.append({
                "end_nodes": set([node, ptw[-1]]),
                "nodes": path_nodes,
                "costs": -(len(path_nodes) - 1)
            })
        try:
            graph[str(node)].add(new_edge)
        except:
            graph[str(node)] = set([new_edge])
        try:
            graph[str(ptw[-1])].add(new_edge)
        except:
            graph[str(ptw[-1])] = set([new_edge])

    # return the end nodes of the walked paths, which are next to explore
    return [i[-1] for i in final_paths_walked]


# create alternative grid
edges = []
graph = {}
exploration = find_new_paths((x_start, y_start))
while len(exploration) > 0:
    index_min = 0
    next_to_explore = exploration[index_min]
    exploration.pop(index_min)
    exploration += find_new_paths(next_to_explore)

for i in edges:
    print(i)

for k, v in graph.items():
    print(k, v)


def walk_to_neighbors(path):
    result = []
    node_xy = path["node"]
    previous_nodes = path["previous_nodes"]

    for possible_edge in graph[str(node_xy)]:
        next_node = list(edges[possible_edge]["end_nodes"] - {node_xy})[0]
        if next_node not in previous_nodes:
            result.append({
                "node": next_node,
                "previous_nodes": previous_nodes + [next_node],
                "total_costs": path["total_costs"] + edges[possible_edge]["costs"]
            })
    return result


start = {
    "node": (x_start, y_start),
    "previous_nodes": [(x_start, y_start)],
    "total_costs": 0
}
exploration = walk_to_neighbors(start)

longest_paths = [0]
while len(exploration) > 0:
    exploration = sorted(exploration, key=lambda x: (x['total_costs'], x['node']))
    index_min = 0
    next_to_explore = exploration[index_min]
    # print(next_to_explore)

    # found a possible longest path to end-node if that is the next to explore!
    if next_to_explore["node"] == (x_end, y_end):
        if -next_to_explore["total_costs"] > max(longest_paths):
            print("longest path find so far has length", -next_to_explore["total_costs"])
            print(next_to_explore)
            print("explorations left", len(exploration))
            longest_paths.append(-next_to_explore["total_costs"])
        exploration.pop(index_min)
        continue

    exploration.pop(index_min)
    exploration += walk_to_neighbors(next_to_explore)

print("the DEFINITIVE longest path has length", max(longest_paths))
