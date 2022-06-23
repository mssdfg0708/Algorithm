n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)
answer = []

for i, j in enumerate(s):
    answer.append(i + j + 2)

print(max(answer))
