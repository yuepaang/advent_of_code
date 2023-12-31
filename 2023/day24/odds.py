from dataclasses import dataclass

import numpy as np


with open("./odds_input.txt", "r") as f:
    # with open("./test.txt", "r") as f:
    lines = f.readlines()


@dataclass
class Hailstone:
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int


hailstones = []
for line in lines:
    line = line.strip()
    p, v = line.split(" @ ")
    px, py, pz = p.split(", ")
    vx, vy, vz = v.split(", ")
    hailstones.append(Hailstone(int(px), int(py), int(pz), int(vx), int(vy), int(vz)))

# print(hailstones)


def extract_line(hailstone):
    p0 = (hailstone.x, hailstone.y)
    p1 = (hailstone.x + hailstone.vx, hailstone.y + hailstone.vy)
    a = (p0[1] - p1[1]) / (p0[0] - p1[0])
    b = p0[1] - a * p0[0]

    return (a, b)


def extract_intersection(line1, line2):
    a1, b1 = line1
    a2, b2 = line2
    if a1 == a2:
        return None, None
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return (x, y)


def extract_plane(hailstone):
    p0 = (hailstone.x, hailstone.y, hailstone.z)
    p1 = (
        hailstone.x + hailstone.vx,
        hailstone.y + hailstone.vy,
        hailstone.z + hailstone.vz,
    )
    p2 = (
        hailstone.x + hailstone.vx + hailstone.vx,
        hailstone.y + hailstone.vy + hailstone.vy,
        hailstone.z + hailstone.vz + hailstone.vz,
    )
    print(p0, p1, p2)
    a1 = p1[0] - p0[0]
    b1 = p1[1] - p0[1]
    c1 = p1[2] - p0[2]
    a2 = p2[0] - p0[0]
    b2 = p2[1] - p0[1]
    c2 = p2[2] - p0[2]

    print(a1, b1, c1)
    print(a2, b2, c2)
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = -a * p0[0] - b * p0[1] - c * p0[2]

    return (a, b, c, d)


# Part one
# lines = [extract_line(hailstone) for hailstone in hailstones]
# total = 0
# for i in range(len(lines)):
#     for j in range(i + 1, len(lines)):
#         x, y = extract_intersection(lines[i], lines[j])
#         if x is None or y is None:
#             continue
#         m = hailstones[i]
#         n = hailstones[j]
#         if m.vx < 0:
#             if x > m.x:
#                 continue
#         else:
#             if x < m.x:
#                 continue
#         if n.vx < 0:
#             if x > n.x:
#                 continue
#         else:
#             if x < n.x:
#                 continue
#         print((x, y))
#         print("---------")
#         if 2e14 < x < 4e14 and 2e14 < y < 4e14:
#         # if 7 < x < 27 and 7 < y < 27:
#             total += 1
# print(total)

# Part two
# t_i*v_i + d_i = t_i*v_rock + d_rock
# t_i*(v_i - v_rock) = d_rock - d_i
# (v_i - v_rock) x (d_rock - d_i) = 0
coef = [
    [
        hailstones[1].vy - hailstones[0].vy,
        hailstones[0].vx - hailstones[1].vx,
        0,
        hailstones[0].y - hailstones[1].y,
        hailstones[1].x - hailstones[0].x,
        0,
    ],
    [
        hailstones[2].vy - hailstones[0].vy,
        hailstones[0].vx - hailstones[2].vx,
        0,
        hailstones[0].y - hailstones[2].y,
        hailstones[2].x - hailstones[0].x,
        0,
    ],
    [
        hailstones[1].vz - hailstones[0].vz,
        0,
        hailstones[0].vx - hailstones[1].vx,
        hailstones[0].z - hailstones[1].z,
        0,
        hailstones[1].x - hailstones[0].x,
    ],
    [
        hailstones[2].vz - hailstones[0].vz,
        0,
        hailstones[0].vx - hailstones[2].vx,
        hailstones[0].z - hailstones[2].z,
        0,
        hailstones[2].x - hailstones[0].x,
    ],
    [
        0,
        hailstones[1].vz - hailstones[0].vz,
        hailstones[0].vy - hailstones[1].vy,
        0,
        hailstones[0].z - hailstones[1].z,
        hailstones[1].y - hailstones[0].y,
    ],
    [
        0,
        hailstones[2].vz - hailstones[0].vz,
        hailstones[0].vy - hailstones[2].vy,
        0,
        hailstones[0].z - hailstones[2].z,
        hailstones[2].y - hailstones[0].y,
    ],
]

A = np.array(coef)
print(A)
b = np.array(
    [
        (hailstones[0].y * hailstones[0].vx - hailstones[1].y * hailstones[1].vx)
        - (hailstones[0].x * hailstones[0].vy - hailstones[1].x * hailstones[1].vy),
        (hailstones[0].y * hailstones[0].vx - hailstones[2].y * hailstones[2].vx)
        - (hailstones[0].x * hailstones[0].vy - hailstones[2].x * hailstones[2].vy),
        (hailstones[0].z * hailstones[0].vx - hailstones[1].z * hailstones[1].vx)
        - (hailstones[0].x * hailstones[0].vz - hailstones[1].x * hailstones[1].vz),
        (hailstones[0].z * hailstones[0].vx - hailstones[2].z * hailstones[2].vx)
        - (hailstones[0].x * hailstones[0].vz - hailstones[2].x * hailstones[2].vz),
        (hailstones[0].z * hailstones[0].vy - hailstones[1].z * hailstones[1].vy)
        - (hailstones[0].y * hailstones[0].vz - hailstones[1].y * hailstones[1].vz),
        (hailstones[0].z * hailstones[0].vy - hailstones[2].z * hailstones[2].vy)
        - (hailstones[0].y * hailstones[0].vz - hailstones[2].y * hailstones[2].vz),
    ]
)
print(b)
x = np.linalg.solve(A, b)
print(int(sum(x[:3])))
