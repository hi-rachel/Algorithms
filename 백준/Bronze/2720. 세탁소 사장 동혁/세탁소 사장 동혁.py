t = int(input())

coins = [25, 10, 5, 1]

for _ in range(t):
  c = int(input())
  for coin in coins:
    print(c // coin, end=' ')
    c = c % coin