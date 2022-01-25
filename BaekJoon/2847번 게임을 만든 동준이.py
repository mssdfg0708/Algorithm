test_case = int(input())

scores = []
for _ in range(test_case):
    scores.append(int(input()))

answer = 0
for index in range(len(scores)-2, -1, -1):
    while scores[index] >= scores[index+1]:
        scores[index] -= 1
        answer += 1

print(answer)
