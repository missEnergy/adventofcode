from aocd import get_data, submit

year, day = 2023, 13

# parse data
data = get_data(year=year, day=day).split("\n\n")


def find_reflection_line(pattern, old_score=0):
    score = 0

    # find vertical line
    for i in range(1, len(pattern[0])):
        no_mirror = False
        for line in pattern:
            left = line[:i][::-1]
            right = line[i:]
            if len(left) <= len(right):
                right = right[:len(left)]
            else:
                left = left[:len(right)]
            if left != right:
                no_mirror = True
                break
        if not no_mirror:
            if i != old_score:
                score += i
                break

    pattern_on_side = []
    for idx in range(len(pattern[0])):
        column = ""
        for idy in range(len(pattern)):
            column += pattern[idy][len(pattern[0]) - idx - 1]
        pattern_on_side.append(column)

    # find horizontal line
    for i in range(1, len(pattern_on_side[0])):
        no_mirror = False
        for line in pattern_on_side:
            left = line[:i][::-1]
            right = line[i:]
            if len(left) <= len(right):
                right = right[:len(left)]
            else:
                left = left[:len(right)]
            if left != right:
                no_mirror = True
                break
        if not no_mirror:
            if 100*i != old_score:
                score += 100*i
                break
    return score


# part A
total = 0
for pattern in data:
    pattern = pattern.split('\n')
    total += find_reflection_line(pattern)
print(total)
# submit(total, part="a", day=day, year=year)

# part B
import copy
total = 0
for pattern in data:
    pattern = pattern.split('\n')
    old_reflection_score = find_reflection_line(pattern)
    double_break = False
    for idy, line in enumerate(pattern):
        for idx, c in enumerate(line):
            if c == ".":
                d = "#"
            else:
                d = "."
            new_pattern = copy.deepcopy(pattern)
            new_pattern[idy] = new_pattern[idy][:idx] + d + new_pattern[idy][idx+1:]
            new_score = find_reflection_line(new_pattern, old_reflection_score)
            total += new_score
            if new_score != 0:
                double_break = True
                break
        if double_break:
            break
print(total)
# submit(total, part="b", day=day, year=year)
