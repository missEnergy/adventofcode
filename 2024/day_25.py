from aocd import get_data, submit

year = 2024
day = 25

data = get_data(year=year, day=day)
keys_and_locks = data.split('\n\n')

keys = []
locks = []
for i in keys_and_locks:
    rows = i.splitlines()
    new = []
    for j in range(5):
        count = 0
        for k in range(1, 6):
            if rows[k][j] == '#':
                count += 1
        new.append(count)

    if rows[0] == '#####': # lock
        locks.append(new)
    elif rows[0] == '.....': # key    
        keys.append(new)

# PART A
fits = 0
for lock in locks:
    for key in keys:
        all_fits = True
        for i in range(5):
            if lock[i] + key[i] > 5:
                all_fits = False
                break
        if all_fits:
            fits += 1

print(fits)
# submit(fits, part="a", day=day, year=year)