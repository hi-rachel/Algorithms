n, m = map(int, input().split())

balls = [*range(1, n+1)]

for _ in range(m):
  i, j = map(int, input().split())
  temp = balls[i-1:j]
  temp.reverse()
  balls[i-1:j] = temp

print(*balls)