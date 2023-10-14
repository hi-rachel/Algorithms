n, m = map(int, input().split())

s = list(map(int, input().split()))

for _ in range(m):
    a, l, r = map(int, input().split())
    if a == 1:
        s[l - 1] = r
    elif a == 2:
        for idx in range(l, r + 1):
            if s[idx - 1] == 0:
                s[idx - 1] = 1
            else:
                s[idx - 1] = 0
    elif a == 3:
        for idx in range(l, r + 1):
            s[idx - 1] = 0
    elif a == 4:
        for idx in range(l, r + 1):
            s[idx - 1] = 1

print(*s)