from collections import OrderedDict
with open("./lens_input.txt", "r") as f:
    lines = f.readlines()


def hash_func(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res


print(hash_func("HASH"))
segments = lines[0].strip().split(",")

print(sum([hash_func(seg) for seg in segments]))

print(hash_func("cm"))
boxes = [OrderedDict() for _ in range(256)]

for seg in segments:
    if "=" in seg:
        label, length = seg.split("=")
        boxes[hash_func(label)][label] = length
    elif "-" in seg:
        label = seg.split("-")[0]
        if label in boxes[hash_func(label)]:
            del boxes[hash_func(label)][label]

total = 0
for i, d in enumerate(boxes):
    cnt = 1
    for k, v in d.items():
        total += (i + 1) * cnt * int(v)
        cnt += 1

print(total)
