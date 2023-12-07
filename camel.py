# with open("./camel_input.txt", "r") as f:
with open("./test.txt", "r") as f:
    lines = f.readlines()

num = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_rank = {n: i for i, n in enumerate(num)}


def counter(card):
    counter = {}
    for c in card:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter


def rank_counter(counter):
    if 4 in counter.values():
        return 5
    elif 3 in counter.values() and 2 in counter.values():
        return 4
    elif 3 in counter.values():
        return 3
    elif 2 in counter.values():
        return 2
    return 1


card_list = []
card_counter = []
score_list = []
for line in lines:
    line = line.strip()
    card, score = line.split(" ")
    card_list.append(card)
    card_counter.append(counter(card))
    score_list.append(int(score))

print(card_counter)
for counter in card_counter:
    print(rank_counter(counter))

