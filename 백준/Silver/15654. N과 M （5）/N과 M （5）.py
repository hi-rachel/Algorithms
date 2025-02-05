import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().strip().split(' ')))

ans = list(permutations(nums, M))
ans.sort()

for i in range(len(ans)):
    print(*ans[i])