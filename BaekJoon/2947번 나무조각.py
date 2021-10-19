def print_table():
    for item in table:
        print(item, end=' ')
    print()


def bubble_module():
    for i in range(1, len(table)):
        if table[i - 1] > table[i]:
            table[i - 1], table[i] = table[i], table[i - 1]
            print_table()


def check_order():
    for i in range(1, len(table)):
        if table[i - 1] > table[i]:
            return True
    return False


table = list(map(int, input().split()))
while check_order():
    for i in range(1, len(table)):
        if table[i - 1] > table[i]:
            bubble_module()
            break
