N, M = map(int, input().split())
forest = list(map(int, input().split()))

start = 1
end = max(forest)

while start <= end:
    wood = 0
    mid = (start + end) // 2
    for tree in forest:
        if tree >= mid:
            wood += (tree - mid)
    
    if wood >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)