from csv import reader

stacks = {}
position = 1
with open("advent5-2.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        stacks[str(position)] = row[0]
        position = position + 1

with open("advent5.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        _, size, _, start, _, end = row[0].split(" ")
        stacks[end] = stacks[end] + stacks[start][-int(size):] #[::-1] #switch this on for first solution
        stacks[start] = stacks[start][:(len(stacks[start]) - int(size))]

print(stacks)
