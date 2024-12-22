with open("./2024/day4/input.txt", "r") as f:
    # with open("./2024/day4/eg.txt", "r") as f:
    lines = f.readlines()

graph = []
for line in lines:
    graph.append(list(line.strip()))

m, n = len(graph), len(graph[0])

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


def is_valid(i, j):
    return 0 <= i < m and 0 <= j < n


def part_one():
    def search(i, j, level, dir, cnt):
        if level == 0:
            for d in directions:
                x, y = i + directions[d][0], j + directions[d][1]
                if is_valid(x, y) and graph[x][y] == "M":
                    search(x, y, 1, d, cnt)
        else:
            x, y = i + directions[dir][0], j + directions[dir][1]
            if is_valid(x, y):
                if level == 1 and graph[x][y] == "A":
                    search(x, y, 2, dir, cnt)
                elif level == 2 and graph[x][y] == "S":
                    cnt[0] += 1

    res = [0]
    for i in range(m):
        for j in range(n):
            if graph[i][j] == "X":
                # dfs(i, j, 0, "")
                search(i, j, 0, "", res)

    print(res[0])


part_one()


def part_two():
    diag_one = ["lud", "rdd"]
    diag_two = ["ldd", "rud"]

    def is_x(i, j):
        ms_cnt = {"M": 0, "S": 0}
        flag_one, flag_two = False, False
        for d in diag_one:
            x, y = i + directions[d][0], j + directions[d][1]
            if is_valid(x, y) and (graph[x][y] == "M" or graph[x][y] == "S"):
                ms_cnt[graph[x][y]] += 1
        if ms_cnt["M"] == 1 and ms_cnt["S"] == 1:
            flag_one = True
        for d in diag_two:
            x, y = i + directions[d][0], j + directions[d][1]
            if is_valid(x, y) and (graph[x][y] == "M" or graph[x][y] == "S"):
                ms_cnt[graph[x][y]] += 1
        if ms_cnt["M"] == 2 and ms_cnt["S"] == 2:
            flag_two = True
        return flag_one and flag_two

    res = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == "A":
                if is_x(i, j):
                    res += 1
    print(res)


part_two()
