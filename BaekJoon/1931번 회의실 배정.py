import sys

num = int(input())
array = []
count = 0
end_memory = 999999999999
for i in range(num):
    array.append(list(map(int, sys.stdin.readline().split())))

array.sort()

for start, end in array:
    if start >= end_memory:
        count += 1
        end_memory = 999999999999
    if end < end_memory:
        end_memory = end
print(count + 1)
