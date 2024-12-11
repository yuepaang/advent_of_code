with open(r"D:\Work\advent_of_code_2023\2024\day2\input.txt", "r") as f:
    # with open(r"D:\Work\advent_of_code_2023\2024\day2\eg.txt", "r") as f:
    lines = f.readlines()

reports = []
for line in lines:
    reports.append([int(x) for x in line.strip().split(" ")])


def part_one():
    res = 0

    def is_safe(x):
        flag = None
        for i in range(1, len(x)):
            adj_diff = x[i] - x[i - 1]
            if i == 1:
                flag = (adj_diff) > 0
            else:
                if (adj_diff > 0) != flag:
                    return False
            if abs(adj_diff) < 1 or abs(adj_diff) > 3:
                return False
        return True

    for report in reports:
        if is_safe(report):
            # print(report)
            res += 1

    print(res)


# part_one()


def part_two():
    res = 0

    def is_safe(x):
        flag = None
        for i in range(1, len(x)):
            adj_diff = x[i] - x[i - 1]
            if i == 1:
                flag = (adj_diff) > 0
            else:
                if (adj_diff > 0) != flag:
                    return False
            if abs(adj_diff) < 1 or abs(adj_diff) > 3:
                return False
        return True

    for report in reports:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i + 1 :]):
                # print(report)
                res += 1
                break
    print(res)


part_two()
