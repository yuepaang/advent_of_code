from copy import deepcopy
from itertools import combinations


# with open("./test.txt", "r") as f:
with open("./snow_input.txt", "r") as f:
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


def dfs(node, visited, nm):
    if node.name in visited:
        return
    visited.add(node.name)
    for child in node.children:
        dfs(nm[child], visited, nm)


# group = set()
# for name, node in node_map.items():
#     visited = set()
#     dfs(node, visited, node_map)
#     group.add(tuple(sorted(visited)))
# print(group)

all_nodes = list(node_map.keys())
coms = combinations(all_nodes, 3)
for com in coms:
    cand = [[] for _ in range(3)]
    for i, n in enumerate(com):
        for on in node_map[n].children:
            if on in com:
                continue
            cand[i].append((n, on))
    for a in cand[0]:
        for b in cand[1]:
            for c in cand[2]:
                tmp_node_map = deepcopy(node_map)
                tmp_node_map[a[0]].children.remove(a[1])
                tmp_node_map[a[1]].children.remove(a[0])
                tmp_node_map[b[0]].children.remove(b[1])
                tmp_node_map[b[1]].children.remove(b[0])
                tmp_node_map[c[0]].children.remove(c[1])
                tmp_node_map[c[1]].children.remove(c[0])
                group = set()
                for name, node in tmp_node_map.items():
                    visited = set()
                    dfs(node, visited, tmp_node_map)
                    group.add(tuple(sorted(visited)))
                group = list(group)
                if len(group) == 2:
                    print(group)
                    print(len(group[0]) * len(group[1]))
                    raise Exception("find it")
