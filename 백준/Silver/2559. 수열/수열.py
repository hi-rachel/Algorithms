import sys
input = sys.stdin.readline

# 온도를 측정한 전체 날짜의 수, 합을 구하기 위한 연속적인 날짜의 수
N, K = map(int, input().split())
arr = list(map(int, input().split()))

window_sum = sum(arr[:K])
max_temp = sum(arr[:K])

for i in range(K, len(arr)):
    window_sum = window_sum - arr[i - K] + arr[i]
    max_temp = max(max_temp, window_sum)

print(max_temp)