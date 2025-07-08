"""
갈색 격자의 수, 노란색 격자의 수
카펫의 가로 길이 >= 세로 길이
카펫의 가로, 세로 크기를 순서대로 배열에 담아 반환해라
"""
def solution(brown, yellow):
    total = brown + yellow
    
    # 가장 작은 카펫 3 x 3
    for h in range(3, int(total ** 0.5) + 1):
        if total % h == 0:
            w = total // h
            if (w - 2) * (h - 2) == yellow:
                return [w, h]