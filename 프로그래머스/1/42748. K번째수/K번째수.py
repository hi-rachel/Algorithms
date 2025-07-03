"""
i번째 숫자부터 j번째 숫자까지 자르고 정렬했을때,
k번째에 있는 수를 구하려고 한다.

TC: O(n log n)
SC: O(n)
"""

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]