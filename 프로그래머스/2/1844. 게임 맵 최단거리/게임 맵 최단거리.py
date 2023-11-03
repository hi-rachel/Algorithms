from collections import deque
        
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append([0, 0])
    
    while queue:
        x, y = queue.popleft()
        
        if n - 1 == x and m - 1 == y:
            return maps[x][y]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx, ny])
    print(maps)

    return -1
    
    
    