import sys

sys.setrecursionlimit(999999)
with open("./lava_input.txt", "r") as f:
# with open("./test.txt", "r") as f:
    lines = f.readlines()


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


def next_point(point, direction, dist):
    # Based on direction and distance, return the next point
    match direction:
        case "R":
            return (point[0] + dist, point[1])
        case "L":
            return (point[0] - dist, point[1])
        case "U":
            return (point[0], point[1] - dist)
        case "D":
            return (point[0], point[1] + dist)


def area_of_polygon(p, perimeter):
    # Use the shoelace formula to get the area of an irregular polygon based on points
    a = 0
    for i in range(len(p) - 1):
        a += p[i][0] * p[i + 1][1]
        a -= p[i][1] * p[i + 1][0]
    a += perimeter  # Don't forget the items in the perimeter
    return (a // 2) + 1  # Add one to include the first point


# move_list = []
# row, col = 1, 1
# max_row, max_col = 0, 0
curr_point = (0, 0)
all_points = [curr_point]  # Shoelace method needs both ends to have the starting point
perimeter = 0
for line in lines:
    line = line.strip()
    move, num, color = line.split(" ")
    curr_point = next_point(curr_point, move, int(num))
    perimeter += int(num)
    all_points.append(curr_point)

    # move_list.append((move, int(num)))
    # if move == "R":
    #     col += int(num)
    # elif move == "L":
    #     col -= int(num)
    # elif move == "D":
    #     row += int(num)
    # elif move == "U":
    #     row -= int(num)
    # max_row = max(max_row, row)
    # max_col = max(max_col, col)

print(area_of_polygon(all_points, perimeter))


def get_direction(num):
    # Return the direction based on the last number of the hex number
    match num:
        case "0":
            return "R"
        case "1":
            return "D"
        case "2":
            return "L"
        case "3":
            return "U"


def hex_number(num):
    # int can convert hex to dec if it begins with 0x and includes base 0 at the end, so add those and return the decimal value
    # of only the first 5 numbers
    return int((num.strip("()").replace("#", "0x")[:7]), 0)


curr_point = (0, 0)
all_points = [curr_point]  # Shoelace method needs both ends to have the starting point
perimeter = 0
for line in lines:
    line = line.strip()
    _, _, color = line.split(" ")
    move = get_direction(color[-2])
    curr_point = next_point(curr_point, move, hex_number(color))
    perimeter += hex_number(color)
    all_points.append(curr_point)

    # move_list.append((move, int(num)))
    # if move == "R":
    #     col += int(num)
    # elif move == "L":
    #     col -= int(num)
    # elif move == "D":
    #     row += int(num)
    # elif move == "U":
    #     row -= int(num)
    # max_row = max(max_row, row)
    # max_col = max(max_col, col)

print(area_of_polygon(all_points, perimeter))

# print(max_row, max_col)
# grid = [["." for _ in range(max_col)] for _ in range(max_row)]
# cur_row, cur_col = 0, 0
# path_set = set()
#
# for move, num in move_list:
#     if move == "R":
#         for _ in range(num):
#             cur_col += 1
#             grid[cur_row][cur_col] = "#"
#     elif move == "L":
#         for _ in range(num):
#             cur_col -= 1
#             grid[cur_row][cur_col] = "#"
#     elif move == "D":
#         for _ in range(num):
#             cur_row += 1
#             grid[cur_row][cur_col] = "#"
#     elif move == "U":
#         for _ in range(num):
#             cur_row -= 1
#             grid[cur_row][cur_col] = "#"
#
#     if grid[cur_row][cur_col] == "#":
#         path_set.add((cur_row, cur_col))
#
#
# def flood_fill_util(x, y, target_color, replacement_color, grid):
#     rows, cols = len(grid), len(grid[0])
#     if x < 0 or x >= rows or y < 0 or y >= cols:
#         return
#     if grid[x][y] != target_color:
#         return
#     grid[x][y] = replacement_color
#     flood_fill_util(x - 1, y, target_color, replacement_color, grid)
#     flood_fill_util(x + 1, y, target_color, replacement_color, grid)
#     flood_fill_util(x, y - 1, target_color, replacement_color, grid)
#     flood_fill_util(x, y + 1, target_color, replacement_color, grid)
#
#
# def flood_fill(point, replacement_color, grid):
#     x, y = point[0], point[1]
#     target_color = grid[x][y]
#     if target_color != replacement_color:
#         flood_fill_util(x, y, target_color, replacement_color, grid)
#
#
# for r in range(max_row):
#     for c in range(max_col):
#         if is_point_inside_loop((r, c), list(path_set)):
#             start_flood_point = (r, c)
#             break
#
#
# # flood_fill(start_flood_point, "#", grid)
#
#
# total = 0
# for row in grid:
#     total += sum([1 if x == "#" else 0 for x in row])
#     print("".join(row))
#
# print(total)
