import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split(' '))

queue = deque()

visited = [0] * (N+1)

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs(v):
    queue.append(v)
    cnt = 1
    visited[v] = 1

    while queue:
        u = queue.popleft()

        for ele in graph[u]:
            if visited[ele] == 0:
                cnt += 1
                queue.append(ele)
                visited[ele] = cnt

bfs(R)

for i in range(1, len(visited)):
    print(visited[i])