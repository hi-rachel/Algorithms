import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())

cards = []

for _ in range(n):
    heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
    exit()

cards_num = 0
while True:
    sum = 0
    sum += heappop(cards)
    sum += heappop(cards)
    cards_num += sum
    if len(cards) == 0:
        break
    heappush(cards, sum)

print(cards_num)