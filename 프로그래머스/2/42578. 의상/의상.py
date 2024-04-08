# 매일 다른 옷을 조합하여 입는다
# 각 종류별로 최대 1가지만 착용 가능
# 하루 최소 한 개의 의상은 착용!
# 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산

# [[의상의 이름, 의상의 종류], ...]
def solution(clothes):
    clothes_dict = {}
    answer = 1
    
    for i in range(len(clothes)):
        _, type = clothes[i]
        if type not in clothes_dict:
            clothes_dict[type] = 2
        else:
            clothes_dict[type] += 1        
    
    for value in clothes_dict.values():
        answer *= value
        
    return answer - 1