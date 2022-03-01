import sys

bitmask = [False for _ in range(21)]

queryLength = int(sys.stdin.readline())
for _ in range(queryLength):
    query = list(sys.stdin.readline().split())

    if query[0] == 'all':
        bitmask = [True for _ in range(21)]
        continue
    if query[0] == 'empty':
        bitmask = [False for _ in range(21)]
        continue

    num = int(query[1])
    if query[0] == 'add':
        bitmask[num] = True
        continue
    if query[0] == 'remove':
        bitmask[num] = False
        continue

    if query[0] == 'check' and bitmask[num]:
        print(1)
        continue
    if query[0] == 'check' and not bitmask[num]:
        print(0)
        continue

    if query[0] == 'toggle':
        bitmask[num] = not bitmask[num]
