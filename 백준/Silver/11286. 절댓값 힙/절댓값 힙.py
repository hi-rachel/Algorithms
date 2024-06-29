import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heappush(heap, (abs(x), x))
    elif len(heap) == 0:
        print(0)
    else:
        print(heappop(heap)[1])