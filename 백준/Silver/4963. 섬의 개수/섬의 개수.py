import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, -1, +1, +1, 0, +1, -1]
dy = [-1, -1, +1, 0, +1, +1, -1, 0]

def bfs(i, j):
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if visited[nx][ny] != 1 and island_map[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    island_map = []

    visited = [[0] * w for _ in range(h)]
    island = 0

    for i in range(h):
        island_map.append(list(map(int, input().split())))

    queue = deque()
    for i in range(h):
        for j in range(w):
            if island_map[i][j] == 1 and visited[i][j] != 1:
                bfs(i, j)
                island += 1
    print(island)