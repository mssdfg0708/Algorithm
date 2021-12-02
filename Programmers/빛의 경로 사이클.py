def calculate_cycle(x, y, d, visited, grid):
    cycle = 0
    # d = 방향 [북, 동, 남, 서]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while not visited[x][y][d]:
        visited[x][y][d] = True
        cycle += 1
        nx = x + dx[d]
        ny = y + dy[d]

        if nx >= len(grid):
            nx = 0
        elif nx < 0:
            nx = len(grid) - 1
        elif ny >= len(grid[0]):
            ny = 0
        elif ny < 0:
            ny = len(grid[0]) - 1
        x, y = nx, ny

        if grid[x][y] == "S":
            pass
        elif grid[x][y] == "R":
            d = (d + 1) % 4
        elif grid[x][y] == "L":
            d = (d - 1) % 4

    return cycle


def solution(grid):
    # visited[x][y][d] / x = x행 / y = y열 / d = 방향 [북, 동, 남, 서]
    visited = [[[False, False, False, False] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    result = []

    # visited 값 순회
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for d in range(4):
                if not visited[x][y][d]:
                    cycle = calculate_cycle(x, y, d, visited, grid)
                    result.append(cycle)

    result.sort()
    return result


grid = ["RSR", "RLS"]
print(solution(grid))
