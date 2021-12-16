def solution(citations):
    citations.sort(reverse=True)
    answer = 0

    # 가장 최대인 h 를 찾는 알고리즘
    for h in range(10001):
        count = 0
        # citations 의 원소를 순회
        for item in citations:
            # h 보다 원소가 크다면 count += 1
            if item >= h:
                count += 1
        # h 보다 큰 원소의 개수가 h 보다 많은지 확인
        if count >= h:
            answer = h

    return answer


citations = [100 for _ in range(1001)]
print(solution(citations))
