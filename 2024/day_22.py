from aocd import get_data, submit

year = 2024
day = 22

data = get_data(year=year, day=day)
secrets = map(int, data.splitlines())

# PART A
answer = 0
for s in secrets:
    secret = s
    for i in range(2000):
        secret = (secret * 64) ^ secret
        secret = secret % 16777216
        secret = int(secret / 32) ^ secret
        secret = secret % 16777216
        secret = (secret * 2048) ^ secret
        secret = secret % 16777216
    answer += secret

print(answer)
# submit(answer, part="a", day=day, year=year)

# PART B
prices = []
prices_diff = []
for s in secrets:
    secret = s
    prices_s = [secret % 10]
    prices_s_diff = [None]
    for i in range(2000):
        secret = (secret * 64) ^ secret
        secret = secret % 16777216
        secret = int(secret / 32) ^ secret
        secret = secret % 16777216
        secret = (secret * 2048) ^ secret
        secret = secret % 16777216
        prices_s.append(secret % 10 ) # TO GET ONLY THE FIRST DIGIT!
        prices_s_diff.append(prices_s[-1] - prices_s[-2])
    prices.append(prices_s)
    prices_diff.append(prices_s_diff)

what_occurs_often = {}
for h in range(len(prices)):
    for i in range(1, 2001-4):
        try_diff_seq = prices_diff[h][i:i+4]
        if str(try_diff_seq) in what_occurs_often:
            what_occurs_often[str(try_diff_seq)] += 1
        else:
            what_occurs_often[str(try_diff_seq)] = 1
sorted_what_occurs_often = sorted(what_occurs_often.items(), key=lambda x: x[1], reverse=True)

print(f"len(sorted_what_occurs_often): {len(sorted_what_occurs_often)}")

max_bananas = 0
for key, value in sorted_what_occurs_often:
    try_diff_seq = key
    print(key, value)
    bananas = 0
    for j in range(len(prices_diff)):
        for k in range(1, 2001-4):
            if str(prices_diff[j][k:k+4]) == try_diff_seq:
                bananas += prices[j][k+3]
                break
    if bananas > max_bananas:
        max_bananas = bananas
    print(f"max_bananas: {max_bananas}")