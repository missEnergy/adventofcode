from aocd import get_data, submit
from sympy import solve
from sympy.abc import a, b

year = 2024
day = 13

data = get_data(year=year, day=day)
machines = data.split('\n\n')

answer = 0
for d in machines:
    ax = int(d.splitlines()[0].split(': X+')[1].split(',')[0])
    ay = int(d.splitlines()[0].split(', Y+')[1])
    bx = int(d.splitlines()[1].split(': X+')[1].split(',')[0])
    by = int(d.splitlines()[1].split(', Y+')[1])

    # PART A
    # px = int(d.splitlines()[2].split('X=')[1].split(',')[0])
    # py = int(d.splitlines()[2].split('Y=')[1])

    # PART B
    px = int(d.splitlines()[2].split('X=')[1].split(',')[0]) + 10000000000000
    py = int(d.splitlines()[2].split('Y=')[1]) + 10000000000000

    solutions = solve([ax*a + bx*b - px, ay*a + by*b - py], [a, b], dict=True)
    assert len(solutions) == 1

    if '/' in str(solutions[0][a]) or '/' in str(solutions[0][b]):
        print('no int solution')
        continue
    print('int solution')
    answer += 3*int(solutions[0][a]) + int(solutions[0][b])

print(answer)
# submit(answer, part="a", day=day, year=year)
submit(answer, part="b", day=day, year=year)
