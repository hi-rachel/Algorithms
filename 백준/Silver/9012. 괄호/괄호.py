import sys

input = sys.stdin.readline

T = int(input())

def is_valid_parenthesis(arr):
    stack = []
    for c in arr:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            return False
        # print(f"stack ${i}", stack, not stack)
    # print('i', stack)
    return not stack



for _ in range(T):
    s = list(input().rstrip())
    print("YES") if is_valid_parenthesis(s) else print("NO")