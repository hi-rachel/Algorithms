from itertools import permutations

def solution(numbers):
    answer = []
    nums_list = list(numbers)
    per = []
    for i in range(1, len(numbers)+1):
        per += permutations(nums_list, i)
        new_list = [int(''.join(p)) for p in per]
        
    for num in new_list:
        if num < 2:
            continue
        check = True
        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                check = False
                break
        if check:
            answer.append(num)
                    
    return (len(set(answer)))