import sys
n = int(input())
array = [int(sys.stdin.readline().strip()) for i in range(n)]
array.sort()
for i in array:
  print(i)