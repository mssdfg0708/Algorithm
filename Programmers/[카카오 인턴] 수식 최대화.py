def solution(expression):
    # 숫자와 연산자 분리
    nums = []
    operands = []
    buffer = ''
    for item in expression:
        if item.isdigit():
            buffer += item
            continue
        nums.append(int(buffer))
        operands.append(item)
        buffer = ''
    nums.append(int(buffer))

    root_nums = []
    root_operands = []
    for item in nums:
        root_nums.append(item)
    for item in operands:
        root_operands.append(item)

    # 알고리즘 실행
    priorities = ['+-*', '+*-', '-*+', '-+*', '*-+', '*+-']
    result = []

    for p in priorities:
        nums = []
        operands = []
        for item in root_nums:
            nums.append(item)
        for item in root_operands:
            operands.append(item)

        for operand in p:
            for index in range(len(operands)):
                if operands[index] == operand:
                    if operand == '+':
                        nums[index+1] = nums[index] + nums[index+1]
                    if operand == '-':
                        nums[index+1] = nums[index] - nums[index+1]
                    if operand == '*':
                        nums[index+1] = nums[index] * nums[index+1]
                    operands[index] = None
                    nums[index] = None
                    continue

            while None in operands:
                operands.remove(None)
            while None in nums:
                nums.remove(None)

            if not operands:
                result.append(abs(nums[0]))
                break

    return max(result)


expression = "100-200*300-500+20"
print(solution(expression))
