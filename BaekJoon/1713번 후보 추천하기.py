import sys

CANDIDATE = int(sys.stdin.readline().rstrip())
RECOMMEND = int(sys.stdin.readline().rstrip())
candidates = []
recommends = [0 for _ in range(101)]
query = list(map(int, sys.stdin.readline().split()))
for candidate in query:
    if len(candidates) < CANDIDATE:
        candidates.append(candidate)
        recommends[candidate] = 1
        continue

    if candidate in candidates:
        recommends[candidate] += 1
        continue

    delete_value = 999999
    target = -1
    for index in candidates:
        if recommends[index] < delete_value:
            delete_value = recommends[index]
            target = index
            print(target, candidates)
    candidates.remove(target)
    candidates.append(candidate)
    recommends[target] = 0
    recommends[candidate] = 1

candidates.sort()
for item in candidates:
    print(item, end=' ')
