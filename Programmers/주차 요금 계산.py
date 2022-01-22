import math


def solution(fees, records):
    new_records = []
    result = []

    def str_to_int(query):
        time_str, number, control = query.split()
        time = 0
        hour = time_str[0:2]
        time += int(hour) * 60
        minute = time_str[3:5]
        time += int(minute)
        new_records.append([time, int(number), control])

    def calculate_fee(time_memory):
        time_count = 0
        fee_cost = 0
        time_memory.reverse()
        # 홀수 일 경우
        if time_memory[0][1] == 'IN':
            time_count += 1439 - time_memory[0][0]
            for i in range(1, len(time_memory), 2):
                time_count += time_memory[i][0] - time_memory[i + 1][0]
        # 짝수 일 경우
        else:
            for i in range(0, len(time_memory), 2):
                time_count += time_memory[i][0] - time_memory[i + 1][0]
        fee_cost += fees[1]
        if time_count > fees[0]:
            fee_cost += (math.ceil((time_count - fees[0]) / fees[2]) * fees[3])
        return fee_cost

    for record in records:
        str_to_int(record)
    new_records.sort(key=lambda x: x[1])

    time_memory = []
    last_car_number = new_records[0][1]
    for time, car_number, control in new_records:
        if car_number == last_car_number:
            time_memory.append([time, control])
        else:
            result.append(calculate_fee(time_memory))
            last_car_number = car_number
            time_memory.clear()
            time_memory.append([time, control])
    result.append(calculate_fee(time_memory))

    return result


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
           "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
