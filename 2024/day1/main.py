# with open(r"D:\Work\advent_of_code_2023\2024\day1\eg.txt", "r") as f:
with open(r"D:\Work\advent_of_code_2023\2024\day1\input.txt", "r") as f:
    lines = f.readlines()

left, right = [], []
for line in lines:
    l, r = line.strip().split("   ")
    left.append(int(l))
    right.append(int(r))


def part_one():
    # part one
    left.sort()
    right.sort()
    # print(left)
    # print(right)
    total_dist = 0
    for i in range(len(right)):
        total_dist += abs(right[i] - left[i])
    print(total_dist)


# part_one()


def part_two():
    c = {}
    for n in right:
        if n in c:
            c[n] += 1
        else:
            c[n] = 1

    total_dist = 0
    for n in left:
        total_dist += c.get(n, 0) * n
    print(total_dist)


part_two()
