"""
짝수번째 알파벳은 대문자로,
홀수번째 알파벳은 소문자로 바꾼 문자열을 반환해라

단어별로 짝홀수 인덱스 판단, 첫 글자 => 짝수

TC: O(n)
SC: O(n)
"""

def solution(s):
    answer = []
    
    for word in s.split(' '):
        temp = []
        
        for i, c in enumerate(word):
            if i % 2 == 0:
                temp.append(word[i].upper())
            else:
                temp.append(word[i].lower())
        answer.append(''.join(temp))
        
    return ' '.join(answer)