with open("./cosmic_input.txt", "r") as f:
# with open("./test.txt", "r") as f:
    lines = f.readlines()

col_expand_idx = set(list(range(len(lines[0].strip()))))
for j, line in enumerate(lines):
    line = line.strip()
    for i, char in enumerate(line):
        if char == "#":
            col_expand_idx.discard(i)

# Part 1
# margin = 1
# Part 2
margin = 999999
galaxy = []
row_expand_cnt = 0
for j, line in enumerate(lines):
    line = line.strip()
    col_expand_cnt = 0
    for i, char in enumerate(line):
        if i in col_expand_idx:
            col_expand_cnt += margin
        if char == "#":
            galaxy.append((i + col_expand_cnt, j + row_expand_cnt))
    if "#" not in line:
        row_expand_cnt += margin


total = 0
for i in range(len(galaxy)):
    for j in range(i + 1, len(galaxy)):
        total += abs(galaxy[i][0] - galaxy[j][0]) + abs(galaxy[i][1] - galaxy[j][1])
print(total)
