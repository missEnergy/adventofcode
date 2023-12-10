import math

from aocd import get_data, submit

year, day = 2023, 9

# COPYRIGHT BY SKILLER WHALE JOLIJN!
data = get_data(year=year, day=day).split("\n")
sum = 0
for line in data:
    lijst_met_getallen_in_string = line.split()
    lijst_met_getallen_in_int = [int(getal) for getal in lijst_met_getallen_in_string]
    lijst_met_getallen_in_int.reverse()  # added reverse() for part B!
    moederlijst = [lijst_met_getallen_in_int]
    sum = sum + moederlijst[-1][-1]
    while set(moederlijst[-1]) != {0}:
        lijst_verschil = []
        for i in range(len(lijst_met_getallen_in_int) - 1):
            verschil = lijst_met_getallen_in_int[i+1] -  lijst_met_getallen_in_int[i]
            lijst_verschil.append(verschil)
        lijst_met_getallen_in_int = lijst_verschil
        moederlijst.append(lijst_verschil)
        sum = sum + moederlijst[-1][-1]
print(sum)
