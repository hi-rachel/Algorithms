def solution(n, times):
    start, end = 1, max(times) * n
    answer = end
    
    while start <= end:
        mid = (start + end) // 2
        people = sum(mid // time for time in times)

        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer