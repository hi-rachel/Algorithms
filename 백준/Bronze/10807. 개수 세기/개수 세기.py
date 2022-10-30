import sys
n = int(input())
int_list = list(map(int, sys.stdin.readline().split()))
v = int(input())
count = 0

for i in int_list:
  if i == v:
    count += 1

print(count)