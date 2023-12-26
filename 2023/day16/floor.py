# with open("./test.txt", "r") as f:
with open("./floor_input.txt", "r") as f:
    lines = f.readlines()

layout = []
for line in lines:
    row = []
    line = line.strip()
    for c in line:
        row.append(c)
    layout.append(row)

print("x: ", len(layout))
print("y: ", len(layout[0]))


class Beam(object):
    def __init__(self, x, y, direction="R"):
        self.curr = (x, y)
        self.next = get_next_pos(self.curr, direction)
        self.stop = False
        self.direction = direction


def get_next_pos(pos, direction):
    if direction == "R":
        return (pos[0], pos[1] + 1)
    elif direction == "L":
        return (pos[0], pos[1] - 1)
    elif direction == "U":
        return (pos[0] - 1, pos[1])
    elif direction == "D":
        return (pos[0] + 1, pos[1])
    return None


def is_out_of_bound(pos):
    x, y = pos
    if x < 0 or x >= len(layout):
        return True
    if y < 0 or y >= len(layout[0]):
        return True
    return False


def energize(start):
    beams = [start]
    visited = set()
    step = 0
    while beams:
        step += 1
        new_beams = []
        for b in beams:
            visited.add((b.curr[0], b.curr[1], b.direction))
            x, y = b.curr

            if layout[x][y] == ".":
                b.curr = get_next_pos(b.curr, b.direction)
                b.next = get_next_pos(b.curr, b.direction)
            elif layout[x][y] == "|":
                if b.direction == "R" or b.direction == "L":
                    new_pos = get_next_pos(b.curr, "D")

                    b.curr = get_next_pos(b.curr, "U")
                    b.next = get_next_pos(b.curr, "U")
                    b.direction = "U"

                    new_beam = Beam(new_pos[0], new_pos[1])
                    new_beam.next = get_next_pos(new_pos, "D")
                    new_beam.direction = "D"
                    new_beams.append(new_beam)
                elif b.direction == "U" or b.direction == "D":
                    b.curr = get_next_pos(b.curr, b.direction)
                    b.next = get_next_pos(b.curr, b.direction)
            elif layout[x][y] == "-":
                if b.direction == "U" or b.direction == "D":
                    new_pos = get_next_pos(b.curr, "L")

                    b.curr = get_next_pos(b.curr, "R")
                    b.next = get_next_pos(b.curr, "R")
                    b.direction = "R"

                    new_beam = Beam(new_pos[0], new_pos[1])
                    new_beam.next = get_next_pos(new_pos, "L")
                    new_beam.direction = "L"
                    new_beams.append(new_beam)
                elif b.direction == "R" or b.direction == "L":
                    b.curr = get_next_pos(b.curr, b.direction)
                    b.next = get_next_pos(b.curr, b.direction)
            elif layout[x][y] == "/":
                if b.direction == "R":
                    b.curr = get_next_pos(b.curr, "U")
                    b.next = get_next_pos(b.curr, "U")
                    b.direction = "U"
                elif b.direction == "D":
                    b.curr = get_next_pos(b.curr, "L")
                    b.next = get_next_pos(b.curr, "L")
                    b.direction = "L"
                elif b.direction == "L":
                    b.curr = get_next_pos(b.curr, "D")
                    b.next = get_next_pos(b.curr, "D")
                    b.direction = "D"
                elif b.direction == "U":
                    b.curr = get_next_pos(b.curr, "R")
                    b.next = get_next_pos(b.curr, "R")
                    b.direction = "R"
            elif layout[x][y] == "\\":
                if b.direction == "R":
                    b.curr = get_next_pos(b.curr, "D")
                    b.next = get_next_pos(b.curr, "D")
                    b.direction = "D"
                elif b.direction == "D":
                    b.curr = get_next_pos(b.curr, "R")
                    b.next = get_next_pos(b.curr, "R")
                    b.direction = "R"
                elif b.direction == "L":
                    b.curr = get_next_pos(b.curr, "U")
                    b.next = get_next_pos(b.curr, "U")
                    b.direction = "U"
                elif b.direction == "U":
                    b.curr = get_next_pos(b.curr, "L")
                    b.next = get_next_pos(b.curr, "L")
                    b.direction = "L"

        beams.extend(new_beams)
        beams = [
            b
            for b in beams
            if (b.curr[0], b.curr[1], b.direction) not in visited
            and not is_out_of_bound(b.curr)
        ]

    new_visited = set()
    for x, y, _ in visited:
        new_visited.add((x, y))

    # for x, line in enumerate(layout):
    #     print(
    #         "".join([c if (x, y) not in new_visited else "#" for y, c in enumerate(line)])
    #     )
    return len(new_visited)


# Part one
# start = Beam(0, 0)
# print(energize(start))

top_beams = [Beam(0, i, "D") for i in range(len(layout[0]))]
bottom_beams = [Beam(len(layout) - 1, i, "U") for i in range(len(layout[0]))]
left_beams = [Beam(i, 0, "R") for i in range(len(layout))]
right_beams = [Beam(i, len(layout[0]) - 1, "L") for i in range(len(layout))]

top_energies = [energize(b) for b in top_beams]
bottom_energies = [energize(b) for b in bottom_beams]
left_energies = [energize(b) for b in left_beams]
right_energies = [energize(b) for b in right_beams]
print(max(top_energies))
print(max(bottom_energies))
print(max(left_energies))
print(max(right_energies))
