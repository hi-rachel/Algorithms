from collections import deque

m, n = map(int, input().split())
tomatoes = []

for _ in range(n):
    tomatoes.append(list(map(int, input().split())))

visited = [[0] * (m + 1) for _ in range(n + 1)]
dates = [[0] * (m) for _ in range(n)]

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

queue = deque()

for i in range(0, n):
    for j in range(0, m):
        if tomatoes[i][j] == 1:
            queue.append([i, j])
            visited[i][j] = 1

while queue:
    x, y = queue.popleft()
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < n) and (0 <= ny < m):
            if visited[nx][ny] != 1:
                visited[nx][ny] = 1
                if tomatoes[nx][ny] != -1:
                    tomatoes[nx][ny] = 1
                    dates[nx][ny] = dates[x][y] + 1
                    queue.append([nx, ny])

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            print(-1)
            exit()

result = 0
for i in range(n):
    for j in range(m):
        if result < dates[i][j]:
            result = dates[i][j]

print(result)