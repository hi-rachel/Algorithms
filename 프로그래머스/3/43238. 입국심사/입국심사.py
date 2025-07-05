"""
결정 문제 -> 이분 탐색

시간 범위: 1 ~ max(times) * n

TC: O(log(max(times) × n) × m), m = len(times)
SC: O(1)
"""

def solution(n, times):
    left = 0
    right = max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        total = sum(mid // time for time in times)
        
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer