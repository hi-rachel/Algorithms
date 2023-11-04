from collections import deque
def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    if target not in words:
        return 0
        
    def compare_diff(a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False
    
    def bfs(start):
        queue = deque()
        queue.append((start, 0))
        
        while queue:
            now = queue.popleft()
            
            if now[0] == target:
                return now[1]
            
            for i in range(len(words)):
                if compare_diff(now[0], words[i]) and visited[i] == 0:
                    queue.append((words[i], now[1] + 1))
                    visited[i] = 1

    return bfs(begin)
            