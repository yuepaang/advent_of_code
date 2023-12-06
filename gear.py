import re
from collections import defaultdict

# with open("./test.txt", "r") as f:
with open("./gear_input.txt", "r") as f:
    lines = f.readlines()

index_map = []
symbols = []
for i, line in enumerate(lines):
    line = line.strip()
    is_new_number = False
    new_number = ""
    for j, segment in enumerate(line):
        if segment == ".":
            continue
        elif segment.isdigit():
            continue
        else:
            symbols.append((i, j, segment))
    for match in re.finditer(r"\d+", line):
        number = int(match.group())
        index_map.append((i, match.start(), match.end(), number))

# print(index_map)
# print(symbols)

total = 0
gear = defaultdict(list)
for symbols_idx in symbols:
    for number_idx in index_map:
        number = number_idx[3]
        if abs(number_idx[0] - symbols_idx[0]) > 1:
            continue
        number_range = list(range(number_idx[1] - 1, number_idx[2] + 1))
        # print(number, number_idx)
        # print(number_range)
        if symbols_idx[1] in number_range:
            if symbols_idx[2] == "*":
                gear[(symbols_idx[0], symbols_idx[1])].append(number)
            total += number

total = 0
for key, value in gear.items():
    if len(value) > 1:
        print(value)
        product = 1
        for n in value:
            product *= n
            # total -= n
        total += product
print(total)
