import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input().rstrip())

tree = [[] for _ in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (N+1)

def dfs(node, parent):
    parents[node] = parent
    for child in tree[node]:
        if parents[child] == 0:
            dfs(child, node)

dfs(1, 0)

for i in range(2, N+1):
    print(parents[i])