import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
    
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
dfs(V)
print()
visited = [0] * (N + 1)
            
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    
bfs(V)