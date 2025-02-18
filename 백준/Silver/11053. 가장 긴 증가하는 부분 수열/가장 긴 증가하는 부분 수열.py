import bisect

def longest_increasing_subsequence(arr):
    dp = []
    for num in arr:
        idx = bisect.bisect_left(dp, num)
        
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
            
    return len(dp)

n = int(input())
arr = list(map(int, input().split()))

print(longest_increasing_subsequence(arr))