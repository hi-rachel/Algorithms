a, b = input().split()
result = []

for i in range(len(b) - len(a) + 1):
  diff = 0
  for x in range(len(a)):
    if a[x] != b[i + x]:
      diff += 1
  result.append(diff)

print(min(result))