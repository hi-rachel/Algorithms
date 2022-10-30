import sys

n = int(input())
time = list(map(int, sys.stdin.readline().split()))
Y = M = 0
for n in time:
  Y += (n // 30 + 1) * 10
  M += (n // 60 + 1) * 15
if Y < M:
  print("Y", Y)
elif Y == M:
  print("Y", "M", Y)
else:
  print("M", M)