from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dist = [[-1] * M for _ in range(N)]

q = deque()

for y in range(N):
    for x in range(M):
        if graph[y][x] == 2:
            target = [y, x]
            q.append(target)
            break

dist[target[0]][target[1]] = 0

while q:
    ey, ex = q.popleft()

    for dy, dx in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        ny, nx = ey + dy, ex + dx
        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[ey][ex] + 1
                q.append([ny, nx])

for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            print(0, end=' ')
        else:
            print(dist[y][x], end=' ')
    print()