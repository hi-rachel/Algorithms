# 매 순간 가장 무거운 사람, 가장 가벼운 사람의 조합

def solution(people, limit):
    answer = 0
    people.sort()
    
    start = 0
    end = len(people) - 1
    
    while (start <= end):
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            answer += 1
        else:
            end -=1
            answer += 1

    return answer