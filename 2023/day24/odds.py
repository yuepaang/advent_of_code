from dataclasses import dataclass


# with open("./odds_input.txt", "r") as f:
with open("./test.txt", "r") as f:
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

print(hailstones)


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
for t in range(999):
    x_range = []
    for hailstone in hailstones:
        print(extract_plane(hailstone))

# from ortools.linear_solver import pywraplp
#
# # Create the solver, specifying the underlying solver to use.
# # Here we use SCIP, which is one of the solvers included with OR-Tools.
# solver = pywraplp.Solver.CreateSolver("SCIP")
#
# # Check if the solver is available before proceeding
# if not solver:
#     print("SCIP solver unavailable.")
#     exit(1)
#
# # Create the variables x and y.
# x = solver.IntVar(-solver.infinity(), solver.infinity(), "x")
# y = solver.IntVar(-solver.infinity(), solver.infinity(), "y")
# z = solver.IntVar(-solver.infinity(), solver.infinity(), "z")
# vx = solver.IntVar(-solver.infinity(), solver.infinity(), "vx")
# vy = solver.IntVar(-solver.infinity(), solver.infinity(), "vy")
# vz = solver.IntVar(-solver.infinity(), solver.infinity(), "vz")
# t = solver.IntVar(-solver.infinity(), solver.infinity(), "t")
#
# # Define the constraints.
# for i, hailstone in enumerate(hailstones):
#     solver.Add(
#         x + y + z + t * (vx + vy + vz)
#         == (hailstone.x + hailstone.y + hailstone.z)
#         + t * (hailstone.vx + hailstone.vy + hailstone.vz)
#     )
#     # solver.Add(vx + vy + vz == (hailstone.vx + hailstone.vy + hailstone.vz))
#     if hailstone.vx > 0:
#         solver.Add(x >= hailstone.x)
#     else:
#         solver.Add(x <= hailstone.x)
#
#     if hailstone.vy > 0:
#         solver.Add(y >= hailstone.y)
#     else:
#         solver.Add(y <= hailstone.y)
#
#     if hailstone.vz > 0:
#         solver.Add(z >= hailstone.z)
#     else:
#         solver.Add(z <= hailstone.z)
#
# # Define the objective function.
# # solver.Minimize(t)
#
# # Solve the problem and print the solution.
# status = solver.Solve()
#
# if status == pywraplp.Solver.OPTIMAL:
#     print("Solution:")
#     print("Objective value =", solver.Objective().Value())
#     print("x =", x.solution_value())
#     print("y =", y.solution_value())
#     print("z =", z.solution_value())
# elif status == pywraplp.Solver.FEASIBLE:
#     print("A potentially suboptimal solution was found.")
# else:
#     print("The problem does not have an optimal solution.")

# from gurobipy import GRB, Model
#
# # 创建模型
# m = Model("equation_solver")
#
# # 添加变量
# a = m.addVar(vtype=GRB.INTEGER, name="a")
# b = m.addVar(vtype=GRB.INTEGER, name="b")
# c = m.addVar(vtype=GRB.INTEGER, name="c")
# va = m.addVar(vtype=GRB.INTEGER, name="va")
# vb = m.addVar(vtype=GRB.INTEGER, name="vb")
# vc = m.addVar(vtype=GRB.INTEGER, name="vc")
# # ... 为其他变量重复添加变量 ...
#
# # 添加约束
# for i, hailstone in enumerate(hailstones):
#     m.addConstr(
#         a + b + c == (hailstone.x + hailstone.y + hailstone.z), f"constraint {i}"
#     )
#     m.addConstr(
#         va + vb + vc == (hailstone.vx + hailstone.vy + hailstone.vz), f"constraint v{i}"
#     )
#     if hailstone.vx > 0:
#         m.addConstr(a > hailstone.x, f"constraint x{i}")
#     else:
#         m.addConstr(a <= hailstone.x, f"constraint x{i}")
#
#     if hailstone.vy > 0:
#         m.addConstr(b > hailstone.y, f"constraint y{i}")
#     else:
#         m.addConstr(b <= hailstone.y, f"constraint y{i}")
#
#     if hailstone.vz > 0:
#         m.addConstr(c > hailstone.z, f"constraint z{i}")
#     else:
#         m.addConstr(c <= hailstone.z, f"constraint z{i}")
# # ... 为其他方程重复添加约束 ...
#
# # 定义目标函数（如果需要最小化或最大化某些表达式）
# # 这里我们没有具体的目标函数，因为我们只是寻找满足条件的解
#
# # 进行优化
# m.optimize()
#
# # 输出解
# if m.status == GRB.OPTIMAL:
#     print("Optimal solution found:")
#     for v in m.getVars():
#         print("%s = %g" % (v.varName, v.x))
# else:
#     print("No optimal solution found")
