import sys
from collections import deque

test = int(sys.stdin.readline().strip())
for _ in range(test):
    days_length = int(sys.stdin.readline().strip())
    days = list(map(int, sys.stdin.readline().split()))
    high_prices = deque()
    for price in days:
        if not high_prices:
            high_prices.append(price)
            continue
        if high_prices[0] < price:
            high_prices.clear()
            high_prices.append(price)
            continue
        if high_prices[-1] >= price:
            high_prices.append(price)
            continue
        while high_prices[-1] < price:
            high_prices.pop()
        high_prices.append(price)

    profit = 0
    high_prices.append(-1)
    target_price = high_prices.popleft()
    for price in days:
        if price < target_price:
            profit += target_price - price
        else:
            target_price = high_prices.popleft()

    print(profit)
