m, n = map(int, input().split())

result = [0] * (n + 1)

for i in range(2, n + 1, 1):
    result[i] = i

for i in range(2, n + 1, 1):
    if result[i] == 0:
        continue

    for j in range(i + i, n + 1, i):
        result[j] = 0

result = result[m : n + 1]

for num in result:
    if num != 0:
        print(num)