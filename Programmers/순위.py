from collections import deque


def count_win(root_num, count, people):
    q = deque()
    visited = [False for _ in range(len(people)+1)]
    q.append(root_num)
    visited[root_num] = True

    while q:
        cur_num = q.popleft()
        for next_num in people[cur_num][0]:
            if visited[next_num]:
                continue
            count += 1
            q.append(next_num)
            visited[next_num] = True

    return count


def count_lose(root_num, count, people):
    q = deque()
    visited = [False for _ in range(len(people)+1)]
    q.append(root_num)
    visited[root_num] = True

    while q:
        cur_num = q.popleft()
        for next_num in people[cur_num][1]:
            if visited[next_num]:
                continue
            count += 1
            q.append(next_num)
            visited[next_num] = True

    return count


def solution(n, results):
    answer = 0
    people = [[[], []]for _ in range(n+1)]
    for win_person, lose_person in results:
        people[win_person][0].append(lose_person)
        people[lose_person][1].append(win_person)

    for person_num in range(1, n+1):
        count = 1
        count = count_win(person_num, count, people)
        count = count_lose(person_num, count, people)
        if count == n:
            answer += 1

    return answer


input_n = 5
input_results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(input_n, input_results))

# person[2][0] 2번 선수가 이긴 선수 목록
# person[2][1] 2번 선수가 진 선수 목록
