with open("./input.txt", "r") as f:
    lines = f.readlines()

s = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
i = ["o1ne", "t2wo", "t3hree", "f4our", "f5ive", "s6ix", "s7even", "e8ight", "n9ine"]

trans = dict()
for j in range(len(s)):
    trans[s[j]] = i[j]

regex = "|".join(s)

total = 0
for line in lines:
    line = line.strip()
    for k, v in trans.items():
        line = line.replace(k, v)

    l, r = 0, len(line) - 1
    a, b = 0, 0
    # print(line)
    # print(line[10].isdigit())
    find_l = False
    find_r = False
    while not (find_l and find_r):
        if line[l].isdigit():
            a = int(line[l])
            find_l = True
        else:
            l += 1

        if line[r].isdigit():
            b = int(line[r])
            find_r = True
        else:
            r -= 1
    total += a * 10 + b

print(total)
