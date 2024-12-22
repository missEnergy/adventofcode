year = 2024
day = 17

# PART A
A = 64854237
B = 0
C = 0

while True:
    B = A % 8
    B = B ^ 1
    C = int(A/(pow(2,B)))
    B = B ^ 5
    B = B ^ C
    print(f"{B%8},", end='') # OUT
    A = int(A/(pow(2,3)))
    if A == 0:
        print('done')
        break

# PART B
ref = "2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0,"
init = 164279024967600 # update the init when you find partial match and refine from there
while True:
    print(init)
    A = init
    B = 0
    C = 0
    out = ''
    while True:
        B = A % 8
        B = B ^ 1
        C = int(A/(pow(2,B)))
        B = B ^ 5
        B = B ^ C
        out += f"{B%8},"
        A = int(A/(pow(2,3)))
        if A == 0:
            break
        if len(out) >= len(ref):
            break
    if out[0:] == ref[0:]: # start with looking for only end of seq match, and then make larger
        print('done!')
        print(f"ref: {ref}")
        print(f"out: {out}")
        break
    init += 1 # start with bigger steps (e.g. 1000000000)
    print(f"ref: {ref}")
    print(f"out: {out}")
