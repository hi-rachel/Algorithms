import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
tang = list(map(int, input().split()))

max_len = 0
left = 0
right = 0
fruit_count = defaultdict(int)
unique_fruits = 0

for right in range(N):
    if fruit_count[tang[right]] == 0:
        unique_fruits += 1
    fruit_count[tang[right]] += 1

    while unique_fruits > 2:
        fruit_count[tang[left]] -= 1
        if fruit_count[tang[left]] == 0:
            unique_fruits -= 1
        left += 1
    
    max_len = max(max_len, right-left+1)

print(max_len)