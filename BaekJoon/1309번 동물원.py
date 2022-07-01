n = int(input())

arr = [[0] * 3 for i in range(100001)]

for index in range(3):
    arr[1][index] = 1

for index in range(2, 100001):
    arr[index][0] = arr[index - 1][1] + arr[index - 1][2] % 9901
    arr[index][1] = arr[index - 1][0] + arr[index - 1][2] % 9901
    arr[index][2] = arr[index - 1][0] + arr[index - 1][1] + arr[index - 1][2] % 9901

answer = sum(arr[n]) % 9901
print(answer)
