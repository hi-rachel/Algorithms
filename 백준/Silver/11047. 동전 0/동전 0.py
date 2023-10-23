import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))

for _ in range(n):
    if k == 0:
        break
    coin = coins.pop()
    while k >= coin:
        k -= coin
        cnt += 1

print(cnt)