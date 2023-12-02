from csv import reader

total_score = 0
with open("advent2.csv", "r") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj, delimiter=" ")
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        print(row)
        # row[0]  # A for Rock, B for Paper, and C for Scissors
        # row[1]  # X means you need to lose,
        # Y means you need to end the round in a draw,
        # and Z means you need to win.

        if row[1] == "X":
            total_score = total_score + 0
        elif row[1] == "Y":
            total_score = total_score + 3
        elif row[1] == "Z":
            total_score = total_score + 6

        if row[0] == "A":
            if row[1] == "X":
                total_score = total_score + 3
            elif row[1] == "Y":
                total_score = total_score + 1
            elif row[1] == "Z":
                total_score = total_score + 2
        elif row[0] == "B":
            if row[1] == "X":
                total_score = total_score + 1
            elif row[1] == "Y":
                total_score = total_score + 2
            elif row[1] == "Z":
                total_score = total_score + 3
        elif row[0] == "C":
            if row[1] == "X":
                total_score = total_score + 2
            elif row[1] == "Y":
                total_score = total_score + 3
            elif row[1] == "Z":
                total_score = total_score + 1


print(total_score)
