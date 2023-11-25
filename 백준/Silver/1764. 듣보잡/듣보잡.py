import sys
input = sys.stdin.readline

n, m = map(int, input().split())

names = {}

for _ in range(n):
    names[str(input().rstrip())] = 1

for _ in range(m):
    x = str(input().rstrip())
    if x not in names.keys():
        names[x] = 1
    else:
        names[x] += 1

result = []
for key, value in names.items():
    if value == 2:
        result.append(key)

print(len(result))
result.sort()
for x in result:
    print(x)