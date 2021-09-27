# def str_to_num(string):
#     row = ['NULL', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#     return row.index(string)
#
#
# def num_to_str(num):
#     row = ['NULL', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#     return row[num]
#
#
# def move(d, king, stone):
#     king_row, king_col = king
#     stone_row, stone_col = stone
#     if d == 'R':
#         king_col += 1
#     if d == 'L':
#         king_col -= 1
#     if d == 'B':
#         king_row -= 1
#     if d == 'T':
#         king_row += 1
#     if d == 'RT':
#         king_col += 1
#         king_row += 1
#     if d == 'LT':
#         king_col -= 1
#         king_row += 1
#     if d == 'RB':
#         king_col += 1
#         king_row -= 1
#     if d == 'LB':
#         king_col -= 1
#         king_row -= 1
#     if king_row < 1 or king_row > 8 or king_col < 1 or king_col > 8:
#         return king, stone
#
#     if stone == [king_row, king_col]:
#         if d == 'R':
#             stone_col += 1
#         if d == 'L':
#             stone_col -= 1
#         if d == 'B':
#             stone_row -= 1
#         if d == 'T':
#             stone_row += 1
#         if d == 'RT':
#             stone_col += 1
#             stone_row += 1
#         if d == 'LT':
#             stone_col -= 1
#             stone_row += 1
#         if d == 'RB':
#             stone_col += 1
#             stone_row -= 1
#         if d == 'LB':
#             stone_col -= 1
#             stone_row -= 1
#         if stone_row < 1 or stone_row > 8 or stone_col < 1 or stone_col > 8:
#             return king, stone
#
#     king = [king_row, king_col]
#     stone = [stone_row, stone_col]
#     return king, stone
#
#
# king, stone, count = map(str, input().split())
# king = [str_to_num(king[0]), int(king[1])]
# stone = [str_to_num(stone[0]), int(stone[1])]
# count = int(count)
#
# for _ in range(count):
#     d = input()
#     king, stone = move(d, king, stone)
#
# king[0] = num_to_str(king[0])
# stone[0] = num_to_str(stone[0])
# for item in king:
#     print(item, end='')
# print()
# for item in stone:
#     print(item, end='')
# -------------------------------------------

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
king, stone, count = map(str, input().split())
king = [row.index(king[0]), int(king[1])]
stone = [row.index(stone[0]), int(stone[1])]
count = int(count)

for _ in range(count):
    direction = move.index(input())
    king_row = king[0] + dx[direction]
    king_col = king[1] + dy[direction]
    if king_row < 0 or king_row > 7 or king_col < 1 or king_col > 8:
        continue
    if stone == [king_row, king_col]:
        stone_row = stone[0] + dx[direction]
        stone_col = stone[1] + dy[direction]
        if stone_row < 0 or stone_row > 7 or stone_col < 1 or stone_col > 8:
            continue
        stone = [stone_row, stone_col]
    king = [king_row, king_col]

king[0] = row[king[0]]
stone[0] = row[stone[0]]

for item in king:
    print(item, end='')
print()
for item in stone:
    print(item, end='')
