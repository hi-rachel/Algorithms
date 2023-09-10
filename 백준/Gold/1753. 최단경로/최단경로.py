import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

links = [[] for _ in range(v + 1)]
dist = [1e9 for _ in range(v + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    links[u].append([v, w])
    
q = []
heapq.heappush(q, [0, k])
dist[k] = 0

while q:
    _w, node = heapq.heappop(q)
    
    for nxt, weight in links[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])

for i in range(1, len(dist)):
    print('INF') if dist[i] == 1e9 else print(dist[i])