import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

for _ in range(M):
    x, y = map(int, input().split())
    left_idx = bisect_left(dots, x)
    right_idx = bisect_right(dots, y)
    result = right_idx - left_idx
    print(result)