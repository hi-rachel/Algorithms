import sys
input = sys.stdin.readline
for _ in range(int(input())):
  statement = input().split()
  print(' '.join(statement[::-1])[::-1])