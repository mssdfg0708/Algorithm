from sys import stdin

doc = stdin.readline().strip()
target = stdin.readline().strip()
result = 0

index = 0
while index < (len(doc) - len(target) + 1):
    if target == doc[index: index + len(target)]:
        index += len(target)
        result += 1
        continue
    index += 1

print(result)
