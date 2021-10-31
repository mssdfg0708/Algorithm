from sys import stdin

for _ in range(int(stdin.readline())):
    logs = stdin.readline().strip()
    left, right = [], []

    for log in logs:
        if log == '<':
            if left:
                right.append(left.pop())
        elif log == '>':
            if right:
                left.append(right.pop())
        elif log == '-':
            if left:
                left.pop()
        else:
            left.append(log)

    left.extend(reversed(right))
    print(''.join(left))
