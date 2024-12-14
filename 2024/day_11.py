from aocd import get_data, submit

year = 2024
day = 11

data = "125 17"
data = get_data(year=year, day=day)
stones = data.split()
print(stones)

# PART A
blinks = 25
for i in range(blinks):
    new_stones = []
    for s in stones:
        if s == '0':
            new_stones.append('1')
        elif len(s)%2 == 0:
            new_stones.append(str(int(s[:(len(s)//2)])))
            new_stones.append(str(int(s[(len(s)//2):])))
        else:
            new_stones.append(str(int(s)*2024))
    stones = new_stones
answer = len(stones)
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
blinks = 75
stone_dict = dict()
for s in stones:
    if s not in stone_dict:
        stone_dict[s] = 1
    else:
        stone_dict[s] += 1

for i in range(blinks):
    new_stone_dict = dict()
    for s in stone_dict.keys():
        if s == '0':
            if '1' not in new_stone_dict:
                new_stone_dict['1'] = stone_dict[s]
            else:
                print(new_stone_dict)
                new_stone_dict['1'] += stone_dict[s]

        elif len(s)%2 == 0:
            if str(int(s[:(len(s)//2)])) not in new_stone_dict:
                new_stone_dict[str(int(s[:(len(s)//2)]))] = stone_dict[s]
            else:
                new_stone_dict[str(int(s[:(len(s)//2)]))] += stone_dict[s]
            if str(int(s[(len(s)//2):])) not in new_stone_dict:
                new_stone_dict[str(int(s[(len(s)//2):]))] = stone_dict[s]
            else:
                new_stone_dict[str(int(s[(len(s)//2):]))] += stone_dict[s]
        else:
            if str(int(s)*2024) not in new_stone_dict:
                new_stone_dict[str(int(s)*2024)] = stone_dict[s]
            else:
                new_stone_dict[str(int(s)*2024)] += stone_dict[s]
    stone_dict = new_stone_dict
answer = sum(stone_dict.values())
# submit(answer, part="b", day=day, year=year)