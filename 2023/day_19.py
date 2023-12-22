import math

from aocd import get_data, submit

year, day = 2023, 19

# parse data
data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
data = get_data(year=year, day=day)

data_workflows, data_parts = data.split("\n\n")

workflows = {}
for wf in data_workflows.split("\n"):
    workflow_name = wf.split("{")[0]
    data_rules = wf.split("{")[1][:-1].split(",")
    rules = []
    for r in data_rules:
        if ":" in r:
            condition, destination = r.split(":")
        else:
            condition = None
            destination = r
        rules.append({"condition": condition, "destination": destination})
    workflows[workflow_name] = rules

parts = []
for p in data_parts.split("\n"):
    ratings = p[1:-1].split(",")
    part = {}
    for r in ratings:
        part[r[0]] = r[2:]
    parts.append(part)


def meets_condition(part, condition):
    rating = condition[0]
    return eval(condition.replace(rating, part[rating]))


# part A
accepted_parts = []
for p in parts:
    loc = "in"
    while loc not in ["A", "R"]:
        wf = workflows[loc]
        for r in wf:
            if r["condition"] is None or meets_condition(p, r["condition"]):
                loc = r["destination"]
                break
    if loc == "A":
        accepted_parts.append(p)
print(accepted_parts)
answer_a = 0
for p in accepted_parts:
    answer_a += sum([int(i) for i in p.values()])
print(answer_a)
# submit(answer_a, part="a", day=day, year=year)

# part B
combinations_to_finish = [{"conditions": [], "loc": "in"}]
accepted_combinations = []
while len(combinations_to_finish) > 0:
    combi = combinations_to_finish[0]
    combinations_to_finish.pop(0)

    conditions = combi["conditions"]
    wf = workflows[combi["loc"]]

    for r in wf:
        if r["destination"] == "A":
            print("accept!")
            accepted_combinations.append(conditions + [r["condition"]])
        elif r["destination"] == "R":
            print("reject!")
        else:
            combinations_to_finish.append({"conditions": conditions + [r["condition"]], "loc": r["destination"]})

        if r["condition"] is not None:
            conditions.append("!" + r["condition"])
print(len(accepted_combinations))


def get_start_values():
    all_values = {}
    for i in ["x", "m", "a", "s"]:
        all_values[i] = [i for i in range(1, 4001)]
    return all_values


distinct_combis = 0
for count, combi in enumerate(accepted_combinations):
    print(count)
    values = get_start_values()
    for r in combi:
        if r is None:
            continue
        elif r[0] == "!":
            rating = r[1]
            values[rating] = [i for i in values[rating] if not eval(r[1:].replace(rating, str(i)))]
        else:
            rating = r[0]
            values[rating] = [i for i in values[rating] if eval(r.replace(rating, str(i)))]
    distinct_combis += math.prod([len(i) for i in values.values()])
print(distinct_combis)
# submit(distinct_combis, part="b", day=day, year=year)