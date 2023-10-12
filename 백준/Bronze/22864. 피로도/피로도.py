tired = 0
time = 0
work = 0
a, b, c, m = map(int, input().split())

if a > m:
    print(0)
    exit(0)

while time < 24:
    if tired + a <= m:
        tired += a
        work += b
        time += 1
    else:
        tired -= c
        time += 1
        if tired < 0:
            tired = 0
print(work)