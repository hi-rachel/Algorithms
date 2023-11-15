import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input().rstrip()))

house.sort()
    
start = 1
end = house[-1] - house[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    now = house[0]
    cnt = 1
    for x in house:
        if x >= mid + now:
            cnt += 1
            now = x
    if cnt >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)