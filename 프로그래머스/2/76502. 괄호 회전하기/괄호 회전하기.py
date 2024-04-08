def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        stack = []
        
        for bracket in s:
            if (len(stack) == 0):
                stack.append(bracket)
            elif bracket == "]" and stack[-1] == "[":
                stack.pop()
            elif bracket == "}" and stack[-1] == "{":
                stack.pop()
            elif bracket == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(bracket)

        if (len(stack) == 0):
            answer += 1
            
        s = s[1:] + s[0]
    
    return answer