while True:
    a = input()
    stack = []

    if a == ".":
        break

    for c in a:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
                break
        elif c == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")