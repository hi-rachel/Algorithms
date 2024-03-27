def solution(seoul):
    result = 0
    for idx, val in enumerate(seoul):
        if val == 'Kim':
            result = idx
    return f"김서방은 {result}에 있다"