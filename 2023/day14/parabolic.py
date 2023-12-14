from collections import OrderedDict, Counter
with open("./parabolic_input.txt", "r") as f:
# with open("./test.txt", "r") as f:
    lines = f.readlines()

matrix = []
empty_slots = [[] for _ in range(len(lines[0].strip()))]
for i, line in enumerate(lines):
    row = []
    line = line.strip()
    for j, c in enumerate(line):
        row.append(c)
        if c == "." or c == "#":
            empty_slots[j].append((c, i, j))
    matrix.append(row)

# print(matrix)
# print(empty_slots)


def to_north(matrix):
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == "O":
                continue
            elif matrix[i][j] == ".":
                for down_i in range(i + 1, len(matrix)):
                    if matrix[down_i][j] == "O":
                        matrix[i][j], matrix[down_i][j] = (
                            matrix[down_i][j],
                            matrix[i][j],
                        )
                    elif matrix[down_i][j] == "#":
                        break


def to_south(matrix):
    for j in range(len(matrix[0])):
        for i in range(len(matrix) - 1, -1, -1):
            if matrix[i][j] == "O":
                continue
            elif matrix[i][j] == ".":
                for next_i in range(i - 1, -1, -1):
                    if matrix[next_i][j] == "O":
                        matrix[i][j], matrix[next_i][j] = (
                            matrix[next_i][j],
                            matrix[i][j],
                        )
                    elif matrix[next_i][j] == "#":
                        break


def to_east(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 1, -1, -1):
            if matrix[i][j] == "O":
                continue
            elif matrix[i][j] == ".":
                for next_j in range(j - 1, -1, -1):
                    if matrix[i][next_j] == "O":
                        matrix[i][j], matrix[i][next_j] = (
                            matrix[i][next_j],
                            matrix[i][j],
                        )
                    elif matrix[i][next_j] == "#":
                        break


def to_west(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "O":
                continue
            elif matrix[i][j] == ".":
                for next_j in range(j + 1, len(matrix[0])):
                    if matrix[i][next_j] == "O":
                        matrix[i][j], matrix[i][next_j] = (
                            matrix[i][next_j],
                            matrix[i][j],
                        )
                    elif matrix[i][next_j] == "#":
                        break


to_north(matrix)
for line in matrix:
    print("".join(line))


def get_load(matrix):
    total = 0
    for i in range(0, len(matrix)):
        load = len(matrix) - i
        rock_cnt = 0
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == "O":
                rock_cnt += 1
        total += rock_cnt * load
    return total


print(get_load(matrix))


seq = []
patterns = OrderedDict()
for i in range(1000000000):
    if i % 4 == 0:
        to_north(matrix)
    elif i % 4 == 1:
        to_west(matrix)
    elif i % 4 == 2:
        to_south(matrix)
    elif i % 4 == 3:
        to_east(matrix)

    if i % 2 == 1:
        key = "-".join(map(str, seq[i - 1:i + 1]))
        if key not in patterns:
            patterns[key] = [i]
        else:
            patterns[key].append(i)

    load = get_load(matrix)
    seq.append(load)

    if i == 999:
        break
# print(seq)
# print(patterns)

target = dict()
for k, v in patterns.items():
    if len(v) <= 1:
        continue
    diff = -1
    has_pattern = True
    for i in range(len(v) - 1):
        if diff == -1:
            diff = v[i + 1] - v[i]
        else:
            if diff != v[i + 1] - v[i]:
                has_pattern = False
                break
    if has_pattern:
        target[k] = diff
        print("find: ", k, diff)
        # break

diff_counter = Counter(target.values())
real_target = diff_counter.most_common()[0][0]
to_find_target = -1
for k, v in target.items():
    if v == real_target:
        to_find_target = k
        break

# print(patterns)
# raise Exception("stop")
cyclic_arr = seq[(patterns[to_find_target][0] - 1):(patterns[to_find_target][1] - 1)]
# print(cyclic_arr)
# print(len(cyclic_arr))
# print("----")

final_idx = (1000000000 - patterns[to_find_target][0] + 2) % len(cyclic_arr)
# print(final_idx)
print(cyclic_arr[final_idx + 1])
