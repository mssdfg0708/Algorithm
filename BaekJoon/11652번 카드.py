cards = dict()

n = int(input())
for _ in range(n):
    card = int(input())
    if card not in cards:
        cards[card] = 1
    else:
        cards[card] += 1

cards = sorted(cards.items(), key=lambda x: (-x[1], x[0]))
print(cards[0][0])

