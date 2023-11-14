import sys
input = sys.stdin.readline

N = int(input())
request = list(map(int, input().split()))
M = int(input())

start = 1
end = max(request)

while start <= end:
    mid = (start + end) // 2
    budget = 0
    for one in request:
        if one <= mid:
            budget += one
        else:
            budget += mid

    if budget > M:
        end = mid - 1
    else:
        start = mid + 1
print(end)