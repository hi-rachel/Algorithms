from itertools import combinations
import math

def solution(nums):
    answer = 0
    def is_Prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True
    
    # 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구한다
    for comb in combinations(nums, 3):
        if is_Prime(sum(list(comb))):
            answer += 1

    return answer