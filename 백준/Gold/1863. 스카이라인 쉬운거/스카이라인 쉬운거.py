import sys
input = sys.stdin.readline

n = int(input())

skilines = []
cnt = 0

for i in range(n):
    x, y = map(int, input().split())
    skilines.append(y)

skilines.append(0)

stack = [0]
for height in skilines:
    now = height
    while stack[-1] > height:
        if stack[-1] != now:
            cnt += 1
            now = stack[-1]
        stack.pop()
    stack.append(height)

print(cnt)