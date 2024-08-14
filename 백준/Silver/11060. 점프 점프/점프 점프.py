N = int(input())
dp = [0] * N
A_list = list(map(int, input().split()))
find = [False]

def min_jumps(arr):
    n = len(arr)

    dp = [float('inf')] * N
    dp[0] = 0

    for i in range(n):
        for j in range(1, arr[i] + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        
    return dp[-1] if dp[-1] != float('inf') else -1

print(min_jumps(A_list))