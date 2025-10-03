import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
current_sum = 0
min_len = float('inf')

for right in range(N):
    current_sum += nums[right]
    
    while current_sum >= S:
        min_len = min(min_len, right - left + 1)
        current_sum -= nums[left]
        left += 1
     
if min_len == float('inf'):
    print(0)
else:
    print(min_len)