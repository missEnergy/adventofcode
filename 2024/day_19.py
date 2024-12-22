from aocd import get_data, submit

year = 2024
day = 19

data = get_data(year=year, day=day)
print(data)

towels, designs = data.split('\n\n')
towels = towels.split(', ')
designs = designs.splitlines()

# PART A
def has_solution(design, towels, solutions):
    if design in towels:
        return True
    for i in range(len(design) - 1):
        if solutions[i] and design[i+1:] in towels:
            return True   

valid_designs = 0
for design in designs:
    solutions = [False for _ in range(len(design))]
    for i in range(len(design)):
        solutions[i] = has_solution(design[:i+1], towels, solutions)
    if solutions[-1]:
        valid_designs += 1
print(valid_designs)
# submit(valid_designs, part="a", day=day, year=year)

# PART B
def unique_solutions(design, towels, solutions):
    unique_solutions = 0
    if design in towels:
        unique_solutions += 1
    for i in range(len(design) - 1):
        if design[i+1:] in towels:
            unique_solutions += solutions[i] 
    return unique_solutions

unique_designs = 0
for design in designs:
    solutions = [0 for _ in range(len(design))]
    for i in range(len(design)):
        solutions[i] = unique_solutions(design[:i+1], towels, solutions)
    
    unique_designs += solutions[-1]
print(unique_designs)
# submit(unique_designs, part="b", day=day, year=year)