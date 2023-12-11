import shapely

# with open("./pipe_input.txt", "r") as f:
with open("./test.txt", "r") as f:
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


def _check_inside_tile(row_idx, col_idx, row_len, col_len, loop):
    boundary = list()
    for node in loop:
        x = node % col_len
        y = node // col_len
        boundary.append((x, y))
    polygon = shapely.geometry.Polygon(boundary)
    point = shapely.geometry.Point(col_idx, row_idx)
    return polygon.contains(point)


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
path_set = bfs(start_pos)
total = 0
for j in range(len(map[0])):
    s = ""
    for i in range(len(map)):
        total += 1
        print(_check_inside_tile(i, j, len(map[0]), len(map), list(path_set)))
        if is_point_inside_loop((i, j), list(path_set)):
            s += "I"
        else:
            s += map[i][j]
    print(f"{s}")
print(total)
