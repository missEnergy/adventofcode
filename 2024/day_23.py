from aocd import get_data, submit
import networkx as nx

year = 2024
day = 23

data = get_data(year=year, day=day)
lines = data.splitlines()

G = nx.Graph()            
for line in lines:
    a, b = line.split("-")
    G.add_edge(a, b)

# PART A
complete_graphs_of_3 = []
for i in nx.enumerate_all_cliques(G):
    if len(i) == 3:
        complete_graphs_of_3.append(i)
    if len(i) > 3:
        break

complete_graphs_of_3_filtered = [i for i in complete_graphs_of_3 if i[0][0] == 't' or i[1][0] == 't' or i[2][0] == 't']
answer = len(complete_graphs_of_3_filtered)
print(answer)
# submit(answer, part="a", day=day, year=year)

# # PART B
max_size = 0
LAN = []
G_LAN = nx.find_cliques(G)
for i in G_LAN:
    if len(i) > max_size:
        max_size = len(i)
        LAN = sorted(i)
print(LAN)

answer = ''
for node in LAN:
    answer += node + ","
answer = answer[:-1]
print(answer)
submit(answer, part="b", day=day, year=year)