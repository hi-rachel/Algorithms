import sys

input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def recur(node):
    visited[node] = 1
    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        recur(nxt)


recur(1)

print(sum(visited) - 1)