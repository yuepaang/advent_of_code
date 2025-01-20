# with open("./2024/day6/eg.txt", "r") as f:
with open("./2024/day6/input.txt", "r") as f:
    lines = f.readlines()

graph = []
start_pos = (0, 0)
for i, line in enumerate(lines):
    r = []
    for j, p in enumerate(line.strip()):
        if p != "#" and p != ".":
            start_pos = (i, j)
        r.append(p)
    graph.append(r)

# print(graph)
# print(start_pos)


def is_out_of_bound(pos):
    return pos[0] < 0 or pos[0] >= len(graph) or pos[1] < 0 or pos[1] >= len(graph[0])


directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


def get_next_pos(pos, direction):
    end_flag = False
    new_x = pos[0] + direction[0]
    new_y = pos[1] + direction[1]
    visited = set()
    while graph[new_x][new_y] != "#":
        pos = (new_x, new_y)
        visited.add(pos)
        new_x = pos[0] + direction[0]
        new_y = pos[1] + direction[1]
        if is_out_of_bound((new_x, new_y)):
            end_flag = True
            break
    return pos, visited, end_flag


def get_right_turn(direction):
    if direction == "<":
        return "^"
    elif direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    else:
        raise ValueError("Invalid direction")


def part_one(graph, start_pos):
    res = set()
    res.add(start_pos)
    end_flag = False
    while not end_flag:
        dir = graph[start_pos[0]][start_pos[1]]
        graph[start_pos[0]][start_pos[1]] = "."
        start_pos, visited, end_flag = get_next_pos(start_pos, directions[dir])
        graph[start_pos[0]][start_pos[1]] = get_right_turn(dir)
        # print(start_pos, visited)
        res = res.union(visited)
        # print("===")
    print(len(res))


part_one(graph, start_pos)

path = set()
path.add((start_pos[0], start_pos[1], graph[start_pos[0]][start_pos[1]]))
end_flag = False
while not end_flag:
    dir = graph[start_pos[0]][start_pos[1]]
    graph[start_pos[0]][start_pos[1]] = "."
    start_pos, visited, end_flag = get_next_pos(start_pos, directions[dir])
    graph[start_pos[0]][start_pos[1]] = get_right_turn(dir)
    # print(start_pos, visited)
    path = path.union(visited)
