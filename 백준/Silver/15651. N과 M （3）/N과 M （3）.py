def recur(number):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr.append(i)
        recur(i+1)
        arr.pop()
    
N, M = map(int, input().split())
arr = []
    
recur(1)