def cal_sequence(nums):
    res = nums[-1]
    curr = [n for n in nums]
    head = [nums[0]]
    while any(curr):
        n = len(curr)
        diff = [curr[i + 1] - curr[i] for i in range(n - 1)]
        res += diff[-1]
        head.append(diff[0])
        curr = diff
    heading = 0
    for i in range(len(head) - 2, -1, -1):
        heading = head[i] - heading

    return res, heading


# with open(r"D:\Work\advent_of_code_2023\2023\day9\test.txt", "r") as f:
with open(r"D:\Work\advent_of_code_2023\2023\day9\mirage_input.txt", "r") as f:
    # with open("mirage_input.txt", "r") as f:
    # with open("./test.txt", "r") as f:
    lines = f.readlines()

total = 0
new_total = 0
for line in lines:
    nums = [int(n) for n in line.strip().split(" ")]
    t, nt = cal_sequence(nums)
    total += t
    new_total += nt
    # print(sequences)
    # print(predict_value(nums, sequences))
    # if nums[0] < 0:
    #     raise Exception("stop")

print(total)
print(new_total)
