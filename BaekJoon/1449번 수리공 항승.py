def fix(p):
    for i in range(L):
        fixed_list[p + i] = True


N, L = map(int, input().split())
broken_list = list(map(int, input().split()))
broken_list.sort()
fixed_list = [False for _ in range(broken_list[-1] + L)]
count = 0

for point in broken_list:
    if not fixed_list[point]:
        fix(point)
        count += 1

print(count)
