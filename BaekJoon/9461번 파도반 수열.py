import sys

N = int(sys.stdin.readline())
length_list = [int(sys.stdin.readline()) for i in range(N)]
seq = [1, 1, 1, 2, 2]

for i in range(5, max(length_list)):
    seq.append(seq[i-1]+seq[i-5])

for i in length_list:
    print(seq[i-1])
