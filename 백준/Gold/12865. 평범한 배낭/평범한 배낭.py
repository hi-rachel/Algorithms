import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0, 0]]
kanpsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            kanpsack[i][j] = kanpsack[i - 1][j]
        else:
            kanpsack[i][j] = max(
                value + kanpsack[i - 1][j - weight], kanpsack[i - 1][j]
            )

print(kanpsack[N][K])