import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = str(input())

part = 'IOI'

for _ in range(N-1):
    if part[-1] == 'I':
        part += 'OI'

cnt = 0
len_part = len(part)

for i in range(0, len(S)-1):
    if S[i:i+len_part] == part:
        cnt += 1

print(cnt)