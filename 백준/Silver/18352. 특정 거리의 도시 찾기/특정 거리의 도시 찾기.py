from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

links = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    links[a].append(b)

q = deque([x])
dist[x] = 0

while q:
    node = q.popleft()

    for nxt in links[node]:
         if dist[nxt] == -1: 
            dist[nxt] = dist[node] + 1
            q.append(nxt)

check = False
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)