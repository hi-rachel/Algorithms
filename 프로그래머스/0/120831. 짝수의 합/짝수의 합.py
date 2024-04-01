# 정수 n이 주어질 때, n 이하의 짝수를 모두 더한 값을 반환해라

def solution(n):
    answer = 0
    for num in range(1, n+1):
        if num % 2 == 0:
            answer += num
    return answer