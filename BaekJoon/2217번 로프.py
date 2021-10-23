# 로프가 들어올릴수 있는 각 중량을 정렬한다
# 로프의 최대증량 * 로프의 개수 를 모두 계산
# 가장 큰 값 출력

# 입력 받기
n = int(input())
weights = []
result = -1
for _ in range(n):
    weights.append(int(input()))
weights.sort(reverse=True)

# 각 로프를 포함한 최대 중량 저장
for i in range(n):
    temp = weights[i] * (i+1)
    if temp > result:
        result = temp

# 출력
print(result)
