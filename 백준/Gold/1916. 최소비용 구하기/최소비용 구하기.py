import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

links = [[] for _ in range(n + 1)]
dist = [1e9 for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    links[a].append([b, c])

start, end = map(int, input().split())

q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q:
    _w, node = heapq.heappop(q)

    if dist[node] < _w:
        continue
    
    for nxt, weight in links[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])

print(dist[end])