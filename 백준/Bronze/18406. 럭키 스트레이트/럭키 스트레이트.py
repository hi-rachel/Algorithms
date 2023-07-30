n = list(input())

first = 0
second = 0

for i in range(len(n)):
  if i > len(n)/2-1:
    second += int(n[i])
  else:
    first += int(n[i])

if first == second:
  print('LUCKY')
else:
  print('READY')