from dataclasses import dataclass

with open("./seed_input.txt", "r") as f:
    # with open("./test2.txt", "r") as f:
    lines = f.readlines()

lines.append("stop")

# seeds = []
# seed_to_soil = dict()
# soil_to_fertilizer = dict()
# fertilizer_to_water = dict()
# water_to_light = dict()
# light_to_temperature = dict()
# temperature_to_humidity = dict()
# humidity_to_location = dict()
# m1, m2, m3, m4, m5, m6, m7 = False, False, False, False, False, False, False
# for i, line in enumerate(lines):
#     line = line.strip()
#     # print(line)
#     # some initializations
#     if i == 0:
#         line = line.split(": ")[1]
#         # Part One
#         seeds = [int(s) for s in line.split(" ")]
#         # PERF: large seeds
#         # Part Two
#         # new_seeds = []
#         # for n_pair in range(len(seeds) // 2):
#         #     start_seed = seeds[2 * n_pair]
#         #     seed_num = seeds[2 * n_pair + 1]
#         #     new_seeds.extend([start_seed + i for i in range(seed_num)])
#         # seeds = new_seeds
#         seed_to_soil = {i: i for i in seeds}
#     elif line == "":
#         if m1:
#             soil_to_fertilizer = {i: i for i in seed_to_soil.values()}
#         if m2:
#             fertilizer_to_water = {i: i for i in soil_to_fertilizer.values()}
#         if m3:
#             water_to_light = {i: i for i in fertilizer_to_water.values()}
#         if m4:
#             light_to_temperature = {i: i for i in water_to_light.values()}
#         if m5:
#             temperature_to_humidity = {i: i for i in light_to_temperature.values()}
#         if m6:
#             humidity_to_location = {i: i for i in temperature_to_humidity.values()}

#         m1, m2, m3, m4, m5, m6, m7 = False, False, False, False, False, False, False
#         continue
#     elif line.startswith("seed-to-soil"):
#         m1 = True
#         continue
#     elif line.startswith("soil-to-fertilizer"):
#         m2 = True
#         continue
#     elif line.startswith("fertilizer-to-water"):
#         m3 = True
#         continue
#     elif line.startswith("water-to-light"):
#         m4 = True
#         continue
#     elif line.startswith("light-to-temperature"):
#         m5 = True
#         continue
#     elif line.startswith("temperature-to-humidity"):
#         m6 = True
#         continue
#     elif line.startswith("humidity-to-location"):
#         m7 = True
#         continue

#     # overwrite mappings
#     if m1:
#         d, o, step = [int(s) for s in line.split(" ")]
#         for seed in seeds:
#             if o <= seed < o + step:
#                 delta = seed - o
#                 seed_to_soil[seed] = d + delta
#     elif m2:
#         d, o, step = [int(s) for s in line.split(" ")]
#         for soil in seed_to_soil.values():
#             if o <= soil < o + step:
#                 delta = soil - o
#                 soil_to_fertilizer[soil] = d + delta
#     elif m3:
#         d, o, step = [int(s) for s in line.split(" ")]
#         for f in soil_to_fertilizer.values():
#             if o <= f < o + step:
#                 delta = f - o
#                 fertilizer_to_water[f] = d + delta
#     elif m4:
#         d, o, step = [int(s) for s in line.split(" ")]
#         for w in fertilizer_to_water.values():
#             if o <= w < o + step:
#                 delta = w - o
#                 water_to_light[w] = d + delta
#     elif m5:
#         d, o, step = [int(s) for s in line.split(" ")]
#         for li in water_to_light.values():
#             if o <= li < o + step:
#                 delta = li - o
#                 light_to_temperature[li] = d + delta
#     elif m6:
#         d, o, step = [int(s) for s in line.split(" ")]
#         for t in light_to_temperature.values():
#             if o <= t < o + step:
#                 delta = t - o
#                 temperature_to_humidity[t] = d + delta
#     elif m7:
#         d, o, step = [int(s) for s in line.split(" ")]
#         for h in temperature_to_humidity.values():
#             if o <= h < o + step:
#                 delta = h - o
#                 humidity_to_location[h] = d + delta


# def get_location(seed):
#     soil = seed_to_soil[seed]
#     fertilizer = soil_to_fertilizer[soil]
#     water = fertilizer_to_water[fertilizer]
#     light = water_to_light[water]
#     temperature = light_to_temperature[light]
#     humidity = temperature_to_humidity[temperature]
#     location = humidity_to_location[humidity]
#     return location


# locations = [get_location(seed) for seed in seeds]
# print(min(locations))

# PART TWO
@dataclass
class VecRange:
    start: int
    length: int


def convert(source, o, d, step):
    if o <= source < o + step:
        return source - o + d
    return -1


def get_ranges(seed_num, input_ranges, mappings):
    if len(mappings) == 0:
        return input_ranges
    res = [[] for _ in range(seed_num)]
    for i in range(seed_num):
        for vr in input_ranges[i]:
            # print(vr, o, d, step)
            # vec range -> Vec<VecRange>
            slice = []
            range_end = vr.start + vr.length
            for o, d, step in mappings:
                source_end = o + step
                if range_end < o or vr.start > source_end:
                    continue

                if vr.start < o:
                    if o not in slice:
                        slice.append(o)
                if source_end < range_end:
                    if source_end not in slice:
                        slice.append(source_end)

            if range_end not in slice:
                slice.append(range_end)
            current = vr.start
            for pos in slice:
                target_start = -1
                for o, d, step in mappings:
                    if target_start == -1:
                        target_start = convert(current, o, d, step)
                if target_start != -1:
                    res[i].append(VecRange(target_start, pos - current))
                else:
                    res[i].append(VecRange(current, pos - current))
                current = pos
    return res


new_seeds = []
mappings = []
for i, line in enumerate(lines):
    line = line.strip()
    # some initializations
    if i == 0:
        line = line.split(": ")[1]
        # Part One
        seeds = [int(s) for s in line.split(" ")]
        # Part Two
        new_seeds = []
        for n_pair in range(len(seeds) // 2):
            start_seed = seeds[2 * n_pair]
            seed_num = seeds[2 * n_pair + 1]
            new_seeds.append([VecRange(start_seed, seed_num)])
        print("origin", new_seeds)
    elif line == "":
        continue
    elif not line[0].isdigit():
        # print(mappings)
        new_seeds = get_ranges(len(new_seeds), new_seeds, mappings)
        # print("mapping", new_seeds)
        # print()
        mappings = []
        continue
    else:
        d, o, step = [int(s) for s in line.split(" ")]
        mappings.append((o, d, step))

# print(new_seeds)
min_loc = float("inf")
for seed in new_seeds:
    for r in seed:
        if r.start < min_loc:
            # print(r)
            min_loc = r.start
print(min_loc)
