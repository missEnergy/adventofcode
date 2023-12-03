from aocd import get_data, submit
import re

numbers_regex = r'[0-9]'

year, day = 2023, 3

# part A
data = get_data(year=year, day=day) #
matrix_symbol = re.sub(numbers_regex, ' ', data).replace(".", " ").split("\n")
matrix_all = data.split("\n")

matrix_length = len(matrix_all)
matrix_width = len(matrix_all[0])

matrix_count_number = []
for i in range(matrix_length):
    new_row = []
    for j in range(matrix_width):
        new_row.append(False)
    matrix_count_number.append(new_row)

for idy, row in enumerate(matrix_symbol):
    for idx, entry in enumerate(row):
        if entry != " ":
            # print(f"there is a symbol {entry} on position ({idx}, {idy})")
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if re.match(numbers_regex, matrix_all[idy+y][idx+x]):
                        matrix_count_number[idy+y][idx+x] = True

for idy, row in enumerate(matrix_count_number):
    for idx, entry in enumerate(row):
        if entry:
            for x in [-1, 1]:
                try:
                    if re.match(numbers_regex, matrix_all[idy][idx+x]):
                        matrix_count_number[idy][idx + x] = True
                        if re.match(numbers_regex, matrix_all[idy][idx+x+x]):
                            matrix_count_number[idy][idx + x + x] = True
                except:
                    print("out of range")

for idy, row in enumerate(matrix_count_number):
    for idx, entry in enumerate(row):
        if not entry:
            matrix_all[idy] = matrix_all[idy][:idx] + " " + matrix_all[idy][idx+1:]

answer_a = 0
for row in matrix_all:
    row_array = row.split(" ")
    for entry in row_array:
        if entry != '':
            answer_a = answer_a + int(entry)

print(answer_a)
# submit(answer_a, part="a", day=day, year=year)

# part B
data = get_data(year=year, day=day)
matrix_symbol = re.sub(numbers_regex, ' ', data).replace(".", " ").split("\n")
matrix_all = data.split("\n")

matrix_length = len(matrix_all)
matrix_width = len(matrix_all[0])

matrix_count_number = []
for i in range(matrix_length):
    new_row = []
    for j in range(matrix_width):
        new_row.append(False)
    matrix_count_number.append(new_row)

star_pairs = []
for idy, row in enumerate(matrix_symbol):
    for idx, entry in enumerate(row):
        if entry == "*":
            count_adjacent = 0
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if re.match(numbers_regex, matrix_all[idy + y][idx + x]):
                        count_adjacent = count_adjacent + 1
                        if x == -1 and re.match(numbers_regex, matrix_all[idy + y][idx]):
                            break
                        elif x == 0 and re.match(numbers_regex, matrix_all[idy + y][idx + 1]):
                            break
            if count_adjacent == 2:
                pair = []
                for y in [-1, 0, 1]:
                    for x in [-1, 0, 1]:
                        if re.match(numbers_regex, matrix_all[idy + y][idx + x]):
                            pair.append([idy + y, idx + x])
                            matrix_count_number[idy + y][idx + x] = True
                            if x == -1 and re.match(numbers_regex, matrix_all[idy + y][idx]):
                                break
                            elif x == 0 and re.match(numbers_regex, matrix_all[idy + y][idx + 1]):
                                break
                star_pairs.append(pair)

for idy, row in enumerate(matrix_count_number):
    for idx, entry in enumerate(row):
        if entry:
            for x in [-1, 1]:
                try:
                    if re.match(numbers_regex, matrix_all[idy][idx + x]):
                        matrix_count_number[idy][idx + x] = True
                        if re.match(numbers_regex, matrix_all[idy][idx + x + x]):
                            matrix_count_number[idy][idx + x + x] = True
                except:
                    print("out of range")

for idy, row in enumerate(matrix_count_number):
    for idx, entry in enumerate(row):
        if not entry:
            matrix_all[idy] = matrix_all[idy][:idx] + " " + matrix_all[idy][idx + 1:]

answer_b = 0
for pair in star_pairs:
    gear_ratio = 1
    for c in pair:
        number_str = matrix_all[c[0]][c[1]-2:c[1]+3]
        if number_str[1] == ' ':
            number_str = number_str[2:]
            if number_str[1] == ' ':
                number_str = number_str[0]
            elif number_str[2] == ' ':
                number_str = number_str[:2]
        elif number_str[3] == ' ':
            number_str = number_str[:3]
            if number_str[1] == ' ':
                number_str = number_str[2]
            elif number_str[0] == ' ':
                number_str = number_str[1:]
        else:
            number_str = number_str[1:4]
        gear_ratio = gear_ratio * int(number_str)

    answer_b = answer_b + gear_ratio

print(answer_b)
submit(answer_b, part="b", day=day, year=year)