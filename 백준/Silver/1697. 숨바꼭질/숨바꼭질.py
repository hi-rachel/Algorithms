from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

MAX = 10 ** 5
dist = [0] * (MAX+1)
N, K = map(int, input().split())
bfs()