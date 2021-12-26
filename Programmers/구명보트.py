def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    left, right = 0, len(people)-1

    while left <= right:
        boat_weight = 0
        # 가장 무거운 사람 탑승
        boat_weight += people[left]
        left += 1
        # 가장 가벼운 사람 확인
        if boat_weight + people[right] <= limit:
            boat_weight += people[right]
            right -= 1
        # 보트 출발
        answer += 1

    return answer


people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))

# 투포인터 활용
# 왼쪽, 오른쪽 부터 1개씩 pick
# 합이 limit 이하라면 보트 출발
# left > right 까지 반복
# 출발한 보트 개수 return
