from functools import cmp_to_key
from collections import Counter

# with open("./day7.txt", "r") as f:
with open("./camel_input.txt", "r") as f:
    # with open("./test.txt", "r") as f:
    lines = f.readlines()

num = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_rank = {n: len(num) - i for i, n in enumerate(num)}


def counter(card):
    counter = {}
    for c in card:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter


def stupid_compare(x, y):
    x = x[1]
    y = y[1]
    if 5 in x.values() and 5 not in y.values():
        return 1
    elif 5 not in x.values() and 5 in y.values():
        return -1
    elif 5 in x.values() and 5 in y.values():
        a, b = 0, 0
        for k, v in x.items():
            if v == 5:
                a = card_rank[k]
        for k, v in y.items():
            if v == 5:
                b = card_rank[k]
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0
    elif 4 in x.values() and 4 not in y.values():
        return 1
    elif 4 not in x.values() and 4 in y.values():
        return -1
    elif 4 in x.values() and 4 in y.values():
        for k, v in x.items():
            if v == 4:
                a = card_rank[k]
            elif v == 1:
                c = card_rank[k]
        for k, v in y.items():
            if v == 4:
                b = card_rank[k]
            elif v == 1:
                d = card_rank[k]
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            if c > d:
                return 1
            elif c < d:
                return -1
            else:
                return 0

    elif 3 in x.values() and 3 not in y.values():
        return 1
    elif 3 not in x.values() and 3 in y.values():
        return -1
    elif 3 in x.values() and 3 in y.values():
        if 2 in x.values() and 2 not in y.values():
            return 1
        elif 2 not in x.values() and 2 in y.values():
            return -1
        elif 2 in x.values() and 2 in y.values():
            for k, v in x.items():
                if v == 3:
                    a = card_rank[k]
                elif v == 2:
                    c = card_rank[k]
            for k, v in y.items():
                if v == 3:
                    b = card_rank[k]
                elif v == 2:
                    d = card_rank[k]
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                if c > d:
                    return 1
                elif c < d:
                    return -1
                else:
                    return 0
        else:
            c, d = 0, 0
            for k, v in x.items():
                if v == 3:
                    a = card_rank[k]
                elif v == 1:
                    c = max(card_rank[k], c)
            for k, v in y.items():
                if v == 3:
                    b = card_rank[k]
                elif v == 1:
                    d = max(card_rank[k], d)
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                if c > d:
                    return 1
                elif c < d:
                    return -1
                else:
                    return 0
    elif 2 in x.values() and 2 not in y.values():
        return 1
    elif 2 not in x.values() and 2 in y.values():
        return -1
    elif 2 in x.values() and 2 in y.values():
        x_two, y_two = 0, 0
        a, b, c, d = 0, 0, 0, 0
        for k, v in x.items():
            if v == 2:
                x_two += 1
                a = max(card_rank[k], a)
            elif v == 1:
                c = max(card_rank[k], c)
        for k, v in y.items():
            if v == 2:
                y_two += 1
                b = max(card_rank[k], b)
            elif v == 1:
                d = max(card_rank[k], d)
        if x_two == 2 and y_two < 2:
            return 1
        elif x_two < 2 and y_two == 2:
            return -1
        elif x_two == 2 and y_two == 2:
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                if c > d:
                    return 1
                elif c < d:
                    return -1
                else:
                    return 0
        elif x_two == 1 and y_two == 1:
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                if c > d:
                    return 1
                elif c < d:
                    return -1
                else:
                    return 0
    else:
        a, b = 0, 0
        for k, v in x.items():
            a = max(card_rank[k], a)
        for k, v in y.items():
            b = max(card_rank[k], b)
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0


def compare(x, y):
    a, b = x[1], y[1]
    c, d = x[2], y[2]
    if 5 in a.values() and 5 not in b.values():
        return 1
    elif 5 not in a.values() and 5 in b.values():
        return -1
    elif 5 in a.values() and 5 in b.values():
        for i in range(5):
            if card_rank[c[i]] > card_rank[d[i]]:
                return 1
            elif card_rank[c[i]] < card_rank[d[i]]:
                return -1
    elif 4 in a.values() and 4 not in b.values():
        return 1
    elif 4 not in a.values() and 4 in b.values():
        return -1
    elif 4 in a.values() and 4 in b.values():
        for i in range(5):
            if card_rank[c[i]] > card_rank[d[i]]:
                return 1
            elif card_rank[c[i]] < card_rank[d[i]]:
                return -1
    elif 3 in a.values() and 3 not in b.values():
        return 1
    elif 3 not in a.values() and 3 in b.values():
        return -1
    elif 3 in a.values() and 3 in b.values():
        if 2 in a.values() and 2 not in b.values():
            return 1
        elif 2 not in a.values() and 2 in b.values():
            return -1
        else:
            for i in range(5):
                if card_rank[c[i]] > card_rank[d[i]]:
                    return 1
                elif card_rank[c[i]] < card_rank[d[i]]:
                    return -1
    elif 2 in a.values() and 2 not in b.values():
        return 1
    elif 2 not in a.values() and 2 in b.values():
        return -1
    elif 2 in a.values() and 2 in b.values():
        x_two, y_two = 0, 0
        for _, v in a.items():
            if v == 2:
                x_two += 1
        for _, v in b.items():
            if v == 2:
                y_two += 1
        if x_two == 2 and y_two < 2:
            return 1
        elif x_two < 2 and y_two == 2:
            return -1
        else:
            for i in range(5):
                if card_rank[c[i]] > card_rank[d[i]]:
                    return 1
                elif card_rank[c[i]] < card_rank[d[i]]:
                    return -1
    else:
        for i in range(5):
            if card_rank[c[i]] > card_rank[d[i]]:
                return 1
            elif card_rank[c[i]] < card_rank[d[i]]:
                return -1


# PART two (separate card type and card rank)
wild_card_rank = {n: len(num) - i if n != "J" else 0 for i, n in enumerate(num)}
hand_types = {
    (6, "5K"): lambda cs: len(cs) == 1,
    (5, "4K"): lambda cs: any(v == 4 for v in cs.values()),
    (4, "FH"): lambda cs: len(cs) == 2,
    (3, "3K"): lambda cs: any(v == 3 for v in cs.values()),
    (2, "2P"): lambda cs: len([v for v in cs.values() if v == 2]) == 2,
    (1, "1P"): lambda cs: len([v for v in cs.values() if v == 2]) == 1,
    (0, "HC"): lambda cs: True,
}


def check_hand_simple(cardset):
    cards = cardset[1]
    for hand, func in hand_types.items():
        if func(cards):
            return (cardset, hand)


card_list = []
card_counter = []
score_list = []
for line in lines:
    line = line.strip()
    card, score = line.split(" ")
    card_list.append(card)
    card_counter.append(counter(card))
    score_list.append(int(score))

rank_list = [
    (score_list[i], counter, card_list[i]) for i, counter in enumerate(card_counter)
]

# PART ONE
# rank_list = sorted(rank_list, key=cmp_to_key(compare))
# print(rank_list)


def new_compare(x, y):
    x_use_wild = False
    _, ori_x_best_hand = check_hand_simple(x)
    if "J" in x[1]:
        x_best_hand = (0, "HC")
        for card in set(x[2]) - set("J"):
            copy = x[2].replace("J", card)
            _, hand = check_hand_simple((x[0], Counter(copy), x[2]))
            x_best_hand = max(x_best_hand, hand)
        if x_best_hand < ori_x_best_hand:
            x_best_hand = ori_x_best_hand
        x_use_wild = True
    else:
        x_best_hand = ori_x_best_hand

    y_use_wild = False
    _, ori_y_best_hand = check_hand_simple(y)
    if "J" in y[1]:
        y_best_hand = (0, "HC")
        for card in set(y[2]) - set("J"):
            copy = y[2].replace("J", card)
            _, hand = check_hand_simple((y[0], Counter(copy), y[2]))
            y_best_hand = max(y_best_hand, hand)

        if y_best_hand < ori_y_best_hand:
            y_best_hand = ori_y_best_hand
        y_use_wild = True
    else:
        y_best_hand = ori_y_best_hand

    if x_best_hand > y_best_hand:
        return 1
    elif x_best_hand < y_best_hand:
        return -1
    else:
        for i in range(5):
            if not x_use_wild and not y_use_wild:
                if card_rank[x[2][i]] > card_rank[y[2][i]]:
                    return 1
                elif card_rank[x[2][i]] < card_rank[y[2][i]]:
                    return -1
            elif x_use_wild and not y_use_wild:
                if wild_card_rank[x[2][i]] > card_rank[y[2][i]]:
                    return 1
                elif wild_card_rank[x[2][i]] < card_rank[y[2][i]]:
                    return -1
            elif not x_use_wild and y_use_wild:
                if card_rank[x[2][i]] > wild_card_rank[y[2][i]]:
                    return 1
                elif card_rank[x[2][i]] < wild_card_rank[y[2][i]]:
                    return -1
            else:
                if wild_card_rank[x[2][i]] > wild_card_rank[y[2][i]]:
                    return 1
                elif wild_card_rank[x[2][i]] < wild_card_rank[y[2][i]]:
                    return -1


rank_list = sorted(rank_list, key=cmp_to_key(new_compare))

# with open("./day7_sorted.txt", "r") as f:
#     lines = f.readlines()
# for i, line in enumerate(lines):
#     line = line.strip()
#     if line != rank_list[i][2]:
#         print(i)
#         print(line, rank_list[i][2])
#         print(lines[i + 1], rank_list[i + 1][2])
#         raise Exception

total = 0
for i, t in enumerate(rank_list):
    total += t[0] * (i + 1)
print(total)
