from copy import deepcopy
from itertools import combinations


# with open("./snow_input.txt", "r") as f:
with open("./test.txt", "r") as f:
    lines = f.readlines()


class Node(object):
    def __init__(self, name, children):
        self.name = name
        self.children = children


node_map = {}
for line in lines:
    line = line.strip()
    a, bs = line.split(": ")
    all_node = set(bs.split(" "))
    if a not in node_map:
        node_map[a] = Node(a, all_node)
    else:
        node_map[a].children = node_map[a].children | (all_node)
    for b in bs.split(" "):
        if b not in node_map:
            node_map[b] = Node(b, {a})
        else:
            node_map[b].children.add(a)

print("node number:", len(node_map))
for name, node in node_map.items():
    print(name, node.children)

# how to find these
# node_map["hfx"].children.remove("pzl")
# node_map["pzl"].children.remove("hfx")
# node_map["bvb"].children.remove("cmg")
# node_map["cmg"].children.remove("bvb")
# node_map["nvd"].children.remove("jqt")
# node_map["jqt"].children.remove("nvd")


def dfs(node, visited):
    if node.name in visited:
        return
    visited.add(node.name)
    for child in node.children:
        dfs(node_map[child], visited)


group = set()
for name, node in node_map.items():
    visited = set()
    dfs(node, visited)
    group.add(tuple(sorted(visited)))
print(group)

all_nodes = list(node_map.keys())
coms = combinations(all_nodes, 3)
for com in coms:
    tmp_node_map = deepcopy(node_map)
    print(com)
    cand = [[] for _ in range(3)]
    for i, n in enumerate(com):
        for on in tmp_node_map[n].children:
            if on in com:
                continue
            cand[i].append((n, on))
    print(cand)
    for a, b, c in zip(cand[0], cand[1], cand[2]):
        print(a, b, c)
    break
