from aocd import get_data, submit

year = 2024
day = 1

data = get_data(year=year, day=day)
lines = data.split("\n")

array_a = []
array_b = []
for line in lines:
    a, b = line.split()
    array_a.append(int(a))
    array_b.append(int(b))

# PART A
# array_a = sorted(array_a)
# array_b = sorted(array_b)
#
# answer = 0
# for i in range(len(array_a)):
#     answer += abs(array_a[i]-array_b[i])
#
# print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
answer = 0
for i in range(len(array_a)):
    answer += array_a[i]*len([x for x in array_b if x == array_a[i]])
print(answer)
submit(answer, part="b", day=day, year=year)

