import re
from collections import defaultdict

with open("./scratch_input.txt", "r") as f:
    # with open("./test.txt", "r") as f:
    lines = f.readlines()

# total = 0
# for line in lines:
#     line = line.strip()
#     line = line.split(": ")[1]
#     winning_numbers = line.split(" | ")[0]
#     own_numbers = line.split(" | ")[1]
#     winning_set = set()
#     for match in re.finditer(r"\d+", winning_numbers):
#         number = int(match.group())
#         winning_set.add(number)
#     num_cnt = -1
#     for match in re.finditer(r"\d+", own_numbers):
#         number = int(match.group())
#         if number in winning_set:
#             num_cnt += 1
#     if num_cnt >= 0:
#         total += 2**num_cnt

# print(total)

total = defaultdict(int)
for i, line in enumerate(lines):
    i += 1
    line = line.strip()
    line = line.split(": ")[1]
    winning_numbers = line.split(" | ")[0]
    own_numbers = line.split(" | ")[1]
    winning_set = set()
    for match in re.finditer(r"\d+", winning_numbers):
        number = int(match.group())
        winning_set.add(number)

    num_cnt = 0
    for match in re.finditer(r"\d+", own_numbers):
        number = int(match.group())
        if number in winning_set:
            num_cnt += 1

    # copies -> copies
    for _ in range(total[i]):
        for j in range(i + 1, i + 1 + num_cnt):
            total[j] += 1

    # original
    total[i] += 1

    # copies
    for j in range(i + 1, i + 1 + num_cnt):
        total[j] += 1

print(sum(total.values()))
