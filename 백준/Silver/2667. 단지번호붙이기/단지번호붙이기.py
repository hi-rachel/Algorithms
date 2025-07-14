import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def dfs(x, y):
    global cnt
    arr[x][y] = 3
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
            dfs(nx, ny)

houses = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i, j)
            houses.append(cnt)
                
houses.sort()
print(len(houses))
for house in houses:
    print(house)