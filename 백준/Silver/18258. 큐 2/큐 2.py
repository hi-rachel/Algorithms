from collections import deque
import sys
input = sys.stdin.readline

queue = deque()

n = int(input().rstrip())

for i in range(n):
    order = str(input()).rstrip()
    if (len(order.split()) == 2):
        a, b = order.split()
        if a == 'push':
            queue.append(b)
    else:
        if order == 'pop':
            if (queue):
                print(queue.popleft())
            else:
                print(-1)
        elif order == 'size':
            print(len(queue))
        elif order == "empty":
            if (queue):
                print(0)
            else:
                print(1)
        elif order == 'front':
            if (queue):
                print(queue[0])
            else:
                print(-1)
        elif order == 'back':
            if (queue):
                print(queue[-1])
            else:
                print(-1)