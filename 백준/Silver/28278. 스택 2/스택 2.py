from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

stack_ = deque()

for _ in range(n):
    order = list(map(int, input().split()))
    if order[0] == 1:
        stack_.append(order[1])
    elif order[0] == 2:
        if stack_:
            print(stack_.pop())
        else:
            print(-1)
    elif order[0] == 3:
        print(len(stack_))
    elif order[0] == 4:
        if stack_:
            print(0)
        else:
            print(1)
    elif order[0] == 5:
        if stack_:
            print(stack_[-1])
        else:
            print(-1)