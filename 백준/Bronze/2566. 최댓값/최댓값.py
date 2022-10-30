import sys
input = sys.stdin.readline

A = []

for _ in range(9):
  A.append(list(map(int, input().split())))

x = 0
y = 0
MAX = -1

for row in range(9):
  for col in range(9):
    if A[row][col] > MAX:
      MAX = A[row][col]
      x = row + 1
      y = col + 1

print(MAX)
print(x, y)