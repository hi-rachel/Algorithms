import sys
input = sys.stdin.readline

N = int(input())
N_list = sorted(map(int, input().split()))
result = (0, 0)
min_sum = float('inf')

left, right = 0, N-1

while left < right:
    current_sum = N_list[left] + N_list[right]
    if abs(current_sum) < abs(min_sum):
        min_sum = current_sum
        result = (N_list[left], N_list[right])
    
    if current_sum > 0:
        right -= 1
    elif current_sum < 0:
        left += 1
    else:
        break
        
print(result[0], result[1])