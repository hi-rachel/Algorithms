t = int(input())

for i in range(t):
    stack = []
    guess = input()
    for c in guess:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")