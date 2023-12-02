from aocd import get_data, submit

year, day = 2023, 2

# parse data
data = get_data(year=year, day=day).split("\n")
all_games = []
for line in data:
    game_id, games_data = line.split(':')[0].split(' ')[1], line.split(': ')[1].split('; ')
    games = []
    for game_str in games_data:
        game = {"red": 0, "blue": 0, "green": 0}
        for item in game_str.split(', '):
            amount, color = item.split(' ')
            game[color] = int(amount)
        games.append(game)
    all_games.append({"id": game_id, "games": games})

print(all_games)

# part A
answer_a = 0
for i in all_games:
    game_id = int(i["id"])
    for j in i["games"]:
        if (j['red'] > 12) or (j['green'] > 13) or (j['blue'] > 14):
            game_id = 0
    answer_a = answer_a + game_id

print(answer_a)
# submit(answer_a, part="a", day=day, year=year)

# part B
answer_b = 0
for i in all_games:
    min_red, min_green, min_blue = 0, 0, 0
    for j in i["games"]:
        if j['red'] > min_red:
            min_red = j['red']
        if j['green'] > min_green:
            min_green = j['green']
        if j['blue'] > min_blue:
            min_blue = j['blue']
    power = min_red * min_blue * min_green
    answer_b = answer_b + power

print(answer_b)
# submit(answer_b, part="b", day=day, year=year)