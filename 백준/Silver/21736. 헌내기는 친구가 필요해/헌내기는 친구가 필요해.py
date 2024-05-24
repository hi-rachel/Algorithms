import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

campus = []
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(start):
    person = 0
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if visited[nx][ny] != 1 and campus[nx][ny] != 'X':
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    if campus[nx][ny] == 'P':
                        person += 1
    return person

for _ in range(N):
    campus.append(list(map(str, input().rstrip())))

for i in range(N):
    if 'I' in campus[i]:
        answer = bfs([i, campus[i].index('I')])
        if answer == 0:
            print('TT')
        else:
            print(answer)