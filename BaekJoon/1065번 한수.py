n = int(input())
answer = 0

for i in range(1, n + 1):
    if i < 100:
        answer += 1
        continue
    checkList = list(map(int, str(i)))
    if checkList[0] - checkList[1] == checkList[1] - checkList[2]:
        answer += 1

print(answer)
