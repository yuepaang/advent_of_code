from collections import defaultdict, deque


# with open("./test.txt", "r") as f:
with open("./step.txt", "r") as f:
    lines = f.readlines()

graph = []
start = (0, 0)
for i, line in enumerate(lines):
    for j, s in enumerate(line.strip()):
        if s == "S":
            start = (i, j)
    graph.append(list(line.strip()))

print(graph)
print(start)

queue = deque()
queue.append(start)
steps = 64
for i in range(steps):
    print(i, len(queue))
    to_add = set()
    while queue:
        curr = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = curr[0] + dx, curr[1] + dy
            if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
                continue
            if graph[x][y] == "#":
                continue
            to_add.add((x, y))

    queue.extend(to_add)
print(len(queue))


def possible_points(point, garden_map):
    # Loop over all possible directions, and yield each possible new point
    # Check the remainder of the point axis' divided by 131 to continue moving outward infinitely for part 2
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for d in directions:
        new_point = (point[0] + d[0], point[1] + d[1])
        if (
            garden_map[new_point[1] % 131][new_point[0] % 131] != "#"
        ):  # Make sure it wasn't a rock
            yield new_point


def bfs(point, garden_map, max_dist):
    # Use the Breadth first search to find the number of points hit each step, and return the dictionary with key of number of steps taken,
    # and value of number of points hit
    tiles = defaultdict(int)
    visited = set()
    queue = [(point, 0)]
    while queue:  # End when the queue is empty
        curr_point, dist = queue.pop(0)
        if (
            dist == (max_dist + 1) or curr_point in visited
        ):  # Don't include points that have already been visited
            continue

        tiles[dist] += 1
        visited.add(curr_point)

        for next_point in possible_points(
            curr_point, garden_map
        ):  # Loop over possible points and add to queue
            queue.append((next_point, (dist + 1)))
    return tiles


def calculate_possible_spots(start, garden_map, max_steps):
    # Get the output from bfs, and then return the sum of all potential stopping points in the tiles output based on even numbers
    tiles = bfs(start, garden_map, max_steps)
    return sum(
        amount for distance, amount in tiles.items() if distance % 2 == max_steps % 2
    )


def quad(y, n):
    # Use the quadratic formula to find the output at the large steps based on the first three data points
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return (a * n**2) + (b * n) + c


# def part1(parsed_data):
#     # Max steps are 64
#     return calculate_possible_spots(*parsed_data, 64)


def part2(parsed_data):
    # Calculate the first three data points for use in the quadratic formula, and then return the output of quad
    goal = 26501365
    size = len(parsed_data[1])
    edge = size // 2

    y = [
        calculate_possible_spots(start, parsed_data, (edge + i * size))
        for i in range(3)
    ]

    return quad(y, ((goal - edge) // size))


print(part2(graph))
