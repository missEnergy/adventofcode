from csv import reader

score = 0
with open("advent3.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        string = row[0]
        firstpart, secondpart = string[: len(string) // 2], string[len(string) // 2 :]
        letter = list(set(firstpart).intersection(secondpart))[0]
        if letter.isupper():
            score = score + 26
        score = score + (ord(letter) & 31)
print(score)
