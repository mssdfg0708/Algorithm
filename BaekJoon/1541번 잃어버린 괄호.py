import sys

input = sys.stdin.readline()
buffer = ''
number_list = []
operator_list = []
result = 0

# 숫자와 연산자 분리
for item in input:
    if item == '-' or item == '+':
        number_list.append(int(buffer))
        operator_list.append(item)
        buffer = ''
    else:
        buffer += item
number_list.append(int(buffer))

# 결과값 연산
result += number_list[0]
detect_minus = False
for i in range(len(operator_list)):
    if not detect_minus:
        if operator_list[i] == '+':
            result += number_list[i+1]
        else:
            detect_minus = True
            result -= number_list[i+1]
    else:
        result -= number_list[i+1]

print(result)
