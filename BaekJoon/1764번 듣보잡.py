from sys import stdin


never_seen = set()
never_heard = set()

# 입력 받기
see, hear = map(int, stdin.readline().split())
for _ in range(see):
    never_seen.add(stdin.readline().rstrip())
for _ in range(hear):
    never_heard.add(stdin.readline().rstrip())

# 합집합 계산 이후 정렬
result = list(never_seen & never_heard)
result.sort()

# 결과 출력
print(len(result))
for item in result:
    print(item)
