from copy import deepcopy
import re
import operator

# with open("./test.txt", "r") as f:
with open("./apl_input.txt", "r") as f:
    lines = f.readlines()

decisions = {}
parts = []
is_second_part = False
for line in lines:
    line = line.strip()
    if line == "":
        is_second_part = True
        continue

    if not is_second_part:
        name, d = line.split("{")
        d = d.replace("}", "")
        value = []
        for item in d.split(","):
            value.append(item.split(":"))
        decisions[name] = value
    else:
        parts.append(
            {
                pair.split("=")[0]: int(pair.split("=")[1])
                for pair in line.strip("{}").split(",")
            }
        )

print(decisions)
print(parts)


def check(part, curr_instr, decisions):
    # For part 1, simply follow the instructions, and return the next possible instruction set
    for item in decisions[curr_instr]:
        if len(item) > 1:
            match = re.search(
                r"[<>]", item[0]
            )  # Figure out the operator from the string, and calculate
            match match.group():
                case "<":
                    op = operator.lt
                case ">":
                    op = operator.gt
            if op(part[item[0][0]], int(item[0][2:])):
                return item[1]
        else:
            return item[0]

total = 0
for part in parts:
    curr_instr = "in"
    while curr_instr not in ["R", "A"]:
        curr_instr = check(part, curr_instr, decisions)
    if curr_instr == "A":
        total += sum(part.values())

print(total)

def recursive_check(curr_in, curr_path, accepted, instructions):
    # Use recursion to find the values that allow for each successful path and return the list of accepted paths 
    for instr in instructions[curr_in]:
        if len(instr) > 1:
            first = deepcopy(curr_path)  # If going recursive, ensure you are making a copy of the current path
            first[instr[0][0]].append(instr[0][1:])  # Add the current path to the copy
            if instr[1] == 'R':  # For these, make sure to only pass so you don't skip the opposite path for the set
                pass
            elif instr[1] == 'A':
                accepted.append(first)
                pass
            else:  # If we haven't found an end, recurse
                accepted = recursive_check(instr[1], first, accepted, instructions)
            val = int(instr[0][2:])  # Don't forget to add the difference if you have to swap operators
            match instr[0][1]:
                case '>':
                    val += 1
                case '<': 
                    val -= 1
            sym = '<>'.replace(instr[0][1], '')  # Add the opposite operator to the number when swapping
            curr_path[instr[0][0]].append(''.join([sym, str(val)]))  # Add the path to the curr_path before performing the next instruction
        elif instr[0] == 'A':  # If you've hit the end of your instruction set, determine the next step
            accepted.append(curr_path)
            return accepted
        elif instr[0] == 'R':
            return accepted
        else:
            accepted = recursive_check(instr[0], curr_path, accepted, instructions)
    return accepted

path = {'x': [], 'm': [], 'a': [], 's': []}
accepted = recursive_check('in', deepcopy(path), [], decisions)
total = 0
count = 1
for line in accepted:
    curr_values = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]  # Start with the full possible value for each path
    for idx, char in enumerate(line):
        for item in line[char]:
            match item[0]:
                case '<':  # If the operator is less than, and the upper end of the range is greater, set the new upper limit
                    if int(item[1:]) < curr_values[idx][1]:
                        curr_values[idx][1] = int(item[1:]) - 1
                case '>': # If the operator is greater than, and the lower end of the range is lesser, set the new lower limit
                    if int(item[1:]) > curr_values[idx][0]:
                        curr_values[idx][0] = int(item[1:]) + 1
    t = 1  # Add the full possible values to the total
    for lo, hi in curr_values:
        t *= hi - lo + 1
    print(f"Accepted part {count} has {t} possible combinations")
    count += 1
    total += t
print(total)
