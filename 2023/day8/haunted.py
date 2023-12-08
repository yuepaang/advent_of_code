import math
from collections import defaultdict


with open("./haunted_input.txt", "r") as f:
    # with open("./test.txt", "r") as f:
    lines = f.readlines()

# Part one
# moves = []
# node_map = defaultdict(dict)
# start_node = "AAA"
# end_node = "ZZZ"
# for i, line in enumerate(lines):
#     line = line.strip()
#     if i == 0:
#         moves = list(line)
#     elif line == "":
#         continue
#     else:
#         key, value = line.split(" = ")
#         value = value.replace("(", "")
#         value = value.replace(")", "")
#         node_map[key]["L"] = value.split(", ")[0]
#         node_map[key]["R"] = value.split(", ")[1]

# current_node = start_node
# step = 0
# while current_node != end_node:
#     for move in moves:
#         step += 1
#         if move == "L":
#             current_node = node_map[current_node]["L"]
#         elif move == "R":
#             current_node = node_map[current_node]["R"]

# print(step)

moves = []
node_map = defaultdict(dict)
start_nodes = []
for i, line in enumerate(lines):
    line = line.strip()
    if i == 0:
        moves = list(line)
    elif line == "":
        continue
    else:
        key, value = line.split(" = ")
        if key.endswith("A"):
            start_nodes.append(key)
        value = value.replace("(", "")
        value = value.replace(")", "")
        node_map[key]["L"] = value.split(", ")[0]
        node_map[key]["R"] = value.split(", ")[1]


current_nodes = start_nodes
step = 0
end_step = [0 for _ in range(len(current_nodes))]
while True:
    if all(end_step):
        break
    for move in moves:
        for i, n in enumerate(current_nodes):
            if n.endswith("Z"):
                end_step[i] = step
        step += 1
        if move == "L":
            current_nodes = [node_map[n]["L"] for n in current_nodes]
        elif move == "R":
            current_nodes = [node_map[n]["R"] for n in current_nodes]

print(end_step)
print(math.lcm(*end_step))
