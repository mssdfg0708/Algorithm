from itertools import permutations
import sys

n, m = map(int, input().split())
output = ''

n_list = []
for i in range(1, n+1):
    n_list.append(str(i))

for i in permutations(n_list, m):
    for item in i:
        output += ' ' + item
    print(output.strip())
    output = ''
