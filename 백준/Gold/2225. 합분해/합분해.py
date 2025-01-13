import sys
input = sys.stdin.readline

MOD = 1000000000

def solve(N, K):
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    for k in range(1, K + 1):
        dp[k][0] = 1

    for k in range(1, K + 1):
        for n in range(1, N + 1):
            dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % MOD

    return dp[K][N]

N, K  = map(int, input().split())
print(solve(N, K))