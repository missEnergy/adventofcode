from csv import reader

score = 0
with open("advent4.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        range0 = [int(i) for i in row[0].split("-")]
        range1 = [int(i) for i in row[1].split("-")]

        if range0[0] >= range1[0] and range0[1] <= range1[1]:
            score = score + 1
        elif range0[0] <= range1[0] and range0[1] >= range1[1]:
            score = score + 1

print(score)
