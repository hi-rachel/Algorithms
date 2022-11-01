import sys
input = sys.stdin.readline
n = int(input())
paper = [[0]*101 for i in range(101)]

for _ in range(n):
  a, b = map(int, input().split())
  for i  in range(10):
    for j in range(10):
      paper[a+i][b+j] = 1

count = 0
for i in paper:
  count += sum(i)
print(count)