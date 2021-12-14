from itertools import product

# 살아있는 버튼 확인
target = int(input())
buttons = [str(i) for i in range(10)]
broken_count = int(input())
broken_buttons = []
if broken_count > 0:
    broken_buttons = list(input().split())
for button in broken_buttons:
    buttons.remove(button)

# 1-6자리 내에서 가능한 버튼 조합을 확인
# 최소값 저장
answer = 987654321
candidates = []
for r in range(1, 7):
    temp = list(product(buttons, repeat=r))
    candidates += temp
for candidate in candidates:
    channel = ''.join(candidate)
    channel = int(channel)
    difference = abs(channel - target)
    count = difference + len(str(channel))
    answer = min(answer, count)

# 시작점 100에서 +- 만으로 이동가능한 경우 확인
root = abs(100 - target)
answer = min(answer, root)

# 결과 출력
print(answer)
