from collections import defaultdict
from heapq import heappop, heappush


with open("./clumsy_input.txt", "r") as f:
# with open("./test.txt", "r") as f:
    lines = f.readlines()

graph = []

for line in lines:
    graph.append([int(e) for e in line.strip()])
# print(graph)
print("size: ", len(graph), len(graph[0]))


def get_move(dr, dc):
    if dr == 1 and dc == 0:
        return "down"
    elif dr == -1 and dc == 0:
        return "up"
    elif dr == 0 and dc == 1:
        return "right"
    elif dr == 0 and dc == -1:
        return "left"


def check_part_one(curr_dr, curr_dc, dr, dc, straight):
    # If the direction is the same as the previous one, return None, if it's a new direction, return 1, and if it's the same direction,
    # return plus one to the straight variable
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if (dr, dc) != (curr_dr, curr_dc):
        return 1
    if (dr, dc) == (curr_dr, curr_dc):
        return straight + 1


def check_part_two(curr_dr, curr_dc, dr, dc, straight):
    # If direction is the same, add one to the straight variable, if it's opposite, add none, if it's gone for more than 4 spaces, return 1
    if (dr, dc) == (curr_dr, curr_dc):
        return straight + 1
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if straight >= 4 or (curr_dr, curr_dc) == (0, 0):
        return 1


def shortest_path(graph, check_function, max_straight=4):
    """
    Finds the shortest weight path from (0, 0) to (n-1, n-1) in a 2D array representing the graph.

    Args:
        graph: A 2D array representing the graph, where each element is the weight of the edge.

    Returns:
        A tuple containing the shortest weight and the path as a list of coordinates.
    """
    n = len(graph)
    # dist = [[float("inf")] * n for _ in range(n)]
    dist = {
        (i, j): defaultdict(lambda: float("inf")) for i in range(n) for j in range(n)
    }
    # dist[0][0] = 0
    pq = [
        (0, 0, 0, (0, 0), 1, [])
    ]  # (distance, row, col, last direction, last direction move count, Path)

    while pq:
        d, r, c, ld, straight_num, path = heappop(pq)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if dr + ld[0] == 0 and dc + ld[1] == 0:
                continue
            new_num = check_function(ld[0], ld[1], dr, dc, straight_num)
            if not new_num or new_num == max_straight:
                continue

            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < n and 0 <= new_c < n:
                new_dist = d + graph[new_r][new_c]
                if new_dist < dist[(new_r, new_c)][(dr, dc, new_num)]:
                    # dist[new_r][new_c] = new_dist
                    dist[(new_r, new_c)][(dr, dc, new_num)] = new_dist
                    heappush(
                        pq,
                        (
                            new_dist,
                            new_r,
                            new_c,
                            (dr, dc),
                            new_num,
                            path + [get_move(dr, dc)],
                        ),
                    )

    return dist  # No path found


# res = shortest_path(graph, check_part_one)
# n = len(graph)
# print(min(res[(n - 1, n - 1)].values()))

res = shortest_path(graph, check_part_two, 11)
n = len(graph)
print(min(res[(n - 1, n - 1)].values()))
