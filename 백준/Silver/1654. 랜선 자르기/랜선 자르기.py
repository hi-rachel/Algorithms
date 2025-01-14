import sys
input = sys.stdin.readline

K, N = map(int, input().split())
K_list = [int(input()) for _ in range(K)]

def count_lanes(list, lane_len):
    return sum(num // lane_len for num in list)

def binary_search(list):
    start, end = 1, max(list)
    max_len = 0
    
    while start <= end:
        mid = (start + end) // 2
        cnt = count_lanes(K_list, mid)
        
        if cnt >= N:
            max_len = mid
            start = mid + 1
        else:
            end = mid - 1
    return max_len

print(binary_search(K_list))