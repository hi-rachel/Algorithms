"""
음이 아닌 정수 리스트 numbers가 주어졌을 때,
순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버 (target)을 만드는 방법의 수를 반환

TC: O(2^N)
SC: O(N)
"""

def solution(numbers, target):
    stack = [(0, 0)]
    cnt = 0
    
    while stack:
        idx, total = stack.pop()
        if idx == len(numbers):
            if target == total:
                cnt += 1
            continue
    
        stack.append((idx+1, total+numbers[idx]))
        stack.append((idx+1, total-numbers[idx]))
    
    return cnt