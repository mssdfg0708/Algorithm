# connected [][] = 연결 정보 입력

n = int(input())
connected = []
for _ in range(n):
    connected.append((list(map(int, input().split()))))

# Floyd Warshall ====================================
for middle in range(n):
    for start in range(n):
        for end in range(n):
            if connected[start][middle] and connected[middle][end]:
                connected[start][end] = 1
# Floyd Warshall ====================================

# 출력 형식 적용
for row in connected:
    result = ' '.join(map(str, row))
    print(result)
