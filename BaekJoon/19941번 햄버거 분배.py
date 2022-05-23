import sys

N, K = map(int, sys.stdin.readline().split())
table = list(sys.stdin.readline())

answer = 0

for i in range(N):
    if table[i] == 'P':
        for offset in range(max(i-K, 0), min(i+K+1, N)):
            if table[offset] == 'H':
                table[offset] = 0
                answer += 1
                break

print(answer)
