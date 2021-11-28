# Double Linked List with Dictionary
def solution(n, k, cmd):
    chart = dict()
    for i in range(n):
        chart[i] = ['O', i-1, i+1]
    chart[0] = ['O', None, 1]
    chart[n-1] = ['O', n-2, None]

    stack = []
    cursor = k

    for query in cmd:
        # UP
        if query[0] == 'U':
            move = int(query[2:])
            while move > 0:
                cursor = chart[cursor][1]
                move -= 1
        # DOWN
        if query[0] == 'D':
            move = int(query[2:])
            while move > 0:
                cursor = chart[cursor][2]
                move -= 1
        # CLEAR
        if query[0] == 'C':
            stack.append(chart[cursor] + [cursor])
            prev = chart[cursor][1]
            next = chart[cursor][2]
            chart[cursor] = ["X", prev, next]
            if prev is not None:
                chart[prev][2] = next
            if next is not None:
                chart[next][1] = prev
            if next is None:
                cursor = prev
            else:
                cursor = next

        # Z
        if query[0] == 'Z':
            OX, prev, next, now = stack.pop()
            if prev is not None:
                chart[prev][2] = now
            if next is not None:
                chart[next][1] = now
            chart[now] = ['O', prev, next]

    result = ''
    for key in chart:
        char = chart[key][0]
        result += char

    return result


n = 5
k = 2
cmd = ["U 2", "C", "D 1", "Z"]
print(solution(n, k, cmd))
