import sys
input = sys.stdin.readline
from collections import deque

# 컴퓨터의 개수, 신뢰 관계 개수
N, M = map(int, input().split())
computers = [[] for _ in range(N + 1)]

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 1

    while queue:
        node = queue.popleft()
        for next_node in computers[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                cnt += 1

    return cnt

for _ in range(M):
    a, b = map(int, input().split()) # a가 b를 신뢰한다
    computers[b].append(a) # b를 해킹하면 a를 해킹할 수 있으므로 역방향 저장

max_hacks = 0
result = []

for i in range(1, N + 1):
    hacks = bfs(i)
    if hacks > max_hacks:
        max_hacks = hacks
        result = [i]
    elif hacks == max_hacks:
        result.append(i)

print(*result)