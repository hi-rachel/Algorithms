N, M = map(int, input().split())

S = {}
cnt = 0

for _ in range(N):
    x = str(input())
    S[x] = 0

for _ in range(M):
    x = str(input())
    if x in S:
        cnt += 1

print(cnt)