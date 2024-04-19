def find_direction(d):
    if d == "N":
        return 0
    elif d == "S":
        return 1
    elif d == "W":
        return 2
    elif d == "E":
        return 3

# 공원, 로봇강아지가 수행할 명령이 담긴 문자열 배열
def solution(park, routes):
    w = len(park[0])
    h = len(park)
    
    # 시작점 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                answer = [i, j]
    
    # 북, 남, 서, 동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while routes:
        stop = False
        d, steps = routes.pop(0).split(' ')
        
        # 앞으로 가는 동안 내내
        for j in range(1, int(steps) + 1):
            nx = answer[0] + (j * dx[find_direction(d)])
            ny = answer[1] + (j * dy[find_direction(d)])
        
            if nx < 0 or ny < 0 or nx >= h or ny >= w or park[nx][ny] == "X":
                stop = True
                break
            
        if stop:
            continue
        
        answer = [nx, ny]
    # [세로 방향 좌표, 가로 방향 좌표]순
    return answer