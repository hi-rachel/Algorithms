import sys
import heapq
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    x = int(input()) * -1
    if x == 0:
        if len(li) == 0:
            print(0)
        else:
            print(-heapq.heappop(li))
    else:
        heapq.heappush(li, x)