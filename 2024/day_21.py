from aocd import get_data, submit

year = 2024
day = 21

data = get_data(year=year, day=day)
lines = data.splitlines()

for line in lines:
    print(line)

# PART A
# submit(answer, part="a", day=day, year=year)
# PART B
# submit(answer, part="b", day=day, year=year)