import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split(' '))

graph = [[] for _ in range(N+1)]

visited = [0] * (N+1)

queue = deque()

for i in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

def bfs(v):
    queue.append(v)
    cnt = 1
    visited[v] = 1

    while queue:
        u = queue.popleft()

        for ele in graph[u]:
            if visited[ele] == 0:
                cnt += 1
                visited[ele] = cnt
                queue.append(ele)

bfs(R)

for i in range(1, len(visited)):
    print(visited[i])