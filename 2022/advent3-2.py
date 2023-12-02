from csv import reader

score = 0
position = 1
with open("advent3.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        string = row[0]
        if position == 1:
            first = row[0]
            position = 2
        elif position == 2:
            second = row[0]
            position = 3
        elif position == 3:
            third = row[0]
            letter = list(set(first).intersection(second).intersection(third))[0]
            if letter.isupper():
                score = score + 26
            score = score + (ord(letter) & 31)
            position = 1
print(score)
