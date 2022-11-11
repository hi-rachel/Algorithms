import sys, heapq
input = sys.stdin.readline
heap = []

for _ in range(int(input())):
  num_arr = list(map(int, input().split()))
  if not heap:
    for x in num_arr:
      heapq.heappush(heap, x)
  else:
    for x in num_arr:
      if heap[0] < x:
        heapq.heappush(heap, x)
        heapq.heappop(heap)

print(heap[0])