import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = str(input().rstrip())

left, right = 0, 0
cnt = 0

while right < M:
    part = S[right:right+3]
    if part == 'IOI':
        right += 2
        if right - left == 2 * N:
            cnt += 1
            left += 2
    else:
        left = right = right + 1

print(cnt)