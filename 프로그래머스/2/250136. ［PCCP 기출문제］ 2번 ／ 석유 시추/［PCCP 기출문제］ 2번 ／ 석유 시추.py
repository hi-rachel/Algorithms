# 세로 n, 가로 m
# 시추관을 수직(열)으로 단 하나만 뚫을때, 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾아라
# 상, 하, 좌, 우로 연결된 석유는 하나의 덩어리

from collections import deque

def solution(land):
    n = len(land) # 세로
    m = len(land[0]) # 가로
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
     # 각 열마다 최대 석유 덩어리 크기를 저장할 배열
    max_oil_in_column = [0] * m
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        visited[i][j] = 1
        cnt = 1
        min_y, max_y = j, j
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
                    min_y = min(min_y, ny)
                    max_y = max(max_y, ny)

        for y in range(min_y, max_y + 1):
                max_oil_in_column[y] += cnt
                
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                
    return max(max_oil_in_column)