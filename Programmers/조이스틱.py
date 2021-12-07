def solution(name):
    alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    final_alphabet = 26

    target = []
    for char in name:
        target.append(char)

    name = []
    for _ in range(len(target)):
        name += "A"

    # 예외 처리
    if name == target:
        return 0

    answer = []
    # name, index, num
    next_candidates = [[name, 0, -1]]
    for i in range(len(target) + 1):
        candidates = []
        for item in next_candidates:
            candidates.append(item)
        next_candidates = []

        for candidate, index, num in candidates:
            c = []
            for item in candidate:
                c.append(item)
            if c == target:
                answer.append(num)
                continue
            num += 1

            if c[index] != target[index]:
                up = abs(alpha_list.index(c[index]) - alpha_list.index(target[index]))
                down = abs(final_alphabet - up)
                c[index] = target[index]
                num += min(up, down)

            if index + 1 >= len(target):
                next_candidates.append([c, 0, num])
            else:
                next_candidates.append([c, index + 1, num])

            if index - 1 < 0:
                next_candidates.append([c, len(target) - 1, num])
            else:
                next_candidates.append([c, index - 1, num])

    return min(answer)


name = "AAA"
print(solution(name))

# "AAAAAAAA" -> "CTAAAAAPO"
# 최대 2 ** 20 (1,048,576) 만큼 좌우를 고르는 경우의 수 존재
# 각각의 경우에서 분기를 나누며 탐색
# target 과 name 을 비교하여 다르면
# 위로 올라가는 경우와 아래로 내려가는 경우 비교
# "2" or "24" choose 2
