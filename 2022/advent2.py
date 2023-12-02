from csv import reader

total_score = 0
with open("advent2.csv", "r") as read_obj:
    csv_reader = reader(read_obj, delimiter=" ")
    for row in csv_reader:
        print(row)
        # row[0]  # A for Rock, B for Paper, and C for Scissors
        # row[1]  # X for Rock, Y for Paper, and Z for Scissors

        if row[1] == "X":
            total_score = total_score + 1
        elif row[1] == "Y":
            total_score = total_score + 2
        elif row[1] == "Z":
            total_score = total_score + 3

        if row[0] == "A":
            if row[1] == "X":
                total_score = total_score + 3
            elif row[1] == "Y":
                total_score = total_score + 6
            elif row[1] == "Z":
                total_score = total_score + 0
        elif row[0] == "B":
            if row[1] == "X":
                total_score = total_score + 0
            elif row[1] == "Y":
                total_score = total_score + 3
            elif row[1] == "Z":
                total_score = total_score + 6
        elif row[0] == "C":
            if row[1] == "X":
                total_score = total_score + 6
            elif row[1] == "Y":
                total_score = total_score + 0
            elif row[1] == "Z":
                total_score = total_score + 3


print(total_score)
