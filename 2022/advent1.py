from csv import reader

# open file in read mode
elves = []
position = 0
elves.append(0)
with open("advent1.csv", "r") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        try:
            elves[position] = elves[position] + int(row[0])
        except:
            print("calories complete")
            print(elves[position])
            print("next elf!")
            position = position + 1
            elves.append(0)

print("max calories is")
print(max(elves))
elves = sorted(elves)
print(elves)
print(elves[-1] + elves[-2] + elves[-3])
