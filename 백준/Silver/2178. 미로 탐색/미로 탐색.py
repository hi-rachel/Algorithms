import sys
from collections import deque

input = sys.stdin.readline

# 세로, 가로
N, M = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] != 1:
                    if maze[nx][ny] >= 1:
                        queue.append((nx, ny))
                        maze[nx][ny] = maze[x][y] + 1
                        visited[nx][ny] = 1

                if nx == N - 1 and ny == M - 1:
                    break


for i in range(N):
    for j in range(M):
        if maze[i][j] == 1:
            bfs(i, j)

print(maze[N-1][M-1])