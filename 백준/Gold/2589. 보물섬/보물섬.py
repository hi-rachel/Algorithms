from collections import deque
import sys
input = sys.stdin.readline

y_size, x_size = map(int, input().split())

x_map = [list(input().rstrip()) for _ in range(y_size)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

max_distance = 0

for i in range(y_size):
    for j in range(x_size):
        if x_map[i][j] == 'L':
            visited = [[0 for _ in range(x_size)] for _ in range(y_size)] # 방문 기록
            dist = [[0 for _ in range(x_size)] for _ in range(y_size)] # 거리 기록
            queue = deque()
            queue.append([i, j])
            visited[i][j] = 1

            while queue:
                y, x = queue.popleft()

                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < y_size and 0 <= nx < x_size:
                        if x_map[ny][nx] == 'L' and visited[ny][nx] == 0:
                            queue.append([ny, nx])
                            visited[ny][nx] = 1
                            dist[ny][nx] = dist[y][x] + 1
                            max_distance = max(max_distance, dist[ny][nx])

print(max_distance)