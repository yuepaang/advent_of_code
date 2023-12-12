import shapely

with open("./pipe_input.txt", "r") as f:
# with open("./test.txt", "r") as f:
    lines = f.readlines()

map = [["" for _ in range(len(lines))] for _ in range(len(lines[0].strip()))]
start_pos = (0, 0)
for i, line in enumerate(lines):
    line = line.strip()
    for j, ch in enumerate(line):
        map[j][i] = ch
        if ch == "S":
            start_pos = (j, i)
# print(start_pos)
# print(map)
adj_info = dict()
for i in range(len(map)):
    for j in range(len(map[0])):
        ch = map[i][j]
        if ch == ".":
            continue
        delta = []
        if ch == "|":
            delta = [(0, 1), (0, -1)]
        elif ch == "-":
            delta = [(1, 0), (-1, 0)]
        elif ch == "J":
            delta = [(-1, 0), (0, -1)]
        elif ch == "L":
            delta = [(1, 0), (0, -1)]
        elif ch == "7":
            delta = [(-1, 0), (0, 1)]
        elif ch == "F":
            delta = [(1, 0), (0, 1)]
        else:
            delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in delta:
            if (
                0 <= i + di < len(map)
                and 0 <= j + dj < len(map[0])
                and map[i + di][j + dj] != "."
            ):
                if (i, j) not in adj_info:
                    adj_info[(i, j)] = []
                adj_info[(i, j)].append((i + di, j + dj))
# print(adj_info)


def bfs(start_pos):
    queue = [start_pos]
    visited = set()
    visited.add(start_pos)
    while queue:
        cur = queue.pop(0)
        if cur not in adj_info:
            continue
        for next in adj_info[cur]:
            if next not in visited:
                queue.append(next)
                visited.add(next)
    return visited


def is_on_segment(p, q, r):
    """Check if point q lies on line segment 'pr'"""
    return (
        q[0] <= max(p[0], r[0])
        and q[0] >= min(p[0], r[0])
        and q[1] <= max(p[1], r[1])
        and q[1] >= min(p[1], r[1])
    )


def orientation(p, q, r):
    """Find orientation of ordered triplet (p, q, r).
    Returns 0 if p, q, r are collinear, 1 if clockwise, 2 if counterclockwise"""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def do_intersect(p1, q1, p2, q2):
    """Check if line segments 'p1q1' and 'p2q2' intersect"""
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and is_on_segment(p1, p2, q1):
        return True

    if o2 == 0 and is_on_segment(p1, q2, q1):
        return True

    if o3 == 0 and is_on_segment(p2, p1, q2):
        return True

    if o4 == 0 and is_on_segment(p2, q1, q2):
        return True

    return False


# def _check_inside_tile(row_idx, col_idx, row_len, col_len, loop):
#     boundary = list()
#     for node in loop:
#         x = node % col_len
#         y = node // col_len
#         boundary.append((x, y))
#     polygon = shapely.geometry.Polygon(boundary)
#     point = shapely.geometry.Point(col_idx, row_idx)
#     return polygon.contains(point)


def is_point_inside_loop(point, loop_points):
    if point in loop_points:
        return False
    """Check if a point is inside a loop defined by loop_points"""
    if len(loop_points) < 3:
        return False

    extreme = (1e9, point[1])
    count = 0
    n = len(loop_points)

    for i in range(n):
        next = (i + 1) % n

        if do_intersect(loop_points[i], loop_points[next], point, extreme):
            if orientation(loop_points[i], point, loop_points[next]) == 0:
                return is_on_segment(loop_points[i], point, loop_points[next])
            count += 1

    return count % 2 == 1


# Example
loop_path = [(0, 0), (10, 0), (10, 10), (0, 10)]

print(len(bfs(start_pos)) / 2)
# path_set = bfs(start_pos)
# total = 0
# for j in range(len(map[0])):
#     s = ""
#     for i in range(len(map)):
#         total += 1
#         print(_check_inside_tile(i, j, len(map[0]), len(map), list(path_set)))
#         if is_point_inside_loop((i, j), list(path_set)):
#             s += "I"
#         else:
#             s += map[i][j]
#     print(f"{s}")
# print(total)


def get_neighs(z):
    # to get valid maze neighbors
    if maze[z] != "S":
        return [z + w for w in direcs[maze[z]]]
    else:  # z = starting point, so check for which neighbors start is a valid neighbor
        neighbors = [
            z + (1 + 0j),
            z + (-1 + 0j),
            z + (1 + 1j),
            z + (-1 + 1j),
            z + (1 - 1j),
            z + (-1 - 1j),
            z + (0 + 1j),
            z + (0 - 1j),
        ]
        return [n for n in neighbors if z in [n + w for w in direcs[maze[n]]]]


def all_neighs(z):
    # returns all 8 complex neighbors of z
    return [
        z + (1 + 0j),
        z + (-1 + 0j),
        z + (1 + 1j),
        z + (-1 + 1j),
        z + (1 - 1j),
        z + (-1 - 1j),
        z + (0 + 1j),
        z + (0 - 1j),
    ]


def display(maze):
    # optional/handy function to print out the current maze space
    for j in range(len(data)):
        line = ""
        for x in range(len(data[0])):
            line += maze[complex(x, j)]
        print(line)
    return ()


# parse data and pad left and right for easier parsing
data = [
    ["."] + [y for y in x] + ["."] for x in lines
]
# pad the data above and below for easier parsing...
data = [["."] * len(data[0])] + data + [["."] * len(data[0])]
# possible neighbor directions for each character
direcs = {
    "F": [0 + 1j, 1 + 0j],
    "7": [-1 + 0j, 0 + 1j],
    "J": [0 - 1j, -1 + 0j],
    "L": [1 + 0j, 0 - 1j],
    "-": [1 + 0j, -1 + 0j],
    "|": [0 + 1j, 0 - 1j],
    ".": [],
}

# to store complex #: character
maze = {}

# populate maze and find start
for h in range(len(data)):
    for w in range(len(data[0])):
        if data[h][w] == "S":
            start = complex(w, h)
        maze[complex(w, h)] = data[h][w]

# initialize current position in finding the circuit/path back to S
cur = start
path = [cur]

while True:
    # get the path points
    # find valid possible new neighbors on the path
    new = [x for x in get_neighs(cur) if x not in path]
    if len(new) > 0:
        cur = new[0]
        path.append(cur)
    else:
        # must be back at the start...
        break

# re-trace along the path, keeping one side to our right,
# and the other to our left.  we will then flood fill
frontier = []
for i in range(1, len(path)):
    # direction vector between prior and current path point
    d = path[i] - path[i - 1]
    # stepping forward to path[i] and backward to path[i-1] this way helps us deal with
    # going around corners without extra complication
    for n in [path[i - 1], path[i]]:
        # turn 90º right of the direction of movement by multiplying d by -i
        right = n + d * complex(0, -1)
        ##turn 90º left of the direction of movement by multiplying d by i
        left = n + d * complex(0, 1)
        if right not in path:
            # label points just to the right of the path in our direction of traversal
            maze[right] = "X"
            frontier.append(right)
        if left not in path:
            # label points just to the left of the path in our direction of traversal
            maze[left] = "Y"
            frontier.append(left)

# flood fill the rest of the non-path spaces
while frontier != []:
    new_front = []
    for f in frontier:
        for n in all_neighs(f):
            if n not in path and maze.get(n, "X") not in ["X", "Y"]:
                new_front.append(n)
                # label the new point correctly
                maze[n] = maze[f]
    frontier = [x for x in new_front]

# suppose the inside has the X label
to_get = "X"
if maze[0 + 0j] == "X":
    # the padding (including the origin) is outside the maze, so switch labels to count
    to_get = "Y"

print(sum([1 for y in maze.values() if y == to_get]))
