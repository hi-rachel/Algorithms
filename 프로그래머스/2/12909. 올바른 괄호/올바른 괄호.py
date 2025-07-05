def solution(s):
    stack = []
    for bracket in s:
        if(len(stack) == 0):
            stack.append(bracket)
            continue
        if bracket == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(bracket)

    return True if len(stack) == 0 else False

