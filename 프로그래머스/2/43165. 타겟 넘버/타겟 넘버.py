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