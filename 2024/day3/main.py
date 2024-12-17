import re

with open(r"D:\Work\advent_of_code_2023\2024\day3\input.txt", "r") as f:
    # with open(r"D:\Work\advent_of_code_2023\2024\day3\eg2.txt", "r") as f:
    lines = f.readlines()


def part_one():
    res = 0
    for line in lines:
        # print(line)
        g = re.findall(r"mul\(\d+,\d+\)", line)
        for x in g:
            a, b = x.replace("mul(", "").replace(")", "").split(",")
            res += int(a) * int(b)
    print(res)


part_one()


def part_two():
    res = 0
    is_dont = False
    one_line = ["".join(lines)]

    for line in one_line:
        do_idx, dont_idx = [], []
        for match in re.finditer(r"do\(\)", line):
            g = match.group()
            start_index = match.start()
            end_index = match.end()
            do_idx.append(end_index)
        for match in re.finditer(r"don\'t\(\)", line):
            g = match.group()
            start_index = match.start()
            end_index = match.end()
            dont_idx.append(end_index)

        flag_idx = []
        for _ in range(len(do_idx + dont_idx)):
            if do_idx and dont_idx:
                if do_idx[0] < dont_idx[0]:
                    flag_idx.append((do_idx.pop(0), False))
                else:
                    flag_idx.append((dont_idx.pop(0), True))
            elif do_idx:
                flag_idx.append((do_idx.pop(0), False))
            elif dont_idx:
                flag_idx.append((dont_idx.pop(0), True))

        for match in re.finditer(r"mul\(\d+,\d+\)", line):
            g = match.group()
            start_index = match.start()
            end_index = match.end()

            # dont after current
            if flag_idx and end_index > flag_idx[0][0]:
                is_dont = flag_idx[0][1]
                flag_idx.pop(0)

            if not is_dont:
                a, b = g.replace("mul(", "").replace(")", "").split(",")
                # print(f"{a}*{b}")
                res += int(a) * int(b)

    print(res)


part_two()
