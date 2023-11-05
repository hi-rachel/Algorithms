from collections import deque

t = int(input())

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                BFS(i, j)
                cnt += 1

    print(cnt)