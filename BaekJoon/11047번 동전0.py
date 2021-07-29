import sys

# n = 동전 종류의 수
# k = 목표 가격
# count_coin = 필요한 동전의 최소 개수
n, k = map(int, sys.stdin.readline().split())
count_coin = 0

coin_list = []
for i in range(n):
    coin_list.append(int(sys.stdin.readline()))

coin_list.reverse()

for item in coin_list:
    if  k <= 0 :
        break
    count_coin += k//item
    k = k % item

print(count_coin)
