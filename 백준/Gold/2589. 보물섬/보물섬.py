from collections import deque
import sys

input = sys.stdin.readline

Y, X = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(Y)]
maxi = 0

for y in range(Y):
    for x in range(X):
        if graph[y][x] == "L":
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            dist = [[0 for _ in range(X)] for _ in range(Y)]

            q = deque()
            q.append([y, x])
            visited[y][x] = 1

            while q:
                ey, ex = q.popleft()

                for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ny, nx = ey + dy, ex + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if graph[ny][nx] == "L":
                            if visited[ny][nx] == 0:
                                visited[ny][nx] = 1
                                dist[ny][nx] = dist[ey][ex] + 1
                                maxi = max(maxi, dist[ny][nx])
                                q.append([ny, nx])

print(maxi)
