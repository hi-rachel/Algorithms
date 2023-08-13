T = int(input())

for _ in range(T):
  statement = input().split()
  result = ""
  for word in statement:
    result += ''.join(reversed(word)) + ' '
  print(result)