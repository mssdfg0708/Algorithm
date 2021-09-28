N, M = map(int, input().split())
card = list(map(int, input().split()))
result = [0, 0, 0]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j == k or i == k:
                continue
            temp = card[i] + card[j] + card[k]
            if temp <= M and temp > sum(result):
                result = [card[i], card[j], card[k]]
print(sum(result))
