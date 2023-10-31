from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(node):
    visited[node] = 1
    print(node, end=" ")
    for nxt in graph[node]:
        if visited[nxt] != 1:
            dfs(nxt)

dfs(v)
print()

visited = [0 for _ in range(n + 1)]

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 1
    while q:
        now = q.popleft()
        print(now, end=" ")
        for nxt in graph[now]:
            if visited[nxt] != 1:
                visited[nxt] = 1
                q.append(nxt)

bfs(v)