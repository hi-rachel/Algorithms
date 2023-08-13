import sys
n = int(input())

stack = [];

for _ in range(n):
  order = sys.stdin.readline().rstrip()
  if order == 'size':
    print(len(stack))
  elif order == 'pop':
    print(stack.pop() if stack else -1)
  elif order == 'top':
    print(stack[-1] if stack else -1)
  elif order == 'empty':
    print(0 if stack else 1)
  else:
    _, x = order.split()
    stack.append(int(x))