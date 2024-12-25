from aocd import get_data, submit
from itertools import combinations

year = 2024
day = 24

data = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
data = get_data(year=year, day=day)
inits, logics = data.split('\n\n')

key_values = {}
init_keys = set()
for i in inits.splitlines():
    key, value = i.split(': ')
    key_values[key] = int(value)
    init_keys.add(key)

key_logics = {}
for i in logics.splitlines():
    left, ops, right, arrow, result = i.split(' ')
    key_logics[result] = {"inputs": [left, right], "ops": ops}
    if result not in key_values:
        key_values[result] = None

while None in key_values.values():
    for key, value in key_values.items():
        if value is not None:
            continue
        logic = key_logics[key]
        left = key_values[logic["inputs"][0]]
        right = key_values[logic["inputs"][1]]
        if left is not None and right is not None:
            if logic["ops"] == 'AND':
                key_values[key] = left & right
            elif logic["ops"] == 'OR':
                key_values[key] = left | right
            elif logic["ops"] == 'XOR':
                key_values[key] = left ^ right

key_values_sorted = sorted(key_values.items(), key=lambda x: x[0])

binary_x = ''
binary_y = ''
binary_z = ''
for key, value in key_values_sorted:
    if key[0] == 'x' and int(key[1:]) >= 0:
        binary_x += str(value)
    if key[0] == 'y' and int(key[1:]) >= 0:
        binary_y += str(value)
    if key[0] == 'z' and int(key[1:]) >= 0:
        binary_z += str(value)
binary_x = binary_x[::-1]
binary_y = binary_y[::-1]
binary_z = binary_z[::-1]

# PART A
print(int(binary_z, 2))

# PART B
x = int(binary_x, 2)
y = int(binary_y, 2)
z = int(binary_z, 2)
print(' ' + binary_x)
print(' ' + binary_y)
print(binary_z)
target_binary_z = "{0:b}".format(x + y)
print(target_binary_z)
for i in range(len(binary_z)):
    if binary_z[i] != target_binary_z[i]:
        print(len(binary_z) - 1 - i, f'should be {target_binary_z[i]}')
        

# 41 should be 1 --> vnn XOR gnj
# 40 should be 0 --> hkg XOR rrb
# 39 should be 0 --> vtd XOR rfr
# 38 should be 0 --> bfm XOR jnw
# 37 should be 0 --> ncc XOR cqs
# 36 should be 0 --> mbw XOR kth
# 35 should be 0 --> qnm AND rfk 
# 19 should be 1 --> dmn XOR dsj
# 18 should be 0 --> khk OR stg
# 11 should be 0 --> cbj XOR csm
# 8 should be 0 --> rkw XOR whp 
# 7 should be 1 --> y07 AND x07 0 and 1 = 0


# binary_x = binary_x[::-1]
# binary_y = binary_y[::-1]
# binary_z = binary_z[::-1]
# for i in len

# z00, z

#  101101101011101001000011000100001111010101111
#  111110010111001111100011001111000010000011111
# 1101011111110111000100110001011010101101001110
                                            