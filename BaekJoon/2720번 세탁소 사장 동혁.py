T = int(input())
for _ in range(T):
    result = [0, 0, 0, 0]
    cost = int(input())

    while cost >= 25:
        cost -= 25
        result[0] += 1
    while cost >= 10:
        cost -= 10
        result[1] += 1
    while cost >= 5:
        cost -= 5
        result[2] += 1
    while cost >= 1:
        cost -= 1
        result[3] += 1

    for item in result:
        print(item, end=' ')
    print()
