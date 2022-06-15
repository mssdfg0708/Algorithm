import sys

candidate_limit = int(sys.stdin.readline().strip())
scores = []
for _ in range(candidate_limit):
    scores.append(int(sys.stdin.readline().strip()))

my_score = scores[0]
count = 0
while True:
    max_score = 0
    max_index = 0
    for index in range(len(scores)):
        score = scores[index]
        if score >= max_score:
            max_score = score
            max_index = index
    if max_index == 0:
        break
    scores[0] += 1
    scores[max_index] -= 1
    count += 1

print(count)
