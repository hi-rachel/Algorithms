s = str(input())

abc = 'abcdefghijklmnopqrstuvwxyz'

result = []

for i in range(len(abc)):
  result.append(s.find(abc[i]))

print(*result)