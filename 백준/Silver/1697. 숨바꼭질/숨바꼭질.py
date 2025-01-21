import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        if x == K:
            return dist[x]
        for num in (x-1, x+1, x*2):
            if 0 <= num <= MAX and not dist[num]:
                dist[num] = dist[x] + 1
                queue.append(num)

MAX = 10 ** 5
dist = [0] * (MAX+1)

print(bfs())