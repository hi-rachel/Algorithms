import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())

tree = [[] for _ in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (N+1)

visited = [False] * (N+1)

def bfs():
    queue = deque()
    queue.append(1)
    parents[1] = 0

    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if parents[child] == 0:
                parents[child] = node
                queue.append(child)

bfs()

for i in range(2, N+1):
    print(parents[i])