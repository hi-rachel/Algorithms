origin = set(range(1, 10001))
n = set()

for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  n.add(i)

self_num = sorted(origin - n)
for i in self_num:
  print(i)