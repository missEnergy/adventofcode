from csv import reader

trees = []
with open("advent8.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        trees.append([int(i) for i in row[0]])
print(trees)

trees_T = [list(i) for i in zip(*trees)]
print(trees_T)

scenic_scores = []
for i in range(len(trees)):
    scenic_scores.append([])
    for j in range(len(trees[i])):
        scenic_scores[i].append(0)

for i in range(len(scenic_scores)):
    for j in range(len(scenic_scores[i])):
        if i == 0 or j == 0 or i == len(scenic_scores) - 1 or j == len(scenic_scores[i]) - 1:
            scenic_scores[i][j] = 0
        else:


for i in range(len(trees)):
    highest = -1
    for j in range(len(trees[i])):
        if trees[i][j] > highest:
            visible_tree_grid[i][j] = 1
            highest = trees[i][j]

for i in range(len(trees)):
    highest = -1
    for j in range(len(trees[i])):
        if trees[i][-1 - j] > highest:
            visible_tree_grid[i][-1 - j] = 1
            highest = trees[i][-1 - j]

for i in range(len(trees_T)):
    highest = -1
    for j in range(len(trees_T[i])):
        if trees_T[i][j] > highest:
            visible_tree_grid[j][i] = 1
            highest = trees_T[i][j]

for i in range(len(trees_T)):
    highest = -1
    for j in range(len(trees_T[i])):
        if trees_T[i][-1 - j] > highest:
            visible_tree_grid[-1 - j][i] = 1
            highest = trees_T[i][-1 - j]
