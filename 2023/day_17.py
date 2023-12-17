import math

from aocd import get_data, submit
import copy

year, day = 2023, 17

# parse data
grid = []
data = get_data(year=year, day=day)
for line in data.split("\n"):
    grid.append([int(i) for i in list(line)])

# config PART A
threshold = 10
directions = {
    "1N": [[0, -1]],
    "1S": [[0, 1]],
    "1E": [[1, 0]],
    "1W": [[-1, 0]],
    "2N": [[0, -1], [0, -1]],
    "2S": [[0, 1], [0, 1]],
    "2E": [[1, 0], [1, 0]],
    "2W": [[-1, 0], [-1, 0]],
    "3N": [[0, -1], [0, -1], [0, -1]],
    "3S": [[0, 1], [0, 1], [0, 1]],
    "3E": [[1, 0], [1, 0], [1, 0]],
    "3W": [[-1, 0], [-1, 0], [-1, 0]],
}

# config PART B
threshold = 20
directions = {  # slightly limited possible solutions by not considering 7 - 10 steps to N or W
    "4N": [[0, -1] for i in range(4)],
    "4S": [[0, 1] for i in range(4)],
    "4E": [[1, 0] for i in range(4)],
    "4W": [[-1, 0] for i in range(4)],
    "5N": [[0, -1] for i in range(5)],
    "5S": [[0, 1] for i in range(5)],
    "5E": [[1, 0] for i in range(5)],
    "5W": [[-1, 0] for i in range(5)],
    "6N": [[0, -1] for i in range(6)],
    "6S": [[0, 1] for i in range(6)],
    "6E": [[1, 0] for i in range(6)],
    "6W": [[-1, 0] for i in range(6)],
    "7S": [[0, 1] for i in range(7)],
    "7E": [[1, 0] for i in range(7)],
    "8S": [[0, 1] for i in range(8)],
    "8E": [[1, 0] for i in range(8)],
    "9S": [[0, 1] for i in range(9)],
    "9E": [[1, 0] for i in range(9)],
    "0S": [[0, 1] for i in range(10)],
    "0E": [[1, 0] for i in range(10)],
}

# START algorithm
cheapest_path_found = [[math.inf for i in range(len(grid[0]))] for j in range(len(grid))]


def walk_to_neighbors(node):
    if node["total_costs"] >= cheapest_path_found[node["node"][1]][node["node"][0]] + threshold:
        return []
    result = []

    if node["direction"] is None:
        possible_directions = directions.keys()
    else:
        possible_directions = [i for i in directions.keys() if node["direction"][1] not in i]

    previous_nodes = node["previous_nodes"]

    for d in possible_directions:
        neighbors = []
        current_x = node["node"][0]
        current_y = node["node"][1]
        for i in directions[d]:
            current_x += i[0]
            current_y += i[1]
            neighbors.append([
                current_x,
                current_y
            ])

        # can't consider node if already in previous node path
        # this also takes care of not going backwards
        continue_flag = False
        for i in neighbors:
            if i in previous_nodes:
                continue_flag = True
        if continue_flag:
            continue

        # can only consider node if still on grid
        if 0 <= neighbors[-1][0] < len(grid[0]) and 0 <= neighbors[-1][1] < len(grid):
            new_costs = 0
            new_previous_nodes = copy.deepcopy(previous_nodes)
            for i in neighbors:
                new_costs += grid[i[1]][i[0]]
                new_previous_nodes.append(i)
            new_total_costs = node["total_costs"] + new_costs

            if new_total_costs < cheapest_path_found[neighbors[-1][1]][neighbors[-1][0]]:
                cheapest_path_found[neighbors[-1][1]][neighbors[-1][0]] = new_total_costs

            if new_total_costs < cheapest_path_found[neighbors[-1][1]][neighbors[-1][0]] + threshold:
                result.append({
                    "node": neighbors[-1],
                    "direction": "X" + d[1],
                    "costs": new_costs,
                    "total_costs": new_total_costs,
                    "previous_nodes": new_previous_nodes
                })
    return result


start = {
    "node": [0, 0],
    "direction": None,
    "costs": 0,
    "total_costs": 0,
    "previous_nodes": [[0, 0]]
}
exploration = walk_to_neighbors(start)

while True:
    exploration = sorted(exploration, key=lambda x: (x['total_costs'], x['node']))
    index_min = 0
    next_to_explore = exploration[index_min]
    print(next_to_explore)

    # found the shortest path to end-node if that is the next to explore!
    if next_to_explore["node"] == [len(grid[0]) - 1, len(grid) - 1]:
        break

    exploration.pop(index_min)
    new_exploration = walk_to_neighbors(next_to_explore)

    for i in new_exploration:
        # replace explorations to an already known node if a cheaper path is found
        if [i["node"], i["direction"]] in [[n['node'], n['direction']] for n in exploration]:
            index_i = [[n['node'], n['direction']] for n in exploration].index([i["node"], i["direction"]])
            if i["total_costs"] <= exploration[index_i]["total_costs"]:
                exploration[index_i] = i
        else:
            exploration.append(i)

nodes = [n['node'] for n in exploration]
index_end = nodes.index([len(grid[0]) - 1, len(grid) - 1])

print("done!")
print(exploration[index_end])
print(exploration[index_end]["total_costs"])
vis = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
for i in exploration[index_end]["previous_nodes"]:
    vis[i[1]][i[0]] = grid[i[1]][i[0]]
for i in vis:
    print(i)
