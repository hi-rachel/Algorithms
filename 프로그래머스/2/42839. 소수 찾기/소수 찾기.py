from itertools import permutations

def is_prime(n):
    """소수 판별 함수"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # √n까지만 검사
        if n % i == 0:
            return False
    return True

def solution(numbers):
    unique_numbers = set()  # 중복 방지를 위해 set 사용

    # 1~N자리의 모든 순열을 생성하여 숫자로 변환
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            unique_numbers.add(int(''.join(p)))  # set을 사용해 중복 제거

    # 소수 개수 반환
    return sum(1 for num in unique_numbers if is_prime(num))