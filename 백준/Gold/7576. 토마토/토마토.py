import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
tomatoes = [list(map(int, input().rstrip().split())) for _ in range(n)]

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

queue = deque()

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < n) and (0 <= ny < m):
            if tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append([nx, ny])

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            print(-1)
            sys.exit()

days = tomatoes[x][y] - 1
print(days)