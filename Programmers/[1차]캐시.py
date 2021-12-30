from collections import deque


def solution(cache_size, cities):
    answer = 0
    # 예외 처리
    if cache_size == 0:
        return len(cities) * 5

    cache = deque()
    for city in cities:
        city = city.lower()
        # cache 에 city 가 존재
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
            continue
        # cache 에 city 가 존재 하지 않음
        if len(cache) >= cache_size:
            cache.popleft()
        cache.append(city)
        answer += 5

    return answer


cache_size = 2
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cache_size, cities))
