from aocd import get_data, submit
import matplotlib.pyplot as plt

year = 2024
day = 14

data = get_data(year=year, day=day)
wide = 101
tall = 103

# PART A
sec = 100
robots = []
lines = data.splitlines()
for line in lines:
    p, v = line.split(" ")
    px, py = map(int, p[2:].split(","))
    vx, vy = map(int, v[2:].split(","))
    robots.append(((px + sec*vx)%wide, (py + sec*vy)%tall))

left_up_quadrant = len([r for r in robots if r[0] < wide//2 and r[1] < tall//2])
left_down_quadrant = len([r for r in robots if r[0] < wide//2 and r[1] > tall//2])
right_up_quadrant = len([r for r in robots if r[0] > wide//2 and r[1] < tall//2])
right_down_quadrant = len([r for r in robots if r[0] > wide//2 and r[1] > tall//2])

answer = left_up_quadrant * left_down_quadrant * right_up_quadrant * right_down_quadrant
print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
# there are 500 robots, so max 500 grid_positions
robots = []
lines = data.splitlines()
for line in lines:
    p, v = line.split(" ")
    px, py = map(int, p[2:].split(","))
    vx, vy = map(int, v[2:].split(","))
    robots.append({"p": (px, py), "v": (vx, vy)})

sec = 5200 # 5200 is too low (answer tried)
while sec < 7800: # 7800 is too high (answer tried)
    sec += 1
    grid_positions = set()
    for r in robots:
        gp = ((r["p"][0] + sec*r["v"][0])%wide, (r["p"][1] + sec*r["v"][1])%tall)
        grid_positions.add((gp[0], gp[1]))

    if len([c for c in grid_positions if c[0] == 35 or c[0] == 65]) > 60:
        # grid_positions = [c for c in grid_positions if c[0] > 35 and c[0] < 65]
        plt.scatter(*zip(*grid_positions), color='green')
        plt.title(f"sec: {sec}, grid_positions: {len(grid_positions)}")
        plt.xlim(0, wide)
        plt.show()
