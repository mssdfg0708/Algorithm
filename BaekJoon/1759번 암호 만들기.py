import sys


def dfs(length, idx):
    if length == l:
        collection = 0
        consonant = 0
        for i in range(l):
            if arr[i] in 'aeiou':
                collection += 1
            else:
                consonant += 1

        if collection >= 1 and consonant >= 2:
            print(''.join(arr))
        return

    for i in range(idx, c):
        if check[i] == 0:
            arr.append(s[i])
            check[i] = 1
            dfs(length + 1, i + 1)
            check[i] = 0
            del arr[-1]


l, c = map(int, sys.stdin.readline().split())
check = [0 for i in range(c)]
arr = []
s = input().split()
s.sort()
dfs(0, 0)
