import sys
from collections import deque

BELT, SUSHI, QUEUE, coupon = map(int, sys.stdin.readline().split())
choice_sushi_count = [0 for _ in range(SUSHI + 1)]
choice_sushi_types = 0
answer = 0

belt = []
for _ in range(BELT):
    sushi = int(sys.stdin.readline().rstrip())
    belt.append(sushi)

for index in range(QUEUE):
    belt.append(belt[index])


def append_sushi(sushi, choice_sushi_types):
    if choice_sushi_count[sushi] == 0:
        choice_sushi_types += 1
    choice_sushi_count[sushi] += 1
    return choice_sushi_types


def popleft_sushi(sushi, choice_sushi_types):
    choice_sushi_count[sushi] -= 1
    if choice_sushi_count[sushi] == 0:
        choice_sushi_types -= 1
    return choice_sushi_types


choice_queue = deque()
for index in range(QUEUE):
    sushi = belt[index]
    choice_queue.append(sushi)
    choice_sushi_types = append_sushi(sushi, choice_sushi_types)

    sushi_types = choice_sushi_types
    if choice_sushi_count[coupon] == 0:
        sushi_types += 1

    answer = max(answer, sushi_types)

for index in range(QUEUE, BELT + QUEUE):
    sushi = choice_queue.popleft()
    choice_sushi_types = popleft_sushi(sushi, choice_sushi_types)

    choice_queue.append(belt[index])
    sushi = belt[index]
    choice_sushi_types = append_sushi(sushi, choice_sushi_types)

    sushi_types = choice_sushi_types
    if choice_sushi_count[coupon] == 0:
        sushi_types += 1

    answer = max(answer, sushi_types)

print(answer)
