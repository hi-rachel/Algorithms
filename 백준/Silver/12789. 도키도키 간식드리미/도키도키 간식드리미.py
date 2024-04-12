import sys
input = sys.stdin.readline

stack = []

n = int(input().rstrip())
students = list(map(int, input().split()))

strict_num = 1

for student in students:
    stack.append(student)
    while stack and stack[-1] == strict_num:
        stack.pop()
        strict_num+=1
        
if stack:
    print("Sad")
else:
    print("Nice")