def solution(d, budget):
    d.sort()

    count = 0
    for cost in d:
        if budget < cost:
            break
        budget -= cost
        count += 1

    return count


in_d = [1, 3, 2, 5, 4]
in_budget = 9
solution(in_d, in_budget)
