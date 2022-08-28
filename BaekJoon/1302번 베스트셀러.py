import sys

N = int(sys.stdin.readline().rstrip())
sell_count = dict()

for _ in range(N):
    book = sys.stdin.readline().rstrip()
    if book not in sell_count:
        sell_count[book] = 1
        continue
    sell_count[book] += 1

max_count = -1
best_sellers = []
for book, count in sell_count.items():
    if count > max_count:
        max_count = count
        best_sellers.clear()
        best_sellers.append(book)
        continue
    if count == max_count:
        best_sellers.append(book)

best_sellers.sort()
answer = best_sellers[0]
print(answer)
