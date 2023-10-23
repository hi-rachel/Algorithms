l = int(input())
a = list(map(ord, list(input())))

result = 0
for i in range(l):
    cur = a[i] - 96
    result += cur * (31**i)

print(result % 1234567891)