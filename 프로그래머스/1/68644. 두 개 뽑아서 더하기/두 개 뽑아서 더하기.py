from itertools import combinations

def solution(numbers):
    numbers = combinations(numbers, 2)
    answer = list(set(a + b for a, b in numbers))
    answer.sort()
    return answer
    