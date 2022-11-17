m = int(input())
n = int(input())
prime_numbers = []

for i in range(m, n + 1):
  if i == 1:
    pass
  elif i == 2:
    prime_numbers.append(i)
  else:
    for x in range(2, i):
      if i % x == 0:
        break
      elif x==i-1:
        prime_numbers.append(i)
if len(prime_numbers) == 0:
  print('-1')
else:
  print(sum(prime_numbers))
  print(min(prime_numbers))