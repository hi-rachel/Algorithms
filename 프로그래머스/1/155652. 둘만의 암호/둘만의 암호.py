def solution(s, skip, index):
    alpha = [chr(x) for x in range(97, 123)]
    
    for i in skip:
        alpha.remove(i) # 스킵할 문자 삭제

    result = ''
    for char in s:
        result += alpha[(alpha.index(char) + index) % len(alpha)]
    return result
    
    
    
        