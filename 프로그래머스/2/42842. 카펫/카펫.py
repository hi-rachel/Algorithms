# 갈색 격자의 수, 노란색 격자의 수
# 카펫의 가로 길이 >= 세로 길이
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 반환해라
def solution(brown, yellow):
    answer = []
    blocks = brown + yellow
    
    for h in range(3, blocks//3+1):
        if blocks % h == 0:
            w = blocks//h
            if ((w-2) * (h-2) == yellow):
                answer = [w, h]
                break
    return answer