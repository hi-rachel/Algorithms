import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [1, -1, -2, -2, -1, 1, 2, 2]

def bfs(start_x, start_y, target_x, target_y, I):
    visited = [[0] * I for _ in range(I)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()
        if x == target_x and y == target_y:
            return visited[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return 0

for _ in range(T):
    I = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    print(bfs(start_x, start_y, target_x, target_y, I))