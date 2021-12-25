def solution(n, words):
    people = [[] for _ in range(n)]

    # 초기값 설정
    stack = [words[0]]
    people[0].append(words[0])

    # words 확인 알고리즘
    answer = [0, 0]
    for w in range(1, len(words)):
        word = words[w]
        person = w % n
        # 끝말잇기 실패
        if stack[-1][-1] != word[0]:
            answer = [person + 1, len(people[person]) + 1]
            break
        # 중복된 단어 확인
        if word in stack:
            answer = [person + 1, len(people[person]) + 1]
            break
        # 끝말잇기 성공
        people[person].append(word)
        stack.append(word)

    return answer


n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))
