import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

t = int(input())

def DFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            DFS(nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                DFS(i, j)
                cnt += 1

    print(cnt)