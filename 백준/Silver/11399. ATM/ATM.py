N = int(input())

P = list(map(int, input().split()))

P.sort()

result = 0
now = 0
for n in P:
    now += n
    result += now

print(result)