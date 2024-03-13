from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

max_rain = 0

graph = []
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    max_row = max(row)
    max_rain = max(max_rain, max_row)

now_rain = 1

max_safe_area = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt_list = []

def bfs(i, j, k):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] > k:
                        visited[nx][ny] = 1
                        queue.append([nx, ny])

for rain_height in range(max_rain+1):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    safe_area_cnt = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > rain_height and visited[i][j] == 0:
                bfs(i, j, rain_height)
                safe_area_cnt += 1

    max_safe_area = max(max_safe_area, safe_area_cnt)

print(max_safe_area)