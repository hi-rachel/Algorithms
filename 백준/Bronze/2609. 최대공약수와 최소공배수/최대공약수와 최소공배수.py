a, b = map(int, input().split())

max_num = b if b >= a else a

one = []
for i in range(1, max_num):
    if a % i == 0 and b % i == 0:
        one.append(i)

if a == b:
    one.append(a)

result1 = max(one)
result2 = (a // result1) * (b // result1) * result1

print(result1)
print(result2)