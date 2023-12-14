with open("./point_input.txt", "r") as f:
    lines = f.readlines()

lines.append("")
patterns = []
rows = []
switch = False
for line in lines:
    line = line.strip()
    if line == "":
        patterns.append(rows)
        rows = []
        continue

    segments = []
    for c in line:
        segments.append(c)
    rows.append(segments)


def find_col(p):
    col_mirror = []
    for c in range(0, len(p[0]) - 1):
        is_reflection = True
        for r in range(len(p)):
            count = min(c + 1, len(p[0]) - c - 1)
            for i, j in zip(range(c, c - count, -1), range(c + 1, c + 1 + count)):
                if p[r][i] != p[r][j]:
                    is_reflection = False
                    break
            else:
                continue
            break
        if is_reflection:
            col_mirror.append(c)
            # break
    return col_mirror


def find_row(p):
    row_mirror = []
    for c in range(0, len(p) - 1):
        is_reflection = True
        for r in range(len(p[0])):
            count = min(c + 1, len(p) - c - 1)
            for i, j in zip(range(c, c - count, -1), range(c + 1, c + 1 + count)):
                if p[i][r] != p[j][r]:
                    is_reflection = False
                    break
            else:
                continue
            break
        if is_reflection:
            row_mirror.append(c)
            # break

    return row_mirror


total = 0
for i, p in enumerate(patterns):
    cols = find_col(p)
    rows = find_row(p)
    if not cols and not rows:
        print(p)
        raise Exception("No mirror")
    if cols:
        # print(p)
        # print("c", i, cols)
        for c in cols:
            total += c + 1
    if rows:
        # print(p)
        # print("r", i, rows)
        for r in rows:
            total += 100 * (r + 1)
print(total)


# part two
def find_col_new(p):
    col_mirror = []
    for c in range(0, len(p[0]) - 1):
        is_reflection = True
        replace_cnt = 0
        for r in range(len(p)):
            count = min(c + 1, len(p[0]) - c - 1)
            for i, j in zip(range(c, c - count, -1), range(c + 1, c + 1 + count)):
                if p[r][i] != p[r][j]:
                    if replace_cnt == 1:
                        is_reflection = False
                        break
                    else:
                        replace_cnt += 1
            else:
                continue
            break
        if is_reflection and replace_cnt == 1:
            col_mirror.append(c)
            # break
    return col_mirror


def find_row_new(p):
    row_mirror = []
    for c in range(0, len(p) - 1):
        is_reflection = True
        replace_cnt = 0
        for r in range(len(p[0])):
            count = min(c + 1, len(p) - c - 1)
            for i, j in zip(range(c, c - count, -1), range(c + 1, c + 1 + count)):
                if p[i][r] != p[j][r]:
                    if replace_cnt == 1:
                        is_reflection = False
                        break
                    else:
                        replace_cnt += 1
            else:
                continue
            break
        if is_reflection and replace_cnt == 1:
            row_mirror.append(c)
            # break

    return row_mirror


total = 0
for i, p in enumerate(patterns):
    cols = find_col_new(p)
    rows = find_row_new(p)
    if not cols and not rows:
        print(p)
        raise Exception("No mirror")
    if cols:
        # print(p)
        # print("c", i, cols)
        for c in cols:
            total += c + 1
    if rows:
        # print(p)
        # print("r", i, rows)
        for r in rows:
            total += 100 * (r + 1)
print(total)
