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
                    yield sep


def get_sep(springs, quantity_len, group_cache, format_cache):
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
                sep_len = [len(s) for s in sep]
                skip = any([s < q for s, q in zip(sep_len, quantity)])
                if skip:
                    continue
                replace_idx = []
                for i, s in enumerate(sep):
                    if count_spring(s) == quantity[i]:
                        replace_idx.append(i)
                for idx in replace_idx:
                    sep[idx] = sep[idx].replace("?", "")

                has_same_format = False
                for i, s in enumerate(sep):
                    if "#" not in s:
                        continue
                    if i in format_cache and s in format_cache[i]:
                        has_same_format = True and has_same_format
                    else:
                        has_same_format = False and has_same_format

                    if i not in format_cache:
                        format_cache[i] = set()
                    if s not in format_cache[i]:
                        format_cache[i].add(s)
                if has_same_format:
                    continue

                key = "&".join([str(len(s)) for s in sep])
                if key not in group_cache:
                    group_cache.add(key)
                    yield sep


def dig_unknown_spring(sep, quantity):
    total = 1
    if len(sep) == len(quantity):
        for i in range(len(sep)):
            spring_cnt = count_spring(sep[i])
            if spring_cnt < quantity[i]:
                total *= comb(len(sep[i]) - spring_cnt, quantity[i] - spring_cnt)
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
    one_cnt = 0
    group_cache = set()
    format_cache = dict()
    print(springs)
    print(quantity)
    for sep in get_sep(springs, len(quantity), group_cache, format_cache):
        print(sep)
        # one_cnt += dig_unknown_spring(sep, quantity)
        one_cnt += 1
    print("count: ", one_cnt)
    print("-----------")
    total += one_cnt

    # part one
    # one_cnt = 0
    # for sep in get_all(springs, len(quantity)):
    #     all_equal = True
    #     if len(sep) != len(quantity):
    #         raise Exception
    #     for i, s in enumerate(sep):
    #         if count_spring(s) != quantity[i]:
    #             all_equal = False
    #             break
    #     if all_equal:
    #         one_cnt += 1
    # print("count: ", one_cnt)
    # print("-----------")
    # total += one_cnt
print(total)
