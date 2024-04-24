import sys
from collections import deque

input = sys.stdin.readline

def bfs(weight):
    queue = deque()
    queue.append(x)
    visited = [False] * (n+1)
    visited[x] = True

    while queue:
        island = queue.popleft()

        for i, w in graph[island]:
            if not visited[i] and w >= weight:
                visited[i] = True
                queue.append(i)

    if visited[y]: return True
    else: return False

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

x, y = map(int, input().split())

start = 1
end = 10000000000

result = 0
while start <= end:
    mid = (start + end) // 2
    
    if bfs(mid):
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)