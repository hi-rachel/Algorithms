N, M = map(int, input().split())

S = [str(input()) for _ in range(N)]
cnt = 0
for _ in range(M):
    x = str(input())
    if x in S:
        cnt += 1

print(cnt)