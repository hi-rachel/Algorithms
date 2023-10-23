import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))

for _ in range(n):
    coin = coins.pop()
    if k // coin > 0:
        cnt += k // coin
        k = k % coin
    else:
        continue

print(cnt)