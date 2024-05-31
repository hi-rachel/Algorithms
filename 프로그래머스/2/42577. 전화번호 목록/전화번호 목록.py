# 어떤 번호가 다른 번호의 접두인 경우가 있으면 false, 아니면 true를 반환
def solution(phone_book):
    hash_map = {}
    for phone_nums in phone_book:
        hash_map[phone_nums] = 1
    
    for nums in phone_book:
        arr = ''
        for num in nums:
            arr += num
            
            if arr in hash_map and arr != nums:
                return False
    return True