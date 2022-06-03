start, end = map(int, input().split())

array = []
for num in range(100):
    for _ in range(num):
        array.append(num)

answer = 0
for index in range(start-1, end):
    answer += array[index]
print(answer)
