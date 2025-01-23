import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

def bfs(graph, n):
    colors = [0] * (n + 1) # 0: 방문 x, 1: 그룹 1, -1: 그룹 2
    
    for start in range(1, n + 1): # 모든 정점 방문
        if colors[start] != 0: # 방문했으면 pass
            continue
        
        queue = deque([start])
        colors[start] = 1 # 첫 그룹 설정
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0: # 방문하지 않았으면
                    colors[neighbor] = -colors[node] # 인접 노드의 반대 그룹으로 저장
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]: # 인접 노드와 같은 색깔이면
                    return False # 이분 그래프 x
    return True
    
for _ in range(K):
    # 정점의 개수, 간선의 개수
    V, E = map(int, input().split())
    lines = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        a, b = map(int, input().split())
        # 인접 리스트 만들기
        lines[a].append(b)
        lines[b].append(a)
        
    if bfs(lines, V) == True:
        print("YES")
    else:
        print("NO")