import sys

N = int(sys.stdin.readline().rstrip())
customers = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    customers.append(num)

customers.sort(reverse=True)
answer = 0
for index in range(len(customers)):
    tip = customers[index] - index
    if tip > 0:
        answer += tip

print(answer)
