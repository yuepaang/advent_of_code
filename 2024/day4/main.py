with open(r"D:\Work\advent_of_code_2023\2024\day4\input.txt", "r") as f:
    # with open(r"D:\Work\advent_of_code_2023\2024\day4\eg.txt", "r") as f:
    lines = f.readlines()

graph = []
for line in lines:
    graph.append(list(line.strip()))

m, n = len(graph), len(graph[0])


def is_valid(i, j):
    return 0 <= i < m and 0 <= j < n


directions = {
    "lh": (0, -1),
    "rh": (0, 1),
    "uv": (-1, 0),
    "dv": (1, 0),
    "lud": (-1, -1),
    "ldd": (1, -1),
    "rud": (-1, 1),
    "rdd": (1, 1),
}


def search(i, j, level, dir):
    if level == 0:
        for d in directions:
            x, y = i + directions[d][0], j + directions[d][1]
            if is_valid(x, y) and graph[x][y] == "M":
                search(x, y, 1, d)
    else:
        x, y = i + directions[dir][0], j + directions[dir][1]
        if is_valid(x, y):
            if level == 1 and graph[x][y] == "A":
                search(x, y, 2, dir)
            elif level == 2 and graph[x][y] == "S":
                global res
                res += 1


res = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == "X":
            # dfs(i, j, 0, "")
            search(i, j, 0, "")

print(res)
