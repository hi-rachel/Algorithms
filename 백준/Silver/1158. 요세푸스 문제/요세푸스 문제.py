from collections import deque
n, k = map(int, input().split())

def josephus():
    que = deque(range(1, n+1))

    answer = []
    
    while que:
        for _ in range(k-1):
            que.append(que.popleft())
        answer.append(que.popleft())

    return answer

print('<' + ', '.join(map(str, josephus())) + '>')