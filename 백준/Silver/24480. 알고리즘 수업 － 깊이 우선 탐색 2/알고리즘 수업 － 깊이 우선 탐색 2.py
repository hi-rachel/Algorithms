import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

def dfs(graph, visited, r):
    global cnt
    visited[r] = cnt

    for x in graph[r]:
        if visited[x] == 0:
            cnt += 1
            dfs(graph, visited, x)
            
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)

dfs(graph, visited, R)

for i in range(1, N+1):
    print(visited[i])