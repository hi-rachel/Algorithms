a, b = map(str, input().split())
if a[::-1] > b[::-1]:
    print(int(a[::-1]))
else:
    print(int(b[::-1]))