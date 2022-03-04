# 솔직히 아이디어 보고 감탄

weight_length = int(input())
weights = list(map(int, input().split()))
weights.sort()

target = 1
for weight in weights:
    if target < weight:
        break
    target += weight

print(target)
