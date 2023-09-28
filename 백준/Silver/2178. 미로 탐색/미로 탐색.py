from collections import deque

N, M = map(int, input().split())

maze = []

for i in range(N):
    maze.append(list(map(int, input())))

def bfs(x, y):
    while q:
        x, y = q.popleft()
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if x == (N - 1) and y == (M - 1):
            return visited[x][y]

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and ny >= 0 and nx <= N - 1 and ny <= M - 1:
                if maze[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

q = deque([(0, 0)])
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
print(bfs(0, 0))