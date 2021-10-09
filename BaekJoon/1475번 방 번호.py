import math

num = input()
cnt = list()
for n in range(10):
    n = str(n)
    cnt.append(num.count(n))

cnt[6] = math.ceil((cnt[6]+cnt[9])/2)
cnt[9] = 0
print(max(cnt))
