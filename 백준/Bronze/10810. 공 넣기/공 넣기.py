n, m = map(int, input().split())

balls = []

for i in range(n):
  balls.append(0)

for p in range(m):
  i, j, k = map(int, input().split())
  while i <= j:
    balls[i-1] = k
    i += 1

print(' '.join(map(str, balls)))