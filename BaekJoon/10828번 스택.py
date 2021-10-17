import sys

n = int(input())
stack = []

for _ in range(n):
    query = list(sys.stdin.readline().split())
    # query 수행
    if query[0] == 'push':
        stack.append(query[1])
    if query[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if query[0] == 'size':
        print(len(stack))
    if query[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if query[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

