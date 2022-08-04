from itertools import combinations

PEOPLE, CHICKEN = map(int, input().split())
scores = []
for _ in range(PEOPLE):
    row = list(map(int, input().split()))
    scores.append(row)

answer = -1
for candidate in combinations(range(CHICKEN), 3):
    candidate_max = 0
    for person in range(PEOPLE):
        personal_max = -1
        score = scores[person]
        for chicken in candidate:
            personal_max = max(personal_max, score[chicken])
        candidate_max += personal_max

    answer = max(answer, candidate_max)

print(answer)
