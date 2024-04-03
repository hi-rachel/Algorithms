def solution(number, limit, power):
    divisors = [0 for _ in range(number+1)]
    divisors[1] = 1
    
    if number == 1:
        return divisors[number]
    
    for num in range(2, number+1):
        divisors[num] += divisors[num-1]
        for j in range(1, int(num ** 0.5)+1): # 1부터 num의 약수를 찾기 위한 루프(1부터 num의 제곱근까지)
            if num % j == 0: # 나누어 떨어지면 j와 num//j 모두 약수
                divisors[num] += 2
                
        if num ** 0.5 % 1 == 0: # 만약 num이 완전제곱수(제곱근이 정수)인 경우, 약수 중 하나가 중복으로 세어짐
            divisors[num] -= 1
        if divisors[num] - divisors[num-1] > limit:
            divisors[num] = power + divisors[num-1]
            
    return divisors[num]