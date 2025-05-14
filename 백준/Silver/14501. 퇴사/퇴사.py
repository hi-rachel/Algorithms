import sys
input = sys.stdin.readline

N = int(input())
T_arr = []  # 상담 소요 기간
P_arr = []  # 상담 수익

dp = [0] * (N + 1)

for _ in range(N):
    T, P = map(int, input().split())
    T_arr.append(T)
    P_arr.append(P)

for i in range(N - 1, -1, -1):
    if i + T_arr[i] <= N:  # 퇴사일 전이라면
        dp[i] = max(P_arr[i] + dp[i + T_arr[i]], dp[i + 1])  # i일에 상담을 했을 때와 하지 않았을 때 중 더 큰 수익 선택
    else:
        dp[i] = dp[i + 1]

print(dp[0])