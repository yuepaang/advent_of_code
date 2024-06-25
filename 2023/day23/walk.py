from collections import deque


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
for i, line in enumerate(lines):
    for j, c in enumerate(line.strip()):
        if i == 0 and c == ".":
            start = (i, j)
        graph[i][j] = c

print(graph)
print(start)

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

queue = deque()
queue.append((start[0], start[1], 0, {(start[0], start[1])}))
while queue:
    x, y, cur_dist, visited = queue.popleft()
    ans = max(ans, cur_dist)
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        if (
            x + dx >= 0
            and x + dx < len(graph)
            and y + dy >= 0
            and y + dy < len(graph[0])
            and graph[x + dx][y + dy] != "#"
            and (x + dx, y + dy) not in visited
            and dp[x + dx][y + dy] < cur_dist + 1
        ):
            new_visited = visited.union({(x + dx, y + dy)})
            queue.append((x + dx, y + dy, cur_dist + 1, new_visited))
            dp[x + dx][y + dy] = cur_dist + 1

print(ans)
