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


def walk_to_neighbors(node):
    result = []
    node_xy = node["node"]
    previous_nodes = node["previous_nodes"]

    # follow the slope
    if grid[node_xy[1]][node_xy[0]] in directions.keys():
        possible_directions = dict()
        possible_directions[grid[node_xy[1]][node_xy[0]]] = directions[grid[node_xy[1]][node_xy[0]]]
    # or move to anywhere you want
    else:
        possible_directions = directions

    for k, v in possible_directions.items():
        current_x = node_xy[0] + v[0]
        current_y = node_xy[1] + v[1]
        # it should not be outside the grid
        if 0 <= current_x < len(grid[0]) and 0 <= current_y < len(grid):
            # it should be on a possible tile
            if grid[current_y][current_x] in [".", k]:
                # it should be on a non-visited tile
                if (current_x, current_y) not in previous_nodes:
                    result.append({
                        "node": (current_x, current_y),
                        "previous_nodes": node["previous_nodes"] + [(current_x, current_y)]
                    })
    return result


start = {
    "node": (x_start, y_start),
    "previous_nodes": [(x_start, y_start)]
}
exploration = walk_to_neighbors(start)

longest_paths = []
while len(exploration) > 0:
    exploration = sorted(exploration, key=lambda x: (-len(x['previous_nodes']), x['node']))
    index_min = 0
    next_to_explore = exploration[index_min]

    # found a possible longest path to end-node if that is the next to explore!
    if next_to_explore["node"] == (x_end, y_end):
        nodes = [n['node'] for n in exploration]
        index_end = nodes.index((x_end, y_end))
        print(exploration[index_end])
        print(len(exploration[index_end]["previous_nodes"]) - 1)
        longest_paths.append(len(exploration[index_end]["previous_nodes"]) - 1)

    exploration.pop(index_min)
    new_exploration = walk_to_neighbors(next_to_explore)

    for i in new_exploration:
        exploration.append(i)

print("the longest path has length", max(longest_paths))
