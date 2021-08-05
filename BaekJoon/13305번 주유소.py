import sys

# 현재 도시의 기름 가격을 확인한다
# 앞으로 만나게 되는 도시의 가격을 모두 확인하여
# 앞으로 만나게 되는 도시의 가격이 현재 도시의 가격보다 작다면 거기까지만
# 주유한다
# 목적지까지 이 연산을 반복한다
city_amount = int(input())
distance_list = list(map(int, sys.stdin.readline().split()))
cost_list = list(map(int, sys.stdin.readline().split()))
total_cost = 0

i = 0
city_cost = 987654321000
while i < city_amount - 1:
    if (cost_list[i] < city_cost):
        city_cost = cost_list[i]
    total_cost += (distance_list[i] * city_cost)
    i += 1

print(total_cost)
