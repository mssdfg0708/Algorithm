import sys

NATION, target_nation = map(int, sys.stdin.readline().split())
nation_list = []

for _ in range(NATION):
    nation = list(map(int, sys.stdin.readline().split()))
    medal_key = str(nation[1]) + str(nation[2]) + str(nation[3])
    nation.append(medal_key)
    nation_list.append(nation)

nation_list.sort(key=lambda x: (x[1] * -1, x[2] * -1, x[3] * -1))
target_medal_key = None
for nation in nation_list:
    if nation[0] == target_nation:
        target_medal_key = nation[4]
        break

for index in range(len(nation_list)):
    if nation_list[index][4] == target_medal_key:
        print(index+1)
        break
