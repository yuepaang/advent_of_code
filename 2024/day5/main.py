from collections import defaultdict


# with open("./2024/day5/eg.txt", "r") as f:
with open("./2024/day5/input.txt", "r") as f:
    lines = f.readlines()


def topological_sort_relations(items, relations):
    # Build adjacency list
    graph = defaultdict(list)
    for x, y in relations:
        graph[x].append(y)

    # Keep track of visited status: 0=unvisited, 1=visiting, 2=visited
    visited = {item: 0 for item in items}
    result = []  # Holds the sorted order
    has_cycle = [False]  # Use a list so we can modify inside nested func

    def dfs(node):
        if visited[node] == 1:
            # Found a back edge => cycle
            has_cycle[0] = True
            return
        if visited[node] == 2:
            return

        # Mark as visiting
        visited[node] = 1
        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in items:
                continue
            if has_cycle[0]:
                return
            dfs(neighbor)

        # Mark as visited
        visited[node] = 2
        # Add to result
        result.append(node)

    # DFS on each unvisited node
    for item in items:
        if visited[item] == 0:
            dfs(item)
            if has_cycle[0]:
                return None  # or raise Exception("Cycle detected")

    # Reverse result because we appended in post-visit
    result.reverse()
    return result


def is_subsequence(sorted_list, sub_list):
    """
    Return True if all elements of sub_list appear in sorted_list
    in the same relative order; otherwise False.
    """
    j = 0  # pointer for sub_list
    for item in sorted_list:
        if j < len(sub_list) and item == sub_list[j]:
            j += 1
        if j == len(sub_list):
            break
    return j == len(sub_list)


def reorder_sublist_to_sorted_order(sorted_list, sub_list):
    """
    Re-order sub_list so that its elements appear in the same relative
    order as in sorted_list.
    """
    # 1. Build a dictionary mapping each item in sorted_list -> its index
    order_map = {val: i for i, val in enumerate(sorted_list)}

    # 2. Sort sub_list by the index stored in order_map
    #    (if sub_list contains elements not in sorted_list, handle carefully)
    sub_list.sort(key=lambda x: order_map[x])
    return sub_list


nodes = set()
relations = []
part_one_res = 0
part_two_res = 0
for line in lines:
    if "|" in line:
        x, y = line.split("|")
        x, y = int(x), int(y)
        nodes.add(x)
        nodes.add(y)
        relations.append((x, y))
    elif line.strip() == "":
        continue
    else:
        update = [int(v) for v in line.strip().split(",")]
        # only consider nodes that are in the update
        sorted_nodes = topological_sort_relations(
            list(nodes.intersection(set(update))), relations
        )
        # part one
        if is_subsequence(sorted_nodes, update):
            mid = len(update) // 2
            part_one_res += update[mid]
            continue
        # part two
        else:
            # print("old: ", update)
            new_update = reorder_sublist_to_sorted_order(sorted_nodes, update)
            # print("new: ", new_update)
            mid = len(new_update) // 2
            part_two_res += new_update[mid]
            continue

print(part_one_res)
print(part_two_res)
