import sys
sys.setrecursionlimit(10 ** 6)


# Start 시간 초과 코드
def postorder(root):
    if root == -1:
        return
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root)


tree = dict()
root = int(sys.stdin.readline().strip())
tree[root] = [-1, -1]

while True:
    try:
        num = int(sys.stdin.readline().strip())
    except:
        break

    parent = root
    while True:
        if num < parent and tree[parent][0] == -1:
            tree[parent][0] = num
            tree[num] = [-1, -1]
            break
        elif num < parent and tree[parent][0] != -1:
            parent = tree[parent][0]
        elif num > parent and tree[parent][1] == -1:
            tree[parent][1] = num
            tree[num] = [-1, -1]
            break
        elif num > parent and tree[parent][1] != -1:
            parent = tree[parent][1]


postorder(root)
# End 시간 초과 코드


# Start 정답 코드
def postOrder(start, end):
    if start > end:
        return

    root = preOrder[start]
    idx = start + 1

    while idx <= end:
        if preOrder[idx] > root:
            break
        idx += 1

    postOrder(start + 1, idx - 1)
    postOrder(idx, end)
    print(root)


preOrder = []
while True:
    try:
        preOrder.append(int(sys.stdin.readline()))
    except:
        break
postOrder(0, len(preOrder) - 1)
# End 정답 코드
