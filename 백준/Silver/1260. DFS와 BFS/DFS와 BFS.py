import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def recur(node):
    visited[node] = 1
    print(node, end=" ")
    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        recur(nxt)

recur(V)
print()

visited = [0 for _ in range(N + 1)]

q = deque()
q.append(V)
visited[V] = 1

while len(q) > 0:
    node = q.popleft()
    print(node, end=" ")
    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        visited[nxt] = 1
        q.append(nxt)