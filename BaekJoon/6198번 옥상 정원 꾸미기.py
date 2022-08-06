N = int(input())

stack = []
answer = 0

for _ in range(N):
    h = int(input())
    while stack and stack[-1] <= h:
        stack.pop()
    answer += len(stack)
    stack.append(h)

print(answer)
