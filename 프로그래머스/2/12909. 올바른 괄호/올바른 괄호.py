def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            return False
    return not stack