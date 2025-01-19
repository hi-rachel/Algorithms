import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

def is_possible(max_size):
    cnt, current_sum = 1, 0
    for num in N_list:
        if num + current_sum > max_size:
            cnt += 1
            current_sum = num
        else:
            current_sum += num
    return cnt <= M
    
left, right = max(N_list), sum(N_list)
result = right

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        result = mid
        right = mid -1
    else:
        left = mid + 1
        
print(result)