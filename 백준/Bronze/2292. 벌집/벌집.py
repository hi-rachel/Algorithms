n = int(input())

start = 1
steps = 1

while start < n:
  start += 6*steps
  steps += 1
print(steps)