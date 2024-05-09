import sys
import heapq

input = sys.stdin.readline

n = int(input())
que = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(que) == 0:
            print(0)
        else:
            print(heapq.heappop(que))
    else:
        heapq.heappush(que, x)