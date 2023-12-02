from csv import reader

trees = []
with open("advent8.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        trees.append([int(i) for i in row[0]])
print(trees)

trees_T = [list(i) for i in zip(*trees)]
print(trees_T)

visible_tree_grid = []
for i in range(len(trees)):
    visible_tree_grid.append([])
    for j in range(len(trees[i])):
        visible_tree_grid[i].append(0)
print(visible_tree_grid)

for i in range(len(trees)):
    highest = -1
    for j in range(len(trees[i])):
        if trees[i][j] > highest:
            visible_tree_grid[i][j] = 1
            highest = trees[i][j]

for i in range(len(trees)):
    highest = -1
    for j in range(len(trees[i])):
        if trees[i][-1-j] > highest:
            visible_tree_grid[i][-1-j] = 1
            highest = trees[i][-1-j]

for i in range(len(trees_T)):
    highest = -1
    for j in range(len(trees_T[i])):
        if trees_T[i][j] > highest:
            visible_tree_grid[j][i] = 1
            highest = trees_T[i][j]

for i in range(len(trees_T)):
    highest = -1
    for j in range(len(trees_T[i])):
        if trees_T[i][-1-j] > highest:
            visible_tree_grid[-1-j][i] = 1
            highest = trees_T[i][-1-j]

print(visible_tree_grid)
total_visible = 0
for lane in visible_tree_grid:
    for tree in lane:
        total_visible = total_visible + tree

print(total_visible)
# EPIC FAIL