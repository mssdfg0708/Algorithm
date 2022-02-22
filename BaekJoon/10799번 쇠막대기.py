import sys

data = sys.stdin.readline().strip()

answer = 0
overlap = 0
buffer = ''
for index in range(len(data)):

    if data[index] == '(':
        overlap += 1
    if data[index] == ')' and buffer == '(':
        overlap -= 1
        answer += overlap
    if data[index] == ')' and buffer == ')':
        overlap -= 1
        answer += 1

    buffer = data[index]

print(answer)
