# path = dict() 를 이용하여 지나간 길 개수 파악
# path['-1-2-11'] = True
# path['-11-1-2'] = True

def solution(dirs):
    # 초기화
    path = dict()
    x, y, nx, ny = 0, 0, 0, 0

    # 캐릭터 이동
    for d in dirs:
        if d == "U":
            nx = x
            ny = y+1
        if d == "D":
            nx = x
            ny = y-1
        if d == "R":
            nx = x+1
            ny = y
        if d == "L":
            nx = x-1
            ny = y

        # 유효 index 검사
        if nx < -5 or nx > 5:
            continue
        if ny < -5 or ny > 5:
            continue

        # key_code 생성
        key_code = str(x) + str(y) + str(nx) + str(ny)
        path[key_code] = True
        key_code = str(nx) + str(ny) + str(x) + str(y)
        path[key_code] = True
        x, y = nx, ny

    # 지나간 path 길이 반환
    return len(path)//2


dirs = "RRRRRRRRRRLLLLLLLLLLLLLLLLLL"
print(solution(dirs))
