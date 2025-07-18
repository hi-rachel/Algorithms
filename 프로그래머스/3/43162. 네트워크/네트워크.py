from collections import deque

def solution(n, computers):
    visited = [False] * n
    networks = 0

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            for neighbor in range(n):
                if computers[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            networks += 1

    return networks