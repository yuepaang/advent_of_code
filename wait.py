import re

with open("./wait_input.txt", "r") as f:
    # with open("./test.txt", "r") as f:
    lines = f.readlines()

time_list = []
dist_list = []
for line in lines:
    line = line.strip()
    for match in re.finditer(r"\d+", line):
        number = int(match.group())
        if line.startswith("Time"):
            time_list.append(number)
        elif line.startswith("Distance"):
            dist_list.append(number)

one_t = "".join([str(t) for t in time_list])
one_d = "".join([str(d) for d in dist_list])
time_list = [int(one_t)]
dist_list = [int(one_d)]


race_cnt = len(time_list)

total = 1
for race_idx in range(race_cnt):
    t = time_list[race_idx]
    dist = dist_list[race_idx]
    left, right = 0, t // 2
    while left < right:
        mid = (left + right) // 2
        race_dist = mid * (t - mid)
        if race_dist <= dist:
            left = mid + 1
        else:
            right = mid
    total *= t - (2 * left) + 1

print(total)
