import sys
input = sys.stdin.readline
from collections import deque

def is_bipartite(graph, n):
    colors = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if colors[start] != 0:
            continue
        queue = deque([start])
        colors[start] = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
    return True

K = int(input())

for i in range(K):
    V, E = map(int, input().split())
    lines = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        lines[u].append(v)
        lines[v].append(u)

    if is_bipartite(lines, V):
        print("YES")
    else:
        print("NO")