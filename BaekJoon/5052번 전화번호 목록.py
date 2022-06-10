import sys

T = int(sys.stdin.readline())
for _ in range(T):
    answer = True
    n = int(sys.stdin.readline())
    candidate = [sys.stdin.readline().rstrip() for _ in range(n)]
    candidate.sort()
    min_num = candidate[0]
    for i in range(len(candidate)-1):
        if candidate[i+1][:len(candidate[i])] == candidate[i]:
            answer = False

    if answer:
        print("YES")
    else:
        print("NO")
