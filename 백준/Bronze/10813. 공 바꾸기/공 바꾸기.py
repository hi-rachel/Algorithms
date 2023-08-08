n, m = map(int, input().split())

balls = []

for i in range(1, n+1):
  balls.append(i)

for _ in range(m):
  i, j = map(int, input().split())
  temp = balls[i-1]
  balls[i-1] = balls[j-1]
  balls[j-1] = temp

print(*balls)