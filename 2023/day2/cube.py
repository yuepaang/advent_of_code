with open("./cube_input.txt", "r") as f:
    lines = f.readlines()

# conf = {
#     "red": 12,
#     "green": 13,
#     "blue": 14,
# }

# total = 0
# for line in lines:
#     line = line.strip()
#     game, plays = line.split(": ")
#     game_id = int(game.split(" ")[1])
#     # print(game_id)
#     # print(plays)
#     plays_list = plays.split("; ")
#     # print(plays_list)
#     not_possible = False
#     for play in plays_list:
#         if not_possible:
#             break
#         for color_cnt in play.split(", "):
#             num, color = color_cnt.split(" ")
#             num = int(num)
#             # print(num, color)
#             if num > conf[color]:
#                 not_possible = True
#                 break
#     # print(not_possible)
#     if not not_possible:
#         total += game_id

# print(total)

total = 0
for line in lines:
    line = line.strip()
    game, plays = line.split(": ")
    game_id = int(game.split(" ")[1])
    plays_list = plays.split("; ")
    blue, red, green = 0, 0, 0
    for play in plays_list:
        for color_cnt in play.split(", "):
            num, color = color_cnt.split(" ")
            num = int(num)
            if color == "blue":
                blue = max(blue, num)
            elif color == "green":
                green = max(green, num)
            if color == "red":
                red = max(red, num)
    total += blue * red * green

print(total)
