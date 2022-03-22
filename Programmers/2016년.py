def solution(month, day):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for m in range(month):
        day += days_in_month[m]

    date_index = (day-1) % 7
    answer = date[date_index]

    return answer


a, b = 12, 31
print(solution(a, b))

# 0 1 2 3 4 5 6
# 1일 2일 3일 ....
# 8일 9일 10일
# day = (day-1)%7
