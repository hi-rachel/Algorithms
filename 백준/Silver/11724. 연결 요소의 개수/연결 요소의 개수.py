import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def recur(node):
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
            
        recur(nxt)
        
cnt = 0

for i in range(1, len(visited)):
    if visited[i] == 0:
        recur(i)
        cnt += 1

print(cnt)