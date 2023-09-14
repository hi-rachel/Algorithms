a, b, c, d, e, f = map(int, input().split())

for x in range(-1000, 1001):
    for y in range(-1000, 1001):
        if a * x + b * y == c:
            if d * x + e * y == f:
                print(x, y)
                break