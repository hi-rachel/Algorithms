def recur(start):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(start, N+1):
        if i in arr:
            continue
        arr.append(i)
        recur(i+1)
        arr.pop()
    
N, M = map(int, input().split())
arr = []
    
recur(1)