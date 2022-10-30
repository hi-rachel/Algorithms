list = []
for i in range(10):
  a = int(input())
  rest = a % 42
  list.append(rest)

s = set(list)
print(len(s))