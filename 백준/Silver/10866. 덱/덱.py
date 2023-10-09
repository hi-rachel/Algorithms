from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    order = input().split()
    if order[0] == "push_front":
        queue.appendleft(int(order[1]))
    elif order[0] == "push_back":
        queue.append(int(order[1]))
    elif order[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        size = len(queue)
        if size >= 1:
            print(0)
        else:
            print(1)
    elif order[0] == "back":
        if queue:
            print(queue[len(queue) - 1])
        else:
            print(-1)
    elif order[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)