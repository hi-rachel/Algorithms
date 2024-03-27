import sys
input = sys.stdin.readline

n = int(input())

game_map = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

def move():
    for i in range(n):
        for j in range(n):
            k = game_map[i][j]

            if k == 0:
                continue

            if i+k < n:
                dp[i+k][j] += dp[i][j]

            if j+k < n:
                dp[i][j+k] += dp[i][j]
    return dp[-1][-1]

print(move())