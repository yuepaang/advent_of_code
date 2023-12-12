from math import comb
from itertools import combinations

# with open(r"D:\Work\advent_of_code_2023\2023\day12\test.txt", "r") as f:
with open(r"D:\Work\advent_of_code_2023\2023\day12\hot_input.txt", "r") as f:
    lines = f.readlines()


def count_spring(s):
    cnt = 0
    for c in s:
        if c == "#":
            cnt += 1
    return cnt


def get_sep(springs, quantity_len):
    possible_idx = []
    for i, c in enumerate(springs):
        if c == "?":
            possible_idx.append(i)
    for n in range(0, len(possible_idx) + 1):
        if n == 0:
            yield [s for s in springs.split(".") if s != ""]
            continue
        replacement = list(combinations(possible_idx, n))
        for index_list in replacement:
            new_spring = [
                s if i not in index_list else "." for i, s in enumerate(springs)
            ]
            new_spring = "".join(new_spring)
            sep = [s for s in new_spring.split(".") if s != ""]
            if len(sep) == quantity_len:
                for i, s in enumerate(sep):
                    if count_spring(s) == quantity[i]:
                        sep[i] = sep[i].replace("?", "")
                yield sep


def dig_unknown_spring(sep, quantity):
    total = 1
    if len(sep) == len(quantity):
        for i in range(len(sep)):
            sprint_cnt = count_spring(sep[i])
            if sprint_cnt == quantity[i]:
                continue
            elif sprint_cnt < quantity[i]:
                total *= comb(len(sep[i]) - sprint_cnt, quantity[i] - sprint_cnt)
    return total


def available_spring(sep, quantity):
    for i in range(len(sep)):
        if len(sep[i]) < quantity[i]:
            return False
        sprint_cnt = count_spring(sep[i])
        if sprint_cnt > quantity[i]:
            return False
    return True


total = 0
for line in lines:
    line = line.strip()
    springs, tmp = line.split(" ")
    quantity = [int(t) for t in tmp.split(",")]
    # sep = [s for s in springs.split(".") if s != ""]
    print(springs)
    # print(sep)
    print(quantity)
    one_cnt = 0
    cache = set()
    for sep in get_sep(springs, len(quantity)):
        if available_spring(sep, quantity):
            if "&".join(sep) not in cache:
                print(sep)
            cache.add("&".join(sep))
        # one_cnt += dig_unknown_spring(sep, quantity)
        # print("number", dig_unknown_spring(sep, quantity))
    one_cnt += len(cache)
    total += one_cnt
    print("count: ", one_cnt)
    print("-----------")
    break
print(total)
