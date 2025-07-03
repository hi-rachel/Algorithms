"""
짝수번째 알파벳은 대문자로,
홀수번째 알파벳은 소문자로 바꾼 문자열을 반환해라

단어별로 짝홀수 인덱스 판단, 첫 글자 => 짝수
"""

def solution(s):
    answer = []
    words = s.split(' ')
    
    for word in words:
        temp = ''
        for i in range(len(word)):
            if i == 0 or i % 2 == 0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        answer.append(temp)
        
    return ' '.join(answer)