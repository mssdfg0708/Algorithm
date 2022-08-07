from collections import deque

X = int(input())
line = input()
q = deque()
for item in line:
    q.append(item)

stack = []
answer = 0
while q:
    if len(stack) > X:
        break

    answer += 1
    item = q[0]
    next_item = None
    if len(q) > 1:
        next_item = q[1]

    if not stack:
        q.popleft()
        stack.append(item)
        continue

    if stack[-1] != item:
        q.popleft()
        stack.pop()
        continue

    if stack[-1] == item and next_item is None:
        q.popleft()
        stack.append(item)
        continue

    if next_item is None:
        continue

    if stack[-1] == item and stack[-1] != next_item:
        temp = q.popleft()
        q.popleft()
        stack.pop()
        q.appendleft(temp)
        continue

    if stack[-1] == item and stack[-1] == next_item:
        q.popleft()
        stack.append(item)

if len(stack) > X:
    answer -= 1

print(answer)
