from collections import deque
from copy import deepcopy


# def main(file: str):
#     with open(file, "r") as f:
#         forest = [list(line.strip()) for line in f.readlines()]

#     start = (0, 1)
#     end = (len(forest) - 1, len(forest[0]) - 2)
#     nodes = [start, end]
#     # find nodes
#     for y in range(len(forest)):
#         for x in range(len(forest[0])):
#             if forest[y][x] == ".":
#                 poss = 0
#                 for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                     neigh_y = y + d[0]
#                     neigh_x = x + d[1]
#                     # if not out of bounds and not a wall
#                     if (
#                         0 <= neigh_y < len(forest)
#                         and 0 <= neigh_x < len(forest[0])
#                         and forest[neigh_y][neigh_x] != "#"
#                     ):
#                         poss += 1
#                 if poss >= 3:
#                     nodes.append((y, x))

#     graph = {node: {} for node in nodes}

#     for sy, sx in nodes:
#         stack = [(0, sy, sx)]
#         visited = {(sy, sx)}
#         while stack:
#             n, y, x = stack.pop()

#             if n != 0 and (y, x) in nodes:
#                 graph[(sy, sx)][(y, x)] = n
#                 continue

#             for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 new_y = y + d[0]
#                 new_x = x + d[1]
#                 if (
#                     0 <= new_y < len(forest)
#                     and 0 <= new_x < len(forest[0])
#                     and forest[new_y][new_x] != "#"
#                     and (new_y, new_x) not in visited
#                 ):
#                     stack.append((n + 1, new_y, new_x))
#                     visited.add((new_y, new_x))

#     seen = set()

#     def find_longest_path(pt):
#         if pt == end:
#             return 0

#         path = float("-inf")

#         seen.add(pt)
#         for next_node in graph[pt]:
#             if next_node not in seen:
#                 path = max(path, graph[pt][next_node] + find_longest_path(next_node))
#         seen.remove(pt)

#         return path

#     print(find_longest_path(start))


# # 6586
# main("walk_input.txt")


# with open("./test.txt", "r") as f:
with open("./walk_input.txt", "r") as f:
    lines = f.readlines()

graph = [["" for _ in range(len(lines[i]) - 1)] for i in range(len(lines))]

start = (0, 0)
end = (0, 0)
for i, line in enumerate(lines):
    for j, c in enumerate(line.strip()):
        if i == 0 and c == ".":
            start = (i, j)
        if i == len(lines) - 1 and c == ".":
            end = (i, j)
        graph[i][j] = c

print(graph)
print(start, end)

directions_map = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

dp = [[-1 for _ in range(len(graph[i]))] for i in range(len(graph))]

dp[start[0]][start[1]] = 0
ans = 0

# queue = deque()
# queue.append((start[0], start[1], 0, {(start[0], start[1])}))
# while queue:
#     x, y, cur_dist, visited = queue.popleft()
#     # print(cur_dist, visited)
#     if graph[x][y] in directions_map:
#         dx, dy = directions_map[graph[x][y]]
#         if (
#             x + dx >= 0
#             and x + dx < len(graph)
#             and y + dy >= 0
#             and y + dy < len(graph[i])
#             and graph[x + dx][y + dy] != "#"
#             and (x + dx, y + dy) not in visited
#         ):
#             if dp[x + dx][y + dy] < cur_dist + 1:
#                 new_visited = visited.union({(x + dx, y + dy)})
#                 queue.append((x + dx, y + dy, cur_dist + 1, new_visited))
#                 dp[x + dx][y + dy] = cur_dist + 1
#     else:
#         for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
#             if (
#                 x + dx >= 0
#                 and x + dx < len(graph)
#                 and y + dy >= 0
#                 and y + dy < len(graph[i])
#                 and graph[x + dx][y + dy] != "#"
#                 and (x + dx, y + dy) not in visited
#             ):
#                 if dp[x + dx][y + dy] < cur_dist + 1:
#                     new_visited = visited.union({(x + dx, y + dy)})
#                     queue.append((x + dx, y + dy, cur_dist + 1, new_visited))
#                     dp[x + dx][y + dy] = cur_dist + 1
#     ans = max(ans, cur_dist)

# print(ans)

# part two

# queue = deque()
# queue.append((start[0], start[1], 0, {(start[0], start[1])}))
# while queue:
#     x, y, cur_dist, visited = queue.popleft()
#     ans = max(ans, cur_dist)
#     for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
#         if (
#             x + dx >= 0
#             and x + dx < len(graph)
#             and y + dy >= 0
#             and y + dy < len(graph[0])
#             and graph[x + dx][y + dy] != "#"
#             and (x + dx, y + dy) not in visited
#             and dp[x + dx][y + dy] < cur_dist + 1
#         ):
#             new_visited = visited.union({(x + dx, y + dy)})
#             queue.append((x + dx, y + dy, cur_dist + 1, new_visited))
#             dp[x + dx][y + dy] = cur_dist + 1

# print(ans)


def get_neighbors(x, y, px, py):
    # print(x, y, px, py)
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        if (
            x + dx >= 0
            and x + dx < len(graph)
            and y + dy >= 0
            and y + dy < len(graph[0])
            and graph[x + dx][y + dy] != "#"
        ):
            if px != -1 and py != -1 and x + dx == px and y + dy == py:
                continue
            neighbors.append((x + dx, y + dy))
    return neighbors


def build_graph():
    g = {}
    stack = deque()
    stack.append(
        (
            start,
            start,
            0,
            (-1, -1),
        )
    )
    while stack:
        cur, from_node, edge_len, prev = stack.pop()
        neighbors = get_neighbors(*cur, *prev)
        if len(neighbors) == 1:
            stack.append((neighbors[0], from_node, edge_len + 1, cur))
        else:
            if cur in g and from_node in set([e[0] for e in g[cur]]):
                continue
            s = set()
            s.add((from_node, edge_len))
            if cur not in g:
                g[cur] = s
            else:
                g[cur] |= s

            for n in neighbors:
                stack.append((n, cur, 1, cur))
    return g


class Path:
    def __init__(self, path, length):
        self.path = path
        self.length = length

    def __hash__(self):
        return hash(tuple(self.path))

    def __eq__(self, other):
        return self.path == other.path

    def __repr__(self):
        return f"Path: {self.path} - {self.length}"


def find_path_length(g):
    stack = deque()
    stack.append(Path([end], 0))
    mem = {}
    while stack:
        p = stack.pop()
        head = p.path[-1]
        if head not in g:
            continue

        for edge in g[head]:
            if edge[0] in p.path:
                # print(f"Skipping {edge[0]} because it's already in the path")
                continue
            tmp_path = deepcopy(p.path)
            tmp_path.append(edge[0])
            tmp_len = edge[1] + p.length
            if edge[0] not in mem or tmp_len > mem[edge[0]].length:
                mem[edge[0]] = Path(tmp_path, tmp_len)
            stack.append(Path(tmp_path, tmp_len))

    return mem[start].length


g = build_graph()
print(g)
ans = find_path_length(g)
print(ans)
