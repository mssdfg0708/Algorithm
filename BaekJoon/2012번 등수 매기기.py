import sys

N = int(sys.stdin.readline().rstrip())
expectation_ranks = []
for _ in range(N):
    rank = int(sys.stdin.readline().rstrip())
    expectation_ranks.append(rank)

expectation_ranks.sort()

answer = 0
for index in range(len(expectation_ranks)):
    expectation_rank = expectation_ranks[index]
    differ = abs(index + 1 - expectation_ranks[index])
    answer += differ

print(answer)
