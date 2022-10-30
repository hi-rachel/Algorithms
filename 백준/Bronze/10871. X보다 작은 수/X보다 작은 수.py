import sys

n, x = map(int, input().split())
list = map(int, sys.stdin.readline().split())
for i in list:
  if i < x:
    print(i, end=' ')