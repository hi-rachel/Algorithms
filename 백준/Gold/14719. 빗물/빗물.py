h, w = map(int, input().split())
h_list = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    left_max = max(h_list[:i])
    right_max = max(h_list[i+1:])
    
    compare = min(left_max, right_max)
    
    if h_list[i] < compare:
        ans += compare - h_list[i]
    
print(ans)