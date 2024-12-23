year = 2024
day = 21

# PART A
# my input
nums = [319, 85, 143, 286, 789] 
seqs = [
    "^A<<A^^>>AvvvA", 
    "<A^^^AvAvv>A", 
    "^<<A^Av>>AvA", 
    "<^A^^Av>AvvA", 
    "^^^<<A>A>AvvvA"
] 
# 319A: ^A<<A^^>>AvvvA of ^A<<A>>^^AvvvA 
# 085A: <A^^^AvA>vvA of <A^^^AvAvv>A
# 143A: ^<<A^A>>vAvA of ^<<A^Av>>AvA
# 286A: ^<A^^A>vAvvA of ^<A^^Av>AvvA of <^A^^A>vAvvA of <^A^^Av>AvvA
# 789A: ^^^<<A>A>AvvvA


#example A
# nums = [29, 980, 179, 456, 379]
# seqs = ["<A^A>^^AvvvA", "^^^A<AvvvA>A", "^<<A^^A>>AvvvA", "^^<<A>A>AvvA", "^A<<^^A>>AvvvA"]
# 029A: <A^A^^>AvvvA of <A^A>^^AvvvA
# 980A: ^^^A<AvvvA>A 
# 179A: ^<<A^^A>>AvvvA
# 456A: ^^<<A>A>AvvA 
# 379A: ^A^^<<A>>AvvvA of ^A<<^^A>>AvvvA

# PART A
answer = 0

seqs_after_1 = []

for id, i in enumerate(seqs):
    seq = i
    for i in range(2): 
        new_seq = ""
        for idx, c in enumerate(seq):
            if idx - 1 == -1:
                prev = 'A'
            else:
                prev = seq[idx - 1]

            if prev == 'A':
                if c == '^':
                    new_seq += '<A'
                elif c == 'v':
                    new_seq += '<vA'
                elif c == '<':
                    new_seq += 'v<<A'
                elif c == '>':
                    new_seq += 'vA'
                elif c == 'A':       
                    new_seq += 'A'
            elif prev == '<':
                if c == '^':
                    new_seq += '>^A'
                elif c == 'v':
                    new_seq += '>A'
                elif c == '<':
                    new_seq += 'A'
                elif c == '>':
                    new_seq += '>>A'
                elif c == 'A':       
                    new_seq += '>>^A'
            elif prev == '>':
                if c == '^':
                    new_seq += '<^A'
                elif c == 'v':
                    new_seq += '<A'
                elif c == '<':
                    new_seq += '<<A'
                elif c == '>':
                    new_seq += 'A'
                elif c == 'A':       
                    new_seq += '^A'
            elif prev == 'v':
                if c == '^':
                    new_seq += '^A'
                elif c == 'v':
                    new_seq += 'A'
                elif c == '<':
                    new_seq += '<A'
                elif c == '>':
                    new_seq += '>A'
                elif c == 'A':       
                    new_seq += '^>A'
            elif prev == '^':
                if c == '^':
                    new_seq += 'A'
                elif c == 'v':
                    new_seq += 'vA'
                elif c == '<':
                    new_seq += 'v<A'
                elif c == '>':
                    new_seq += 'v>A'
                elif c == 'A':       
                    new_seq += '>A'
        seq = new_seq
        if i == 0:
            seqs_after_1.append(seq)
    print(seq)
    answer += nums[id] * len(seq)
print(answer)

# print("109758 lowest answer")
# print(answer)

# part B
uni_parts = set(["<A", '<vA', 'v<<A', 'vA', 'A', '>^A', '>A', 'A', '>>A', '>>^A', '<^A', '<A', '<<A', 'A', '^A', '^A', 'A', '<A', '>A', '^>A', 'A', 'vA', 'v<A', 'v>A', '>A'])
lookup_growth = {}

for seq in uni_parts:
    new_seq = ""
    for idx, c in enumerate(seq):
        if idx - 1 == -1:
            prev = 'A'
        else:
            prev = seq[idx - 1]

        if prev == 'A':
            if c == '^':
                new_seq += '<A'
            elif c == 'v':
                new_seq += '<vA'
            elif c == '<':
                new_seq += 'v<<A'
            elif c == '>':
                new_seq += 'vA'
            elif c == 'A':       
                new_seq += 'A'
        elif prev == '<':
            if c == '^':
                new_seq += '>^A'
            elif c == 'v':
                new_seq += '>A'
            elif c == '<':
                new_seq += 'A'
            elif c == '>':
                new_seq += '>>A'
            elif c == 'A':       
                new_seq += '>>^A'
        elif prev == '>':
            if c == '^':
                new_seq += '<^A'
            elif c == 'v':
                new_seq += '<A'
            elif c == '<':
                new_seq += '<<A'
            elif c == '>':
                new_seq += 'A'
            elif c == 'A':       
                new_seq += '^A'
        elif prev == 'v':
            if c == '^':
                new_seq += '^A'
            elif c == 'v':
                new_seq += 'A'
            elif c == '<':
                new_seq += '<A'
            elif c == '>':
                new_seq += '>A'
            elif c == 'A':       
                new_seq += '^>A'
        elif prev == '^':
            if c == '^':
                new_seq += 'A'
            elif c == 'v':
                new_seq += 'vA'
            elif c == '<':
                new_seq += 'v<A'
            elif c == '>':
                new_seq += 'v>A'
            elif c == 'A':       
                new_seq += '>A'
    lookup_growth[seq] = new_seq

# PART B
answer = 0
for id, i in enumerate(seqs_after_1):
    seq = i
    seq = [j + 'A' for j in seq.split("A")]
    seq.pop() # remove last A (shouldn't be there)
    seq_dict = {}
    for j in seq:
        if j not in seq_dict:
            seq_dict[j] = 1
        else:
            seq_dict[j] += 1
    
    for i in range(24): 
        new_seq_dict = {}
        for k, v in seq_dict.items():
            new_seq = lookup_growth[k]
            new_seq = [j + 'A' for j in new_seq.split("A")]
            new_seq.pop() # remove last A (shouldn't be there)
            for j in new_seq:
                if j not in new_seq_dict:
                    new_seq_dict[j] = v
                else:
                    new_seq_dict[j] += v
        seq_dict = new_seq_dict
    print(seq_dict)
    total_len = 0
    for k, v in seq_dict.items():
        total_len += v * len(k)
    answer += nums[id] * total_len
print(answer)