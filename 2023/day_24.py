from aocd import get_data, submit
from sympy import *
from sympy.solvers.solveset import nonlinsolve

year, day = 2023, 24

# parse data
data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
data = get_data(year=year, day=day)

# config
x_min, x_max = 200000000000000, 400000000000000
y_min, y_max = x_min, x_max

stones = []
for line in data.split("\n"):
    px, py, pz = line.split(" @ ")[0].split(", ")
    vx, vy, vz = line.split(" @ ")[1].split(", ")
    stones.append([[int(px), int(py), int(pz)], [int(vx), int(vy), int(vz)]])

# part A
intersections_in_test_area = 0
for i in range(0, len(stones) - 1):
    for j in range(i + 1, len(stones)):
        print(stones[i], stones[j])
        vector1 = stones[i][1][:2]
        vector2 = [-v for v in stones[j][1]][:2]
        vector3 = [stones[j][0][v] - stones[i][0][v] for v in range(3)][:2]
        m = Matrix([vector1, vector2, vector3]).transpose()
        m_red = m.rref()[0].values()
        if len(m_red) < 4:
            print("no intersection!")
            continue

        t1 = m_red[1]
        t2 = m_red[3]
        print(t1, t2)
        if t1 >= 0 and t2 >= 0:
            x = stones[i][0][0] + t1 * stones[i][1][0]
            y = stones[i][0][1] + t1 * stones[i][1][1]
            print(float(x), float(y))
            if (x_min <= x <= x_max) and (y_min <= y <= y_max):
                intersections_in_test_area += 1
print("intersections is", intersections_in_test_area)
# submit(intersections_in_test_area, part="a", day=day, year=year)

# part B
px1, py1, pz1 = stones[0][0]
vx1, vy1, vz1 = stones[0][1]
px2, py2, pz2 = stones[1][0]
vx2, vy2, vz2 = stones[1][1]
px3, py3, pz3 = stones[2][0]
vx3, vy3, vz3 = stones[2][1]

u, v, w, a, b, c, d, e, f = symbols('u, v, w, a, b, c, d, e, f')
sol = nonlinsolve(
    [
        px1 + u*vx1 - a - u*d,
        py1 + u*vy1 - b - u*e,
        pz1 + u*vz1 - c - u*f,
        px2 + v*vx2 - a - v*d,
        py2 + v*vy2 - b - v*e,
        pz2 + v*vz2 - c - v*f,
        px3 + w*vx3 - a - w*d,
        py3 + w*vy3 - b - w*e,
        pz3 + w*vz3 - c - w*f
    ],
    (u, v, w, a, b, c, d, e, f)
)
print(sol)
answer_b = sum([200027938836082, 127127087242193, 219339468239370])
print(answer_b)
# submit(answer_b, part="b", day=day, year=year)
