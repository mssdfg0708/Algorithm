from collections import deque

n, k = map(int, input().split())
queue = deque()
removed_list = []

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        removed_number = queue.popleft()
        queue.append(removed_number)
    removed_number = queue.popleft()
    removed_list.append(removed_number)

result = '<'
for item in removed_list:
    result += (str(item) + ', ')
result = result[:-2]
result += '>'
print(result)
