def solution(ingredient):
    hamberger = []
    cnt = 0
    for i in ingredient:
        hamberger.append(i)
        if hamberger[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                hamberger.pop()
    return cnt
    