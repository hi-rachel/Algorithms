import sys
input = sys.stdin.readline

while True:
    word = list(str(input().rstrip()))
    if word == ["0"]:
        break
    check = list(reversed(word))
    if word == check:
        print("yes")
    else:
        print("no")