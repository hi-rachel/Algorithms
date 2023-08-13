import sys
n = int(input())

stack = [];

for _ in range(n):
  order = sys.stdin.readline().split()
  operator = order[0]
  if operator == 'push':
    stack.append(int(order[1]))
  elif operator == 'size':
    print(len(stack))
  elif operator == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
      stack.pop()
  elif operator == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
  elif operator == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)