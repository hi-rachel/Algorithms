def solution(want, number, discount):
    want_map = dict()
    for i in range(len(want)):
        want_map[want[i]] = number[i]
        
    sum_number = sum(number)
    cnt = 0
    
    for i in range(0, len(discount)-sum_number+1):
        comparison = want_map.copy()
        now = discount[i:i+sum_number]
        
        for j in range(len(now)): # 마트에서 할인 품목 세기
            if now[j] in comparison:
                comparison[now[j]] -= 1
            
        if (all(value == 0 for value in comparison.values())):
            cnt += 1
            
    return cnt
            
    