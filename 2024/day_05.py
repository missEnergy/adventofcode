from aocd import get_data, submit

year = 2024
day = 5

data = get_data(year=year, day=day)
rules, updates_raw = data.split("\n\n")
rules = rules.splitlines()

updates = []
for update in updates_raw.splitlines():
    updates.append(list(map(int, update.split(","))))

# assumption, page < 100
rule_book = [{"before": set(), "after": set()} for i in range(100)]

for rule in rules:
    before, after = map(int, rule.split("|"))
    rule_book[before]["before"].add(after)
    rule_book[after]["after"].add(before)

for rule_book_page in rule_book:
    print(rule_book_page)

# PART A
incorrect_updates = []
answer_a = 0
for update in updates:
    print(update)
    valid = True
    for i in range(len(update) - 1):
        if not set(update[i+1:]).issubset(rule_book[update[i]]['before']):
            valid = False
            break
    if valid:
        print("valid")
        answer_a += update[int((len(update) - 1)/2)]
    else:
        incorrect_updates.append(update)
# submit(answer_a, part="a", day=day, year=year)

# PART B
answer_b = 0
for update in incorrect_updates:
    print(update)
    correct_update = []
    for page in update:
        insert_at = 0
        for cu in correct_update:
            if page in rule_book[cu]["before"]:
                insert_at += 1
            else:
                break
        correct_update.insert(insert_at, page)
    print(correct_update)
    answer_b += correct_update[int((len(correct_update) - 1) / 2)]
print(answer_b)
# submit(answer_b, part="b", day=day, year=year)