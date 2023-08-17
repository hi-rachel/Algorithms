import sys

n = int(sys.stdin.readline())
find = int(sys.stdin.readline())

graph = [[0]*(n) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = n//2, n//2

graph[x][y] = 1

num = 2

size = 3

while (x != 0 or y != 0):
  while (num <= size * size):

    if (x == y == (n//2)):
      up, right, down, left = size, size-2, size-1, size-1

      x += dx[0]
      y += dy[0]
      up -= 1

    elif (right > 0):
      x += dx[3]
      y += dy[3]
      right -= 1
    elif (down > 0):
      x += dx[1]
      y += dy[1]
      down -= 1
    elif (left > 0):
      x += dx[2]
      y += dy[2]
      left -= 1
    else:
      x += dx[0]
      y += dy[0]
      up -= 1

    graph[x][y] = num
    num += 1

  size += 2
  n -= 2

find_x, find_y = -1, 1

for i in range(len(graph)):
  for j in range(len(graph)):
    if (graph[i][j] == find):
      find_x, find_y = i, j
    print(graph[i][j], end=' ')
  print('')

print(find_x + 1, find_y + 1)