"""
i번째 숫자부터 j번째 숫자까지 자르고 정렬했을때,
k번째에 있는 수를 구하려고 한다.
"""

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        slice_arr = sorted(array[i-1:j])
        answer.append(slice_arr[k-1])
        
    return answer