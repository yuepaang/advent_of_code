import string
import re

from math import comb
from itertools import combinations

# with open("./test.txt", "r") as f:
with open("./hot_input.txt", "r") as f:
    lines = f.readlines()

letter = list(string.ascii_letters)

# a = re.finditer("\\?+", "??#?")
# for aa in a:
#     print(len(aa.group()))
#     print(aa.start())

# raise Exception


def count_spring(s):
    cnt = 0
    for c in s:
        # if c != "." and c != "?":
        if c == "#":
            cnt += 1
    return cnt


def get_all(springs, quantity_len):
    possible_idx = []
    for i, c in enumerate(springs):
        if c == "?":
            possible_idx.append(i)
    for n in range(0, len(possible_idx) + 1):
        if n == 0:
            new_spring = springs.replace("?", ".")
            sep = [s for s in new_spring.split(".") if s != ""]
            if len(sep) == quantity_len:
                yield sep
        else:
            replacement = list(combinations(possible_idx, n))
            for index_list in replacement:
                new_spring = [
                    "#" if i in index_list else s for i, s in enumerate(springs)
                ]
                new_spring = "".join(new_spring)
                new_spring = new_spring.replace("?", ".")
                sep = [s for s in new_spring.split(".") if s != ""]
                if len(sep) == quantity_len:
                    # print(springs)
                    # print(new_spring)
                    # print("------")
                    yield sep


def get_sep(springs, quantity_len):
    possible_idx = []
    for i, c in enumerate(springs):
        if c == "?":
            possible_idx.append(i)
    for n in range(0, len(possible_idx) + 1):
        if n == 0:
            sep = [s for s in springs.split(".") if s != ""]
            if len(sep) == quantity_len:
                yield sep
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
                    if "#" in sep[i] and len(re.findall("\\?+", sep[i])) > 1:
                        it = re.finditer("\\?+", sep[i])
                        for t in it:
                            sep[i] = sep[i].replace(t.group(), "?")
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
    # new_springs = []
    # for i, s in enumerate(springs):
    #     if s == "#":
    #         new_springs.append(letter[i])
    #     else:
    #         new_springs.append(s)
    # springs = "".join(new_springs)
    # sep = [s for s in springs.split(".") if s != ""]
    # print(springs)
    # print(quantity)
    # one_cnt = 0
    # cache = set()
    # for sep in get_sep(springs, len(quantity)):
    #     if available_spring(sep, quantity):
    #         if "&".join(sep) not in cache:
    #             print(sep)
    #         cache.add("&".join(sep))
    # one_cnt += len(cache)
    # total += one_cnt

    one_cnt = 0
    for sep in get_all(springs, len(quantity)):
        all_equal = True
        if len(sep) != len(quantity):
            raise Exception
        for i, s in enumerate(sep):
            if count_spring(s) != quantity[i]:
                all_equal = False
                break
        if all_equal:
            one_cnt += 1
    # print("count: ", one_cnt)
    # print("-----------")
    total += one_cnt
print(total)
