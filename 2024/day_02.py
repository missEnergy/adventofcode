from aocd import get_data, submit

year = 2024
day = 2

data = get_data(year=year, day=day)
lines = data.splitlines()

input = []
for line in lines:
    input.append([int(i) for i in line.split()])

def is_safe_report(line):
    print(line)
    res = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    print(res)
    if (len([i for i in res if i == 0]) > 0):
        return False
    if (len([i for i in res if abs(i) > 3]) > 0):
        return False
    if (len([i for i in res if i > 0]) == len(res)):
        return True
    if (len([i for i in res if i > 0]) == 0):
        return True
    return False

# PART A
safe_reports = 0
for line in input:
    if is_safe_report(line):
        safe_reports += 1
print(safe_reports)
submit(safe_reports, part="a", day=day, year=year)

# PART B
safe_reports = 0
for line in input:
    if is_save_report(line):
        safe_reports += 1
        print("safe report!")
    else:
        for i in range(len(line)):
            if is_save_report(line[:i] + line[i+1:]):
                safe_reports += 1
                print("safe report!")
                break
print(safe_reports)
submit(safe_reports, part="b", day=day, year=year)