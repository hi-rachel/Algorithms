def solution(number, limit, power):
    divisors = [0] * (number+1)
    divisors[1] = 1

    if number == 1:
        return divisors[number]

    for num in range(2, number+1):
        divisors[num] += divisors[num-1]
        for j in range(1, int(num ** 0.5)+1): # 1부터 num의 약수를 찾기 위한 루프(1부터 num의 제곱근까지)
            if num % j == 0: # 나누어 떨어지면 j와 num//j 모두 약수
                if j ** 2 == num:
                    divisors[num] += 1
                else:
                    divisors[num] += 2

        if divisors[num] - divisors[num-1] > limit:
            divisors[num] = power + divisors[num-1]

    return divisors[num]